from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.recommend import service

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