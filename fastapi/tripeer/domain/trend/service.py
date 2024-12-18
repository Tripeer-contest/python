import urllib.parse
from datetime import datetime, timezone, timedelta
import requests
import pandas as pd
from pymongo import ASCENDING

from database import get_mongo
from .variable import trend_dict, trend_dict2
from domain.recommend.variable import union_values, test_list, keywords_list

mongodb = get_mongo()
ct_collection = mongodb['trending_city_town']

keyword_collection = mongodb['trending_keyword']
# 검색어 리스트로 검색량 확인 (매달 핫한 도시 찾기에 활용)
def save_city_town_trend():
    now = datetime.now()

    # 한국 시간대 (UTC+9) 생성
    kst = timezone(timedelta(hours=9))

    # 한국 시간으로 변환
    now_kst = now.astimezone(kst)
    # Unix 시간 스탬프로 변환 (밀리초 단위)
    unix_timestamp = now_kst.timestamp() * 1000
    for (city_id, town_id) in trend_dict:
        keyword = trend_dict2.get((city_id, town_id))
        url = f"https://ma-pia.net/analysis/api/naver/month_search_ratio.php?keyword={keyword}가볼만한곳&time={unix_timestamp}"
        response = requests.get(url)
        data = response.json()
        pc_data = data.get('result').get('Pc')
        mobile_data = data.get('result').get('Mobile')
        today_avg = int(pc_data[-1].get('searchCnt')) + int(mobile_data[-1].get('searchCnt'))
        pc_avg = sum(map(lambda x: int(x.get('searchCnt')),pc_data)) // len(pc_data)
        mobile_avg = sum(map(lambda x: int(x.get('searchCnt')),mobile_data)) // len(mobile_data)
        total_avg = pc_avg + mobile_avg
        query = {"city_id": city_id, "town_id": town_id}
        document = {"city_id": city_id, "town_id": town_id, "name":keyword, "total_avg": total_avg, "today_avg" :today_avg }
        ct_collection.update_one(query, {"$set": document})
    return "성공"


# 구글 트랜드 + 내가 찾은 우리 키워드 조합해서 인기 키워드 만들기
def save_keyword_trend():
    now = datetime.now()

    # 한국 시간대 (UTC+9) 생성
    kst = timezone(timedelta(hours=9))

    # 한국 시간으로 변환
    now_kst = now.astimezone(kst)
    # Unix 시간 스탬프로 변환 (밀리초 단위)
    unix_timestamp = now_kst.timestamp() * 1000
    keyword_set = set(keywords_list)
    len(keyword_set)
    for keyword in keyword_set:
        url = f"https://ma-pia.net/analysis/api/naver/month_search_ratio.php?keyword={keyword}여행&time={unix_timestamp}"
        response = requests.get(url)
        data = response.json()
        mobile_data = data.get('result').get('Mobile')
        if mobile_data:
            mobile_sum = sum(map(lambda x: int(x.get('searchCnt')),mobile_data))
            today_avg = mobile_data[-1].get('searchCnt')
            total_avg = mobile_sum // 12
        else:
            total_avg = 0
            today_avg = 0
        query = {"keyword": keyword}
        document = { "keyword":keyword, "total_avg": total_avg, "today_avg" :today_avg }
        # keyword_collection.update_one(query, {"$set": document})
        keyword_collection.insert_one(document)
    return "성공"

def test():
    docs = keyword_collection.find({'total_avg': {'$ne': 0}})
    docs_list = list(docs) 
    keyword_list = [doc.get('keyword') for doc in docs_list]
    print(keyword_list)
    return
