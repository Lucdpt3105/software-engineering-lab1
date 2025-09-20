from .db import get_conn
from .security import verify_pin_hash
import mysql.connector

def verify_pin(card_no: str, pin: str) -> bool:
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute("SELECT pin_hash, status FROM cards WHERE card_no=%s", (card_no,))
        row = cur.fetchone()
        if not row: return False
        pin_hash, status = row
        if status != "ACTIVE": return False
        return verify_pin_hash(pin, pin_hash)
    finally:
        conn.close()

def withdraw(card_no: str, amount: float) -> bool:
    if amount <= 0:
        raise ValueError("Amount must be > 0")
    conn = get_conn()
    try:
        cur = conn.cursor()
        conn.start_transaction()
        cur.execute("""
            SELECT a.account_id, a.balance
            FROM accounts a JOIN cards c USING(account_id)
            WHERE c.card_no=%s FOR UPDATE
        """, (card_no,))
        row = cur.fetchone()
        if not row:
            raise RuntimeError("Card not found")
        account_id, balance = row
        if balance < amount:
            # ghi log giao dịch thất bại
            cur.execute("""
                INSERT INTO transactions(account_id,card_no,atm_id,tx_type,amount,balance_after,status)
                VALUES(%s,%s,1,'WITHDRAW',%s,%s,'FAILED')
            """, (account_id, card_no, amount, balance))
            conn.commit()
            return False
        # trừ tiền
        cur.execute("UPDATE accounts SET balance=balance-%s WHERE account_id=%s",
                    (amount, account_id))
        cur.execute("""
            INSERT INTO transactions(account_id,card_no,atm_id,tx_type,amount,balance_after,status)
            VALUES(%s,%s,1,'WITHDRAW',%s,
                   (SELECT balance FROM accounts WHERE account_id=%s),'SUCCESS')
        """, (account_id, card_no, amount, account_id))
        conn.commit()
        return True
    except mysql.connector.Error as e:
        conn.rollback()
        raise
    finally:
        conn.close()

