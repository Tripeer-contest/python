import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    
    class Config:
        orm_mode = True

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
    keyword:str