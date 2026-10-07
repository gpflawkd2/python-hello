from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.user import User, DB_User
from service import user as service
from datetime import timedelta
from error import Missing, Duplicate

router = APIRouter(prefix="/user")

# jwt에 사용할 기본데이터 설정
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2 = OAuth2PasswordBearer(tokenUrl="/user/token")

# 인증에러 처리
def unauthed():
    raise HTTPException(status_code=401,
                                detail="올바르지 않은 인증정보입니다.",
                                headers={"WWW-Authenticate" : "Bearer"}
                                )

# OAuth2가 사용할 POST 접근을 생성
@router.post("/token")
async def create_access_token(
    form_data : OAuth2PasswordRequestForm = Depends()
):
    user = service.auth_user(form_data.username, form_data.password)
    
    if not user:
        unauthed()
    
    expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data = {"sub" : user.name},
        expire = expire
    )
    return {"access_token" : access_token, "token_type" : "bearer"}

# 회원가입
@router.post("/")
def create_user(user: DB_User):
    try :
        return service.create_user(user)
    except Duplicate as E:
         raise HTTPException(status_code=401, detail=E.msg)
 
# 인가된 사용자인지 체크    
@router.get("/user_only")
def check_user(token : str = Depends(oauth2)):
   if service.check_user(token):
       return "인증된 유저로 게시판 접근이 가능합니다."
   raise HTTPException(status_code=401, detail="게시판에 접근권한이 없습니다. 등급을 확인해주세요.")

# 회원조회
@router.get("/{username}")
def find_user(username):
    return service.find_user(username)