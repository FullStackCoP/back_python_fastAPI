from typing import Optional
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/auth/login")
def read_login(request: Request):
    print(request.headers)
    print(request.body)
    return {"accessToken": "jadskjflwkejrkljwelrkjlwkjlrkjqwlke" }

@app.post("/auth/token")
def read_login(request: Request):
    print(request.headers)
    print(request.body)
    return {"refreshToken": "15i4j15jkljasdfjiojewrkjl;qwer98112312" }