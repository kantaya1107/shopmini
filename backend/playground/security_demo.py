"""ทดลองฟังก์ชันใน app/core/security.py  (รันที่โฟลเดอร์ backend: python -m playground.security_demo)"""
from datetime import datetime, timedelta, timezone

import jwt

from app.core.config import settings
from app.core.security import create_access_token, decode_access_token, hash_password, verify_password

# 1) Hash รหัสผ่านเดียวกัน 2 ครั้ง ได้ผลไม่เหมือนกัน เพราะ bcrypt สุ่ม Salt ใหม่ทุกครั้ง
h1 = hash_password("Passw0rd!")
h2 = hash_password("Passw0rd!")
print("hash 1:", h1)
print("hash 2:", h2)
print("ตรวจรหัสถูก:", verify_password("Passw0rd!", h1), "| ตรวจรหัสผิด:", verify_password("wrong", h1))

# 2) สร้างและถอด JWT
token = create_access_token(subject="2", extra_claims={"role": "customer"})
header, payload, signature = token.split(".")
print("Token มี 3 ส่วน:", len(header), len(payload), len(signature), "ตัวอักษร")
print("Payload:", decode_access_token(token))

# 3) แก้ Token แม้แต่ตัวอักษรเดียว การตรวจลายเซ็นจะไม่ผ่านทันที
tampered = token[:-2] + ("AA" if token[-2:] != "AA" else "BB")
try:
    decode_access_token(tampered)
except jwt.InvalidTokenError as e:
    print("Token ถูกแก้ไข:", type(e).__name__)

# 4) Token หมดอายุ
expired = jwt.encode(
    {"sub": "2", "exp": datetime.now(timezone.utc) - timedelta(minutes=1)},
    settings.secret_key,
    algorithm=settings.algorithm,
)
try:
    decode_access_token(expired)
except jwt.ExpiredSignatureError as e:
    print("Token หมดอายุ:", type(e).__name__)