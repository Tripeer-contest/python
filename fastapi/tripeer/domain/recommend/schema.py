import datetime
from pydantic import BaseModel

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    
    class Config:
        # Pydantic v2에서는 orm_mode 대신 from_attributes를 사용합니다.
        from_attributes = True

class SpotInfoResponse(BaseModel):
    spotInfoId: int
    title: str
    contentType: str
    addr: str
    latitude: float
    longitude: float
    img: str
    isWishlist: bool
    spot: bool
    recommended_comment: str
    keyword: str
        
    class Config:
        from_attributes = True
