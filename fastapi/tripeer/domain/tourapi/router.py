from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from . import schema, service
# from domain.tourapi import schema

router = APIRouter(
    prefix="/tour",
)


@router.get("/list", response_model=list[schema.Question])
async def question_list(db: Session = Depends(get_db)):
    _question_list = service.get_question_list()
    return _question_list

@router.get("/spot/info")
async def save_spot_info(db: Session = Depends(get_db)):
    res = service.get_spot_info(db)
    return res