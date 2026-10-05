from pydantic import BaseModel, EmailStr

# ======= 모델정의 =======
class Customer(BaseModel):
    name : str
    home : str
    call_num : str
    email : EmailStr