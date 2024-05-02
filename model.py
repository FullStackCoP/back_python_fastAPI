import datetime
from typing import List
from pydantic import BaseModel

class Restaurant(BaseModel):
    id: str
    name: str
    thumbUrl: str
    tags: List[str]
    priceRange: str
    ratings: float
    ratingsCount: int
    deliveryTime: int
    deliveryFee: int

class RankingItem(BaseModel):
    rank: int
    score: float
    reviewer: str

class PaginationMeta(BaseModel):
    count: int
    hasMore: bool

