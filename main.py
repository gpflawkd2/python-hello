# 필수 프레임워크
from fastapi import FastAPI, Body, Header
import uvicorn

# 파일 import
from web import customer
from web import market

# app 실행
app = FastAPI()

# web에 작성된 router 연결
app.include_router(customer.router)
app.include_router(market.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
    
# 콘솔창 통신 테스트
# http GET localhost:8000/customer/
# http GET localhost:8000/market/
# http GET localhost:8000/market/피자나라