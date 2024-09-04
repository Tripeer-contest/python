from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
import jwt

from database import get_db
from . import service

router = APIRouter(
    prefix="/recommend",
)

# recommend 도메인 테스트 함수
@router.get("/test")
def test(userId: int, cityId: int, townId: int, keyword: str, db: Session = Depends(get_db)):
    res = service.get_more_recommend(userId, cityId, townId, keyword, db)
    return res

# spot 설명에서 키워드 뽑아내는 함수
@router.get("/summary")
def make_summary(db: Session = Depends(get_db)):
    res = service.make_summary(db)
    return res

# spot 설명에서 내가 뽑은 키워드 뽑아내는 summary에 저장하는 함수 
# (위에 함수로 통계를 내고 여행과 관련있는 키워드를 필터링하여 그 키워드가 있는지 검사)
@router.get("/keyword")
def make_summary(db: Session = Depends(get_db)):
    res = service.make_spot_keyword(db)
    return res

# 키워드 저장후 각 키워드 관련 광관지가 얼마나 있는지 통계를 내줌
@router.get("/check")
def check_keywords(db: Session = Depends(get_db)):
    res = service.ckeck_keywords(db)
    return res

# 메인 홈화면 추천로직 기존 방식 + contentType에 따른 추가 추천
@router.get("/home")
def get_home_recommend(request: Request, cityId: int, townId: int, contentType: int, db: Session = Depends(get_db)):
    token = request.headers.get("Authorization").split()[1]
    payload = jwt.decode(token, options={"verify_signature": False})
    user_id = payload.get('userId')
    res = service.get_home_recommend(user_id, cityId, townId, contentType, db)
    return res

# 추천 더보기를 위한 api
@router.get("/more")
def get_more_recommend(request: Request, cityId: int, townId: int, keyword: int, db: Session = Depends(get_db)):
    token = request.headers.get("Authorization").split()[1]
    payload = jwt.decode(token, options={"verify_signature": False})
    user_id = payload.get('userId')
    res = service.get_more_recommend(user_id, cityId, townId, keyword, db)
    return res

@router.get("/")
def get_custom_recommend(db: Session = Depends(get_db)):
    res = service.get_custom_recommend(6,1,1, db)
    return res

# 키워드 추출후 빠른 조회를 위해 모든 city, town, keywor에 대한 추천 리스트를 미리 만들어 몽고DB에 저장
@router.get("/mongo")
def save_mongo(db: Session = Depends(get_db)):
    res = service.save_mongo(db)
    return res

