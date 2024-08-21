from models import SpotInfo, SpotDetail, SpotDescription
from sqlalchemy.orm import Session
from konlpy.tag import Okt
from domain.recommend.variable import stop_list, city_town_list, cat3, union_values
from fastapi import Depends
from database import get_mongo
from pymongo.collection import Collection
import os

from collections import Counter

okt = Okt()

# spot 설명에서 키워드 뽑아내는 함수
def make_summary(db: Session):
    spot_list = db.query(SpotDescription)\
        .order_by(SpotDescription.spot_info_id.desc())\
        .all()
    for spot in spot_list:
        spot_detail = db.query(SpotDetail)\
        .filter(SpotDetail.spot_info_id==spot.spot_info_id)\
        .first()
        if spot.summary.strip():
            continue
        description = spot.overview
        nouns = okt.nouns(description)  # 텍스트에서 명사 추출
        result = [] 
        # 의미 없는 단어 삭제
        for w in nouns: 
            if w not in stop_list: 
                result.append(w) 
        noun_freq = Counter(result)  # 명사의 빈도 수 계산
        top_nouns = [noun for noun, count in noun_freq.most_common(10)]  # 빈도 수 상위 5개 명사 선택
        spot_cate = cat3[spot_detail.cat3] if spot_detail else ""
        top_nouns_string = (spot_cate + " " + " ".join(top_nouns)).strip()
        spot.summary = top_nouns_string
        db.add(spot)
    db.commit()
    return "성공"

# spot 설명에서 내가 뽑은 키워드 뽑아내는 함수 
# (위에 함수로 통계를 내고 실재 여행과 관련있는 키워드를 필터링하여 그 키워드가 있는지 검사)
def make_spot_keyword(db: Session):
    spot_list = db.query(SpotDescription)\
        .order_by(SpotDescription.spot_info_id.desc())\
        .all()
    for spot in spot_list:
        spot_detail = db.query(SpotDetail)\
        .filter(SpotDetail.spot_info_id==spot.spot_info_id)\
        .first()
        description = spot.overview
        summary = set()
        for keyword in union_values:
            if keyword in description:
                summary.add(keyword)
        spot_cate = cat3[spot_detail.cat3] if spot_detail else ""
        spot.summary = (spot_cate + " " + " ".join(summary)).strip()
        db.add(spot)
    db.commit()
    return "성공"


def make_recommend(db: Session, collection: Collection = Depends(get_mongo)):
    for city, town in city_town_list:
        spot_list = db.query(SpotInfo)\
        .filter(SpotInfo.city_id==city)\
        .filter(SpotInfo.town_id==town)\
        .all()
        
    return

def ckeck_keywords(db: Session):
    spot_detail = db.query(SpotDescription).all()
    lst = []
    for spot in spot_detail:
        lst.extend(spot.summary.split())
    freq = Counter(lst)
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    return sorted_freq

def test():
    return len(union_values)