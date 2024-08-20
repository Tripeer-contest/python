from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

#  --------------     test      --------------------
class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String(100), nullable=False,)
    content = Column(String(300), nullable=False)
    create_date = Column(DateTime, nullable=False)



#  --------------     tourApi      --------------------
class SpotInfo(Base):
    __tablename__ = "spot_info"
    spot_info_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    city_id = Column(Integer, nullable=False)
    town_id = Column(Integer, nullable=False)
    content_type_id = Column(Integer, nullable=False)
    title = Column(String(100), nullable=False)
    addr1 = Column(String(100), nullable=True)
    addr2 = Column(String(50), nullable=True)
    zipcode = Column(String(50), nullable=True)
    tel = Column(String(50), nullable=True)
    first_image = Column(String(200), nullable=True)
    first_image2 = Column(String(200), nullable=True)
    readcount = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    mlevel = Column(String(2), nullable=True)

class SpotDetail(Base):
    __tablename__ = "spot_detail"
    spot_info_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cat1 = Column(String(3), nullable=True)
    cat2 = Column(String(5), nullable=True)
    cat3 = Column(String(9), nullable=True)
    created_time = Column(String(14), nullable=True)
    modified_time = Column(String(14), nullable=True)
    booktour = Column(String(5), nullable=True)


class SpotDescription(Base):
    __tablename__ = 'spot_description'
    spot_info_id = Column(Integer, primary_key=True, autoincrement=True)
    overview = Column(String(10000), nullable=False)
    summary = Column(String(100), nullable=False)