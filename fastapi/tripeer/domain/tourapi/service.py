import os, time, random
import requests
from models import SpotInfo, SpotDetail, SpotDescription
from domain.tourapi.func import make_model_from_detail_info
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()

TOUR_API_KEY = os.environ.get('TOUR_API_KEY')
BASE_URL = "http://apis.data.go.kr/B551011/KorService1"

def test(db: Session):
    # spot_id = 2731170
    # url = f"{BASE_URL}/detailIntro1?serviceKey={TOUR_API_KEY}&MobileOS=AND" \
    #     f"&MobileApp=tripeer&contentId={spot_id}&_type=json&contentTypeId=28"
    spot_list = db.query(SpotInfo)\
        .order_by(SpotInfo.spot_info_id.desc())\
        .all()
    print(spot_list)
    return len(spot_list)


# tourAPI 에서 관광지 데이터(spot_info, spot_detail)를 받아 db에 저장 
def get_spot_info(db: Session):
    serviceKey = TOUR_API_KEY
    pageNo = 1
    numOfRows = 53056
    url = f"{BASE_URL}/areaBasedList1?serviceKey={serviceKey}&MobileOS=AND" \
        f"&MobileApp=tripeer&pageNo={pageNo}&numOfRows={numOfRows}&_type=json"
    
    response = requests.get(url)
    data = response.json()
    spot_list = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
    print(f"가져온 장소 수: {len(spot_list)}")

    for spot in spot_list:
        # 관광공사데이터에 무결성 이슈가 있음
        try:
            # 데이터베이스에 이미 존재하는지 확인
            if db.query(SpotInfo).filter(SpotInfo.spot_info_id == spot.get('contentid')).first():
                continue
            # SpotInfo 객체 생성
            new_spot_info = SpotInfo(
                spot_info_id=spot.get('contentid'),
                city_id=spot.get('areacode'),
                town_id=spot.get('sigungucode'),
                content_type_id=spot.get('contenttypeid'),
                title=spot.get('title'),
                addr1=spot.get('addr1'),
                addr2=spot.get('addr2'),
                zipcode=spot.get('zipcode'),
                tel=spot.get('tel'),
                first_image=spot.get('firstimage'),
                first_image2=spot.get('firstimage2'),
                latitude=spot.get('mapy'),
                longitude=spot.get('mapx'),
                mlevel=spot.get('mlevel')
            )

            # SpotDetail 객체 생성
            new_spot_detail = SpotDetail(
                spot_info_id=spot.get('contentid'),
                cat1=spot.get('cat1'),
                cat2=spot.get('cat2'),
                cat3=spot.get('cat3'),
                booktour=spot.get('booktour'),
                created_time=spot.get('createdtime'),
                modified_time=spot.get('modifiedtime')
            )

            db.add(new_spot_info)
            db.add(new_spot_detail)
            db.commit()
        except:
            db.rollback()
            continue
    return data

# tourAPI 에서 관광지 설명(spot_description)를 받아 db에 저장 
def get_spot_description(db: Session):
    spot_list = db.query(SpotInfo)\
        .order_by(SpotInfo.spot_info_id.desc())\
        .all()
    # api가 하루 1000개까지 가능
    for spot in spot_list:
        # 관광공사데이터에 무결성 이슈가 있음
        try:
            spot_id = spot.spot_info_id
            # 기존에 설명이 있으면 pass
            if db.query(SpotDescription).filter(SpotDescription.spot_info_id == spot_id).first():
                continue
            url = f"{BASE_URL}/detailCommon1?serviceKey={TOUR_API_KEY}&MobileOS=AND" \
                f"&MobileApp=tripeer&overviewYN=Y&contentId={spot_id}&_type=json"
            response = requests.get(url)
            data = response.json()
            overview = data.get("response", {}).get("body", {}).get("items", {}).get("item")[0].get("overview")
            new_spot_description = SpotDescription(
                    spot_info_id=spot_id,
                    overview=overview,
                    summary=" "
                )
            db.add(new_spot_description)
            db.commit()
            count += 1
        except:
            db.rollback()
    return {"last_spot_id" :spot_id}

# tourAPI 에서 관광지 상세정보(spot_additional)를 받아 db에 저장 
def get_deteail_info(db: Session):
    spot_list = db.query(SpotInfo)\
        .order_by(SpotInfo.spot_info_id.desc())\
        .all()
    for spot in spot_list:
        time.sleep(random.uniform(0.3, 1.5))
        # 관광공사데이터에 무결성 이슈가 있음
        try:
            spot_id = spot.spot_info_id
            content_type_id = spot.content_type_id
            if spot.mlevel == 11:
                continue
            url = f"{BASE_URL}/detailIntro1?serviceKey={TOUR_API_KEY}&MobileOS=WIN" \
                f"&MobileApp=tripeer&contentId={spot_id}&_type=json&contentTypeId={content_type_id}"
            response = requests.get(url)
            data = response.json()
            detail_info_data = data.get("response", {}).get("body", {}).get("items", {}).get("item")[0]
            print(detail_info_data)
            new_detail_info = make_model_from_detail_info(spot_id, content_type_id, detail_info_data)
            db.add(new_detail_info)
            spot.mlevel = 11
            db.commit()
        except:
            db.rollback()
    return {"count":0, "last_spot_id" :spot_id}
    
# s3에 이미지 저장을 위해 tourAPI 에서 관광지 이미지(first_image1)를 받아 다운로드
def download_images(db: Session):
    spot_list = db.query(SpotInfo).order_by(SpotInfo.spot_info_id.desc()).all()

    if not spot_list:
        print("spot_list가 비어 있습니다.")
        return

    for spot in spot_list:
        print("spot.first_image:", spot.first_image) 
        if 'tong.visitkorea' in (spot.first_image or ''):
            image_url = spot.first_image
            file_name = str(spot.spot_info_id) + ".png"

            print("다운로드 시도 중, URL:", image_url)
            response = requests.get(image_url, stream=True)

            if response.status_code == 200:
                try:
                    with open(file_name, 'wb') as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    print(f"이미지가 성공적으로 {file_name}으로 저장되었습니다.")
                    spot.first_image = "https://tripeer207.s3.ap-northeast-2.amazonaws.com/spot/" + file_name
                    db.add(spot)
                except:
                    continue
            else:
                print("이미지를 다운로드하는 데 실패했습니다. 상태 코드:", response.status_code)
        else:
            print("첫 번째 이미지가 유효하지 않습니다:", spot.first_image)
    db.commit()
    return "성공"