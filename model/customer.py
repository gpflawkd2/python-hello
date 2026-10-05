from pydantic import BaseModel, EmailStr

# ======= 모델정의 =======
class Customer(BaseModel):
    name : str
    home : str
    call_num : str
    email : EmailStr

# name은 경로 파라미터로 받으므로 수정용 모델에는 포함하지 않음
class CustomerUpdate(BaseModel):
    home : str
    call_num : str
    email : EmailStr