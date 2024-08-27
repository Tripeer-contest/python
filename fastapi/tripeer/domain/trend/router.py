from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import service
from database import get_db

router = APIRouter(
    prefix="/trend",
)

@router.get("/city")
def save_city_town_trend():
    res = service.save_city_town_trend()
    return res


@router.get("/keyword")
def save_keyword_trend():
    service.save_keyword_trend()
    return "성공"

@router.get("/test")
def test():
    service.test()
    return "성공"