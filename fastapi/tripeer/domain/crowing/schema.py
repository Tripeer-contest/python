import datetime
from pydantic import BaseModel

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    
    class Config:
        from_attributes = True
