from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from domain.tourapi import service
from database import get_db

scheduler = BackgroundScheduler()


def get_spot_info_description():
    db: Session = next(get_db())
    service.get_spot_info(db)
    service.get_spot_description(db)


# 함수에 파라미터가 없으면 args를 안넣으면 됩니다.
scheduler.add_job(get_spot_info_description, 'cron', hour=2, minute=0)
# scheduler.add_job(function_1, "interval", seconds=5, kwargs={"a": 1, "b": 2, "c": 3})
 