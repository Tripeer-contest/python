from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import pytrends
import pandas as pd

from database import get_db

router = APIRouter(
    prefix="/trend",
)

# 검색어 리스트로 검색량 확인 (매달 핫한 도시 찾기에 활용)
@router.get("/test")
def test():
    keyword_list = ['서울여행', '대구여행', '강원도여행', '부산여행'] #한번에 5개 키워드까지
    pytrends.build_payload(keyword_list, cat=0, timeframe='2023-07-01 2023-12-03', geo='KR')
    data = pytrends.interest_over_time()
    data = data.reset_index()
    print(data)   



# 검색어 리스트로 관련 검색어 확인 
@router.get("/test2")
def test2():
    # 검색할 키워드 목록
    kw_list = ['바다', '스키', '계곡']

    # Google Trends 데이터 요청 (2024-07-01 ~ 2024-08-03, 대한민국)
    pytrends.build_payload(kw_list, timeframe='2024-07-01 2024-08-03', geo='KR')

    # 관련 검색어 데이터 가져오기
    df = pytrends.related_queries()

    # 상승하는 검색어만 추출하여 하나의 데이터프레임으로 결합
    result_rising = pd.concat([df[kw]['rising'] for kw in kw_list], axis=0)

    # value 기준으로 내림차순 정렬하고 인덱스 재설정
    result_rising = result_rising.sort_values(by='value', ascending=False).reset_index(drop=True)

    # 결과 출력
    print(result_rising)



    # 구글 트랜드 + 내가 찾은 우리 키워드 조합해서 인기 키워드 만들기
    # 사건, 사고등 부적절한 키워드 들어가 있는지 필터링하기