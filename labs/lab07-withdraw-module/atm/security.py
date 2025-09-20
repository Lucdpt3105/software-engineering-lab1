import hashlib, hmac, os

def sha256(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()

def verify_pin_hash(pin: str, expected_hash: str) -> bool:
    # so khớp constant-time hạn chế timing attack
    return hmac.compare_digest(sha256(pin), expected_hash)

