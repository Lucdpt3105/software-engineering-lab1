import mysql.connector, os

def get_conn():
    return mysql.connector.connect(
        user=os.getenv("DB_USER","root"),
        password=os.getenv("DB_PASS","123456"),
        host=os.getenv("DB_HOST","127.0.0.1"),
        database=os.getenv("DB_NAME","atm_demo"),
        autocommit=False,
    )

