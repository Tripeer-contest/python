from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.crowing import schema
from . import service

router = APIRouter(
    prefix="/elastic",
)

# 테스트용 라우터
@router.get("")
def test(db: Session = Depends(get_db)):
    res = service.test(db)
    return res

# EL 인덱스 생성
@router.get("/index")
def create_index(indexName: str):
    res = service.create_index(indexName)
    return res

# EL 인덱스 삭제
@router.delete("/index")
def delete_index(indexName: str):
    res = service.delete_index(indexName)
    return res

# EL 데이터 전부 조회
@router.get("/all")
def test():
    res = service.search_all()
    return res

# EL 데이터 검색
@router.get("/search")
def test(keyword: str):
    res = service.search_by_keyword(keyword)
    return res

# 위도 경도 활용한 EL 데이터 검색
@router.get("/search/map")
def search_by_keyword_and_location(keyword: str, minLat: float, minLon: float, maxLat: float, maxLon: float):
    res = service.search_by_keyword_and_location(keyword, minLat, minLon, maxLat, maxLon)
    return res
