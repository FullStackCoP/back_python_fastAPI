from datetime import datetime
import json
import jwt
from typing import Optional
from fastapi import FastAPI, HTTPException, Request, Path
from pydantic import BaseModel

from model import RankingItem, Restaurant

app = FastAPI()

class UserLogin(BaseModel):
    username: str
    password: str

class UserToken(BaseModel):
    access_token: str
    token_type: str

SECRET_KEY = "my-secret-key"

def authenticate_user(username: str, password: str):
    # 사용자 정보를 데이터베이스에서 가져옵니다.
    user = {"username": "user", password: "password"}
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not password == user["password"]:
        raise HTTPException(status_code=401, detail="Invalid password")
    print(f"User {user} authenticated")
    return user

def generate_token(user: UserLogin):
    print(f"Generating token for {user}")
    token_data = {
        "username": user["username"],
        "role": user["password"],
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm="HS256")
    return token

def read_login(request: Request):
    print(request.headers)
    print(request.body)
    return {"accessToken": "jadskjflwkejrkljwelrkjlwkjlrkjqwlke", "refreshToken": "15i4j15jkljasdfjiojewrkjl;qwer98112312" }

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/auth/login")
async def login(request: Request):
    body = await request.body()
    data = json.loads(body)
    print(data)
    name, pw = data["username"], data["password"]
    print(name, pw)
    user = authenticate_user(name, pw)
    print(user)
    token = generate_token(user)
    return UserToken(access_token=token, token_type="bearer")



@app.post("/auth/token")
def read_token(request: Request):
    print(request.headers)
    print(request.body)
    return {"refreshToken": "15i4j15jkljasdfjiojewrkjl;qwer98112312" }

@app.get("/restaurant")
def get_all_restaurant():
    # 레스토랑 정보를 데이터베이스에서 가져옵니다.
    restaurants = [
        Restaurant(id="1", name="My restaurant", thumbUrl="/1", tags=['떡볶이', '치즈', '매운맛'], priceRange="sale", ratings=0.0, ratingsCount=0, deliveryTime=10, deliveryFee=0),
        Restaurant(id="1", name="My restaurant", thumbUrl="/2", tags=['ttttt'], priceRange="sale", ratings=0.0, ratingsCount=0, deliveryTime=20, deliveryFee=0),
        Restaurant(id="1", name="My restaurant", thumbUrl="/3", tags=['ttttt'], priceRange="sale", ratings=0.0, ratingsCount=0, deliveryTime=30, deliveryFee=0),
        Restaurant(id="1", name="My restaurant", thumbUrl="/4", tags=['ttttt'], priceRange="sale", ratings=0.0, ratingsCount=0, deliveryTime=40, deliveryFee=0),
        Restaurant(id="1", name="My restaurant", thumbUrl="/6", tags=['ttttt'], priceRange="sale", ratings=0.0, ratingsCount=0, deliveryTime=50, deliveryFee=0),

    ]
    # 총 데이터 개수 계산
    total_count = len(restaurants)

    # 더 많은 데이터가 있는지 여부 확인
    has_more = total_count > 20  # 예: 20개 이상만 'hasNext'를 True로 설정

    # JSON 형식으로 응답 데이터 구성
    response_data = {
        "meta": {
            "count": total_count,
            "hasMore": has_more
        },
        "data": restaurants
    }
    return response_data

@app.get("/restaurant/{rid}")
def get_restaurant(rid: int = Path(...)):
    # 레스토랑 정보를 데이터베이스에서 가져옵니다.
    restaurant = Restaurant(id="1", name="My restaurant", thumbUrl="/thumNail", tags=['ttttt'], priceRange="sale", ratings=0.0, ratingsCount=0, deliveryTime=30, deliveryFee=0)
    return restaurant

@app.get("/restaurant/{rid}/ranking")
def get_restaurant_ranking(rid: int = Path(...)):
    # 레스토랑 리뷰 목록을 데이터베이스에서 가져옵니다.
    ranking_items = [
        RankingItem(rank=1, score=4.5, reviewer="John Doe"),
        RankingItem(rank=2, score=4.2, reviewer="Jane Smith"),
    ]
    return ranking_items
