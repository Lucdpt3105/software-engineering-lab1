from atm.withdraw import verify_pin, withdraw

card = "CARD-0001"
pin = "1234"

if verify_pin(card, pin):
    ok = withdraw(card, 200000.00)
    print("Withdraw:", "SUCCESS" if ok else "FAILED (insufficient funds)")
else:
    print("PIN invalid or card blocked")

