from fastapi import FastAPI, Body, Header
import uvicorn

app = FastAPI()

# url에 데이터를 넣어서 접근하는 방법
# http -v GET localhost:8000/hrpark
"""
@app.get("/{who}")
def http_get(who):
    return who
"""

# query parameter를 이용해서 접근하는 방법
# http -v GET localhost:8000/\?who=hrpark
# http -v GET localhost:8000/ who==hrpark
"""
@app.get("/")
def http_get(who):
    return who
"""

# header에 데이터 전송 -> :(콜론) 사용
# http -v POST localhost:8000/ who:hrpark
# body에 데이터 전송 -> =(등호) 사용
# http -v POST localhost:8000/ who=hrpark
@app.post("/")
def http_post(who = Body(...)):
    return who

@app.put("/")
def http_put(who = Header(...)):
    return who

@app.patch("/")
def http_patch():
    return "patch으로 접근했습니다."

@app.delete("/")
def http_delete():
    return "delete로 접근했습니다."

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)