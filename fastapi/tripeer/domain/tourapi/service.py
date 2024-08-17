import os
import json
import requests
from models import Question, SpotInfo, SpotDetail
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()

TOUR_API_KEY = os.environ.get('TOUR_API_KEY')
BASE_URL = "http://apis.data.go.kr/B551011/KorService1"

def get_question_list(db: Session):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list

# tourAPI 에서 관광지 데이터(spot_info)를 받아 db에 저장 
def get_spot_info(db: Session):
    serviceKey = TOUR_API_KEY
    pageNo = 1
    numOfRows = 5
    url = f"{BASE_URL}/areaBasedList1?serviceKey={serviceKey}&MobileOS=AND" \
        f"&MobileApp=appName&pageNo={pageNo}&numOfRows={numOfRows}&_type=json"
    res = requests.get(url)

    # data = json.loads(res.text).get("response").get("body").get("items").get("item")
    spot_list = json.loads(res.text)["response"]["body"]["items"]["item"]
    for spot in spot_list:
        try:
            # readcount 빠져있음 api에 없음 디테일 조회에서 따로 추가해야할 듯함
            new_spot_info = SpotInfo(
                spot_info_id=spot['contentid'],
                city_id=spot['areacode'],
                town_id=spot['sigungucode'],
                content_type_id = spot['contenttypeid'],
                title = spot['title'],
                addr1 = spot['addr1'],
                addr2 = spot['addr2'],
                zipcode = spot['zipcode'],
                tel = spot['tel'],
                first_image = spot['firstimage'],
                first_image2 = spot['firstimage2'],
                latitude = spot['mapy'],
                longitude = spot['mapx'],
                mlevel =  spot['mlevel'],
            )
            new_spot_detail = SpotDetail(
                spot_info_id=spot['contentid'],
                cat1=spot['cat1'],
                cat2=spot['cat2'],
                cat3=spot['cat3'],
                booktour=spot['booktour'], 
                created_time=spot['createdtime'],  
                modified_time=spot['modifiedtime'] 
            )
            db.add(new_spot_info)
            db.add(new_spot_detail)
            db.commit()
        except:
            continue
    return 