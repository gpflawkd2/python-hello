import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="token")

# 사용 데이터 구현
class User(BaseModel):
    name: str
    email: str
    
class DB_User(User):
    hashed_password: str
    
# 임시 데이터    
fake_user_db = {
    "spongebob" : {
        "name" : "SpongeBob",
        "email" : "sponge@example.com",
        "hashed_password" : "hashed_1234",
        "active" : False
    },
    "jane" : {
        "name" : "jane",
        "email" : "jane@example.com",
        "hashed_password" : "hashed_5678",
        "active" : True
    }
}

# 로그인을 지원하기 위해 필요한 함수
def fake_hash_password(password: str):
    return "hashed_" + password

# 로그인 기능 구현
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_user_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="아이디와 비밀번호를 정확하게 입력해주세요.")
    h_password = fake_hash_password(form_data.password)
    if not h_password == user_dict["hashed_password"]:
        raise HTTPException(status_code=400, detail="비밀번호가 잘못되었습니다.")
    return {"access_token" : form_data.username, "token_type" : "bearer"}

#유저 데이터 조회
def get_user(db, username : str) :
    user_dict = db.get(username)
    return user_dict

# 토큰을 해체하여 유저 정보 확인
def fake_decode_token(token : str):
    user  = get_user(fake_user_db, token)
    return user

# 토큰을 넘겨준 유저의 정보 조회
async def get_current_user(token:str = Depends(oauth2)):
    # 토큰 분해
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(status_code=401,
                            detail="올바르지 않은 인증정보입니다.",
                            headers={"WWW-Authenticate" : "Bearer"}
                            )
    return user

# 활성 사용자 여부 체크
async def get_current_active_user(current_user : dict =  Depends(get_current_user)):
    if current_user["active"]:
            return current_user
    else :
        raise HTTPException(status_code=400, detail="휴면 유저입니다.")

# 접속한 유저 정보를 확인하는 기능 구현
@app.get("/users/login_data")
async def read_me(current_user : dict = Depends(get_current_active_user)):
    return current_user


if __name__ == "__main__":
    uvicorn.run("oauth:app", reload=True, host="0.0.0.0", port=8000)