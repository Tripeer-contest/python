from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.crowing import schema
from models import Question

router = APIRouter(
    prefix="/py/test",
)


@router.get("/list", response_model=list[schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list
