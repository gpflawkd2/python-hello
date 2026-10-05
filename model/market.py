from pydantic import BaseModel, EmailStr

# ======= 모델정의 =======
class Market(BaseModel):
    name : str
    location : str
    menu : dict[str, int]
    call_num : str