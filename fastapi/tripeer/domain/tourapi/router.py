from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from . import  service
# from domain.tourapi import schema

router = APIRouter(
    prefix="/tour",
)

# tour 도메인 테스트
@router.get("/test")
async def save_spot_info(db: Session = Depends(get_db)):
    res = service.test(db)
    return res

# tourAPI 에서 관광지 데이터(spot_info, spot_detail)를 받아 db에 저장 
@router.get("/spot/info")
async def save_spot_info(db: Session = Depends(get_db)):
    res = service.get_spot_info(db)
    return res

# tourAPI 에서 관광지 설명(spot_description)를 받아 db에 저장 
@router.get("/spot/desc")
async def save_spot_description(db: Session = Depends(get_db)):
    res = service.get_spot_description(db)
    return res

# tourAPI 에서 관광지 상세정보(spot_additional)를 받아 db에 저장
@router.get("/spot/additional")
async def save_spot_description(db: Session = Depends(get_db)):
    res = service.get_deteail_info(db)
    return res

# s3에 이미지 저장을 위해 tourAPI 에서 관광지 이미지(first_image1)를 받아 다운로드
@router.get("/spot/image")
async def download_images(db: Session = Depends(get_db)):
    res = service.download_images(db)
    return res