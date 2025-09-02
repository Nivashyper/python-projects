import bcrypt

def hash_password(pw: str) -> bytes:
    return bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

def verify(pw: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(pw.encode(), hashed)

if __name__ == "__main__":
    h = hash_password("secret123")
    print("hash:", h)
    print("ok:", verify("secret123", h))
