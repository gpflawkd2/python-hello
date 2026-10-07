from datetime import timedelta, datetime
from jose import jwt
import bcrypt
from data import user as data
from model.user import User, DB_User
from fastapi import HTTPException

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

# 토큰 분해
def decode_token(token:str):
    payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    if not (username := payload.get("sub")):
        return None
    return username

# 유저 조회
def get_current_user(token:str):
    username = decode_token(token)
    user = find_user(username)
    if not user:
        raise HTTPException(
            status_code = 401,
            detail = "올바르지 않은 인증정보입니다.",
            headers={"WWW-Authenticate" : "Bearer"}
        )
    return user.name 

# 가짜 데이터 생성
_fake_db = {"spongebob" : True, "jane" : False}

# web에서 요청한 checkuser 반환
# 게시판 접근 여부 판단
def check_usable(token:str):
    username = get_current_user(token)
    if _fake_db[username]:
        return True
    return False

def check_user(token:str):
    check = check_usable(token)
    return check