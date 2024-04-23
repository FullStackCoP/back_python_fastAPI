import datetime
from typing import List
from pydantic import BaseModel

class Restaurant(BaseModel):
    id: str
    name: str
    thumUrl: str
    tag: List[str]
    priceRage: str
    ratings: float
    ratingsCount: int
    deliveryTime: datetime.time 
    deliveryFee: int

class RankingItem(BaseModel):
    rank: int
    score: float
    reviewer: str

class PaginationMeta(BaseModel):
    count: int
    hasMore: bool

