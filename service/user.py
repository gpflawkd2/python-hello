from datetime import timedelta, datetime
from jose import jwt
import bcrypt
from data import user as data
from model.user import User, DB_User

# 시크릿 키 설정
SECRET_KEY = "AC9166628A1DC87650DC3724721C55761F93B8897C0664862081B7DEFE7129EA"
ALGORITHM = "HS256"

# 회원 조회
def find_user(username):
    if (user := data.find_user(username)):
        return user
    return None

# 비밀번호 조회
def verify_password(password : str, hashed_password : str):
    password = password.encode("utf-8")
    hashed_password = hashed_password.encode("utf-8")
    is_valid = bcrypt.checkpw(password, hashed_password)
    return is_valid

# 비밀번호 해시처리
def make_hash_password(password : str):
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password.decode("utf-8")

def auth_user(username, password):
    user = find_user(username)
    if not user:
        return None
    password_check = verify_password(password, user.hashed_password)
    if not password_check:
        return None
    return user

# 토큰 생성
def create_access_token(data : dict, expire : timedelta):
    data = data.copy()
    now = datetime.utcnow()
    data.update({"exp":now + expire})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 회원가입
def create_user(user:DB_User):
    user = DB_User(name=user.name, email=user.email, hashed_password=make_hash_password(user.hashed_password))
    return data.create_user(user)