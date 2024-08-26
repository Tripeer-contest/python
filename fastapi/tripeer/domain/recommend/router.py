from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
import jwt

from database import get_db
from . import service

router = APIRouter(
    prefix="/recommend",
)


@router.get("/summary")
def make_summary(db: Session = Depends(get_db)):
    res = service.make_summary(db)
    return res

@router.get("/keyword")
def make_summary(db: Session = Depends(get_db)):
    res = service.make_spot_keyword(db)
    return res

@router.get("/check")
def check_keywords(db: Session = Depends(get_db)):
    res = service.ckeck_keywords(db)
    return res

@router.get("/test")
def test(db: Session = Depends(get_db)):
    res = service.test()
    return res

@router.get("/home")
def get_home_recommend(request: Request, cityId: int, townId: int, contentType, db: Session = Depends(get_db)):
    token = request.headers.get("Authorization").split()[1]
    payload = jwt.decode(token, options={"verify_signature": False})
    user_id = payload.get('userId')
    res = service.get_home_recommend(user_id, cityId, townId, contentType, db)
    return res

@router.get("/")
def get_custom_recommend(db: Session = Depends(get_db)):
    res = service.get_custom_recommend(6, db)
    return res

@router.get("/mongo")
def save_mongo(db: Session = Depends(get_db)):
    res = service.save_mongo(db)
    return res
