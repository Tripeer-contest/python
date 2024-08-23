from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import service
from database import get_db

router = APIRouter(
    prefix="/trend",
)

@router.get("/test")
def test():
    res = service.test()
    return res


# 검색어 리스트로 관련 검색어 확인 
@router.get("/test2")
def test2():
    service.test2()
    return "성공"