import os
from collections import Counter
import torch
from fastapi import Depends
from database import get_mongo, get_db
from pymongo import ASCENDING
from pymongo.collection import Collection
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from konlpy.tag import Okt
from sentence_transformers import SentenceTransformer, util

from models import SpotInfo, SpotDetail, SpotDescription, User, Wishlist, PlanBucket
from .variable import *
from .schema import SpotInfoResponse

mongodb = get_mongo()
collection = mongodb['recommend2']
collection.create_index([('city_id', ASCENDING), ('town_id', ASCENDING), ('keyword', ASCENDING)], unique=True)

spot_collection = mongodb['spot_collection']
spot_collection.create_index([('spot_info_id', ASCENDING)], unique=True)


model = SentenceTransformer("snunlp/KR-SBERT-V40K-klueNLI-augSTS")
okt = Okt()
hot_wish_keywords = []
hot_bucket_keywords = []

# 현재 전체 즐겨찾기 db에서 가장 많이 등장한 키워드 추출(
def make_hot_keywords(db: Session):
    global hot_wish_keywords
    global hot_bucket_keywords
    wish_list = db.query(Wishlist).all()
    spot_ids = list(map(lambda x: x.spot_info_id, wish_list))
    spot_descriptions = db.query(SpotDescription).filter(SpotDescription.spot_info_id.in_(spot_ids)).all()
    spot_keywords = []
    for description in spot_descriptions:
        spot_keywords.extend(description.summary.split())
    count_dict = Counter(spot_keywords)
    hot_wishlist = count_dict.most_common(10)
    hot_wish_keywords = [keyword for keyword, _ in hot_wishlist]

    bucket_list = db.query(PlanBucket).all()
    spot_ids = list(map(lambda x: x.spot_info_id, wish_list))
    spot_descriptions = db.query(SpotDescription).filter(SpotDescription.spot_info_id.in_(spot_ids)).all()
    spot_keywords = []
    for description in spot_descriptions:
        spot_keywords.extend(description.summary.split())
    count_dict = Counter(spot_keywords)
    hot_bucketlist = count_dict.most_common(10)
    hot_bucket_keywords = [keyword for keyword, _ in hot_bucketlist]
    return 

# 서버가 실행될 때 1번 돌림
def init_hot_keywords():
    db = next(get_db())
    make_hot_keywords(db)
    db.close()

# 서버 시작 시 호출
init_hot_keywords()

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

# spot 설명에서 내가 뽑은 키워드 뽑아내는 summary에 저장하는 함수 
# (위에 함수로 통계를 내고 여행과 관련있는 키워드를 필터링하여 그 키워드가 있는지 검사)
def make_spot_keyword(db: Session):
    spot_list = db.query(SpotDescription)\
        .order_by(SpotDescription.spot_info_id.desc())\
        .all()
    count = 0
    for spot in spot_list:
        count += 1
        print(count)
        spot_detail = db.query(SpotDetail)\
        .filter(SpotDetail.spot_info_id==spot.spot_info_id)\
        .first()
        description = spot.overview
        summary = set()
        for keyword in union_values:
            if keyword in description:
                summary.add(keyword)
        # tourAPI데이터 무결성 문제
        try:
            spot_cate = cat2[spot_detail.cat2] if spot_detail else ""
            if spot_cate == '음식' or spot_cate == '숙박':
                spot_cate = cat3[spot_detail.cat3]
        except:
            spot_cate= ""
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

# 키워드 저장후 각 키워드 관련 광관지가 얼마나 있는지 통계를 내줌
def ckeck_keywords(db: Session):
    spot_detail = db.query(SpotDescription).all()
    lst = []
    for spot in spot_detail:
        lst.extend(spot.summary.split())
    freq = Counter(lst)
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    return sorted_freq

# 내가 만든 키워드로 추천해주는 로직(tripeer 1.0에 추천 로직)
def get_custom_recommend(user_id, city_id, town_id ,db: Session):
    user = db.query(User).filter(User.user_id == user_id).first()
    user_styles = [style for style in (user.style1, user.style2) if style]
    keywordBlackList = user_styles

    wish_list = db.query(Wishlist).filter(Wishlist.user_id == user_id).all()
    wish_spot_ids = list(map(lambda x : x.spot_info_id, wish_list))
    spot_descriptions = db.query(SpotDescription).filter(SpotDescription.spot_info_id.in_(wish_spot_ids)).all()
    spot_keywords = []
    for el in spot_descriptions: 
        spot_keywords.extend(el.summary.split())
    wishlist_top_two = [item for item, _ in Counter(spot_keywords).most_common(6) if item not in keywordBlackList][:2]
    keywordBlackList += wishlist_top_two
    
    hot_wish_keywords_two = [item for item in hot_wish_keywords if item not in keywordBlackList][:2]
    keywordBlackList += hot_wish_keywords_two

    hot_bucket_keywords_two = [item for item in hot_bucket_keywords if item not in keywordBlackList][:2]
    keywordBlackList += hot_bucket_keywords_two

    res = {
        'wishlist1': [],
        'wishlist2': [],
        'style1': [],
        'style2': [],
        'hotwish1': [],
        'hotwish2': [],
        'hotbucket1': [],
        'hotbucket2': []
    }

    keyword_dict = {
        'wishlist1': (wishlist_top_two[0] if len(wishlist_top_two) > 0 else ""),
        'wishlist2': (wishlist_top_two[1] if len(wishlist_top_two) > 1 else ""),
        'style1': user_styles[0],
        'style2': (user_styles[1] if len(user_styles) > 1 else ""),
        'hotwish1': hot_wish_keywords_two[0],
        'hotwish2': hot_wish_keywords_two[1],
        'hotbucket1': hot_bucket_keywords_two[0],
        'hotbucket2': hot_bucket_keywords_two[1]
    }
    for el in keyword_dict:
        keyword = keyword_dict.get(el)
        if not keyword:
            continue
        print(el, keyword)
        document = collection.find_one({'city_id': city_id, 'town_id': town_id, 'keyword': keyword}, {'_id': 0, 'value': 1})
        spot_id_list = document['value']
        spot_list = spot_list = db.query(SpotInfo)\
                    .filter(SpotInfo.spot_info_id.in_(spot_id_list))\
                    .all()
        for spot in spot_list:
            spot_info_res = SpotInfoResponse(
                    spotInfoId= spot.spot_info_id,
                    title= spot.title,
                    contentType= str(spot.content_type_id),
                    addr= spot.addr1,
                    latitude= spot.latitude,
                    longitude= spot.longitude,
                    img= spot.first_image,
                    isWishlist= spot.spot_info_id in wish_spot_ids,
                    spot=False,
                    recommended_comment= el,
                    keyword=keyword
            )
            res[el].append(spot_info_res)
    result = {
        "res": res,
        "keyword_dict": keyword_dict,
    }
    return result

# 숙소 추천 로직(커스텀 키워드 추가 필요)
# 숙소 데이터 부족한 것 같음
def get_lodging_recommend(user_id, city_id, town_id ,db: Session):
    wish_list = db.query(Wishlist).filter(Wishlist.user_id == user_id).all()
    wish_spot_ids = list(map(lambda x : x.spot_info_id, wish_list))
    keyword_dict = {
        'basic1': '관광호텔',
        'basic2': '콘도미니엄',
        'basic3': '유스호스텔',
        'basic4': '펜션',
        'basic5': '민박',
        'basic6': '모텔',
        'basic7': '게스트하우스',
        'basic8': '홈스테이',
        'basic9': '서비스드레지던스',
        'basic10':'한옥',
    }
    response = {
        'basic1': [],
        'basic2': [],
        'basic3': [],
        'basic4': [],
        'basic5': [],
        'basic6': [],
        'basic7': [],
        'basic8': [],
        'basic9': [],
        'basic10': [],
    }

    if city_id == -1 and town_id == -1:
        res = db.query(SpotInfo, SpotDetail)\
            .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
            .filter(SpotInfo.content_type_id == 32).all()
    elif city_id != -1 and town_id == -1:
        res = db.query(SpotInfo, SpotDetail)\
            .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
            .filter(SpotInfo.city_id == city_id)\
            .filter(SpotInfo.content_type_id == 32).all()
    elif city_id != -1 and town_id != -1:
        res = db.query(SpotInfo, SpotDetail)\
            .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
            .filter(SpotInfo.city_id == city_id)\
            .filter(SpotInfo.town_id == town_id)\
            .filter(SpotInfo.content_type_id == 32).all()
    for (spot, spot_detail) in res:
        if cat3[spot_detail.cat3] not in lodging_reversed_dict:
            continue
        spot_info_res = SpotInfoResponse(
                spotInfoId= spot.spot_info_id,
                title= spot.title,
                contentType= str(spot.content_type_id),
                addr= spot.addr1,
                latitude= spot.latitude,
                longitude= spot.longitude,
                img= spot.first_image,
                isWishlist= spot.spot_info_id in wish_spot_ids,
                spot=False,
                recommended_comment= lodging_reversed_dict[cat3[spot_detail.cat3]],
                keyword=cat3[spot_detail.cat3]
            )
        response.get(lodging_reversed_dict[cat3[spot_detail.cat3]]).append(spot_info_res)
    return response

# 음식 추천 로직(커스텀 키워드 추가 필요)
def get_food_recommend(user_id, city_id, town_id ,db: Session):
    wish_list = db.query(Wishlist).filter(Wishlist.user_id == user_id).all()
    wish_spot_ids = list(map(lambda x : x.spot_info_id, wish_list))
    keyword_dict = {
        'basic1': '한식',
        'basic2': '서양식',
        'basic3': '일식',
        'basic4': '중식',
        'basic5': '이색음식점',
        'basic6': '카페/전통찻집',
        'basic7': '클럽',
    }
    response = {
        'basic1': [],
        'basic2': [],
        'basic3': [],
        'basic4': [],
        'basic5': [],
        'basic6': [],
        'basic7': [],
    }

    if city_id == -1 and town_id == -1:
        res = db.query(SpotInfo, SpotDetail)\
            .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
            .filter(SpotInfo.content_type_id == 39).all()
    elif city_id != -1 and town_id == -1:
        res = db.query(SpotInfo, SpotDetail)\
            .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
            .filter(SpotInfo.city_id == city_id)\
            .filter(SpotInfo.content_type_id == 39).all()
    elif city_id != -1 and town_id != -1:
        res = db.query(SpotInfo, SpotDetail)\
            .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
            .filter(SpotInfo.city_id == city_id)\
            .filter(SpotInfo.town_id == town_id)\
            .filter(SpotInfo.content_type_id == 39).all()
    for (spot, spot_detail) in res:
        if cat3[spot_detail.cat3] not in food_reversed_dict:
            continue
        spot_info_res = SpotInfoResponse(
                spotInfoId= spot.spot_info_id,
                title= spot.title,
                contentType= str(spot.content_type_id),
                addr= spot.addr1,
                latitude= spot.latitude,
                longitude= spot.longitude,
                img= spot.first_image,
                isWishlist= spot.spot_info_id in wish_spot_ids,
                spot=False,
                recommended_comment= food_reversed_dict[cat3[spot_detail.cat3]],
                keyword=cat3[spot_detail.cat3]
            )
        response.get(food_reversed_dict[cat3[spot_detail.cat3]]).append(spot_info_res)
    return response


# 각 시도, 타운, 키워드 기준 추천 리스트를 미리만들어 몽고db에 저장
# 갯수로 저장하는 것이 아닌 정확도를 기준으로 커트해야함
# 반복되는 부분 함수로 따로 빼기
def save_mongo_keyword_sim(db: Session):
    for city_id, town_id in city_town_list:
        res = db.query(SpotInfo, SpotDescription)\
            .join(SpotDescription, SpotInfo.spot_info_id == SpotDescription.spot_info_id)\
            .filter(SpotInfo.city_id == city_id)\
            .filter(SpotInfo.town_id == town_id)\
            .all()
        
        spot_summaries = [SpotDescription.summary for (_, SpotDescription) in res]  # SpotDetail의 summary 리스트
        if not spot_summaries:
            continue  # summary가 없으면 다음 반복으로 넘어감
        summary_embeddings = model.encode(spot_summaries, convert_to_tensor=True)  # 임베딩
        doc_list = []
        keywords_set = set(union_values)
        for keyword in keywords_set:
            keyword_embedding = model.encode(keyword, convert_to_tensor=True)  # 키워드 임베딩

            cosine_scores = util.pytorch_cos_sim(keyword_embedding, summary_embeddings)[0]  # 코사인 유사도 계산

            top_results = torch.topk(cosine_scores, k = 20)  # 코사인 유사도 상위 20개 인덱스 및 값

            top_spot_list = [res[idx][0].spot_info_id for idx in top_results[1]]  # 상위 20개의 spot_list 추출
            document = {
                'city_id': int(city_id),
                'town_id': int(town_id),
                'keyword': keyword,
                'value': top_spot_list
                }
            doc_list.append(document)
        collection.insert_many(doc_list)
    for city_id in city_id_list:
        res = db.query(SpotInfo, SpotDescription)\
            .join(SpotDescription, SpotInfo.spot_info_id == SpotDescription.spot_info_id)\
            .filter(SpotInfo.city_id == city_id)\
            .all()
        spot_summaries = [SpotDescription.summary for (_, SpotDescription) in res]  # SpotDetail의 summary 리스트
        if not spot_summaries:
            continue  # summary가 없으면 다음 반복으로 넘어감
        summary_embeddings = model.encode(spot_summaries, convert_to_tensor=True)  # 임베딩
        doc_list = []
        keywords_set = set(union_values)
        for keyword in keywords_set:
            keyword_embedding = model.encode(keyword, convert_to_tensor=True)  # 키워드 임베딩

            cosine_scores = util.pytorch_cos_sim(keyword_embedding, summary_embeddings)[0]  # 코사인 유사도 계산

            top_results = torch.topk(cosine_scores, k = 20)  # 코사인 유사도 상위 20개 인덱스 및 값

            top_spot_list = [res[idx][0].spot_info_id for idx in top_results[1]]  # 상위 20개의 spot_list 추출
            document = {
                'city_id': int(city_id),
                'town_id': -1,
                'keyword': keyword,
                'value': top_spot_list
                }
            doc_list.append(document)
        collection.insert_many(doc_list)
    res = db.query(SpotInfo, SpotDescription)\
        .join(SpotDescription, SpotInfo.spot_info_id == SpotDescription.spot_info_id)\
        .all()
    spot_summaries = [SpotDescription.summary for (_, SpotDescription) in res]  # SpotDetail의 summary 리스트
    summary_embeddings = model.encode(spot_summaries, convert_to_tensor=True)  # 임베딩
    doc_list = []
    keywords_set = set(union_values)
    for keyword in keywords_set:
        keyword_embedding = model.encode(keyword, convert_to_tensor=True)  # 키워드 임베딩

        cosine_scores = util.pytorch_cos_sim(keyword_embedding, summary_embeddings)[0]  # 코사인 유사도 계산

        top_results = torch.topk(cosine_scores, k = 20)  # 코사인 유사도 상위 20개 인덱스 및 값

        top_spot_list = [res[idx][0].spot_info_id for idx in top_results[1]]  # 상위 20개의 spot_list 추출
        document = {
            'city_id': -1,
            'town_id': -1,
            'keyword': keyword,
            'value': top_spot_list
            }
        doc_list.append(document)
    collection.insert_many(doc_list)
    return {'asd':'asd'}

# content_type에 따라 각 타입에 맞는 추천 로직 실행
def get_home_recommend(user_id, city_id, town_id, content_type, db: Session):
    if content_type == 39:
        result = get_food_recommend(user_id, city_id, town_id, db)
    elif content_type == 32:
        result = get_lodging_recommend(user_id, city_id, town_id, db)
    else:
        result = get_custom_recommend(user_id, city_id, town_id, db)
    return result

def test():
    return hot_wish_keywords

# 추천 더보기를 위한 api
def get_more_recommend(user_id, city_id, town_id, keyword, db: Session):
    res = []
    document = collection.find_one({'city_id': city_id, 'town_id': town_id, 'keyword': keyword}, {'_id': 0, 'value': 1})
    wish_list = db.query(Wishlist).filter(Wishlist.user_id == user_id).all()
    wish_spot_ids = list(map(lambda x : x.spot_info_id, wish_list))
    spot_id_list = document['value']
    spot_list = spot_list = db.query(SpotInfo)\
                .filter(SpotInfo.spot_info_id.in_(spot_id_list))\
                .all()
    for spot in spot_list:
        spot_info_res = SpotInfoResponse(
                spotInfoId= spot.spot_info_id,
                title= spot.title,
                contentType= str(spot.content_type_id),
                addr= spot.addr1,
                latitude= spot.latitude,
                longitude= spot.longitude,
                img= spot.first_image,
                isWishlist= spot.spot_info_id in wish_spot_ids,
                spot=False,
                recommended_comment= "",
                keyword=keyword
        )
        res.append(spot_info_res)
    return res

# 스프링에 홈 추천 pk 리스트 주기
def get_spring_home(user_id, city_id, town_id, content_type, db: Session):
    if content_type == 39:
        result = get_spring_food(user_id, city_id, town_id, db)
    elif content_type == 32:
        result = get_spring_lodging(user_id, city_id, town_id, db)
    else:
        result = get_spring_recommend(user_id, city_id, town_id, db)
    return result

def get_spring_food(user_id, city_id, town_id, db: Session):
    response = []
    for el in food_dict:
            
        if city_id == -1 and town_id == -1:
            res = db.query(SpotInfo, SpotDetail)\
                .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
                .filter(SpotDetail.cat3 == el).limit(10).all()
        elif city_id != -1 and town_id == -1:
            res = db.query(SpotInfo, SpotDetail)\
                .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
                .filter(SpotInfo.city_id == city_id)\
                .filter(SpotDetail.cat3 == el).limit(10).all()
        elif city_id != -1 and town_id != -1:
            res = db.query(SpotInfo, SpotDetail)\
                .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
                .filter(SpotInfo.city_id == city_id)\
                .filter(SpotInfo.town_id == town_id)\
                .filter(SpotDetail.cat3 == el).limit(10).all()
        id_list = list(map(lambda x : x[0].spot_info_id, res))
        response.append({'comment' : food_comment_dict[food_dict[el]], 'keyword' : food_dict[el], 'idList' : id_list})
    return response


def get_spring_lodging(user_id, city_id, town_id, db: Session):
    response = []
    for el in lodging_dict:
        if city_id == -1 and town_id == -1:
            res = db.query(SpotInfo, SpotDetail)\
                .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
                .filter(SpotDetail.cat3 == el).limit(10).all()
        elif city_id != -1 and town_id == -1:
            res = db.query(SpotInfo, SpotDetail)\
                .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
                .filter(SpotInfo.city_id == city_id)\
                .filter(SpotDetail.cat3 == el).limit(10).all()
        elif city_id != -1 and town_id != -1:
            res = db.query(SpotInfo, SpotDetail)\
                .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
                .filter(SpotInfo.city_id == city_id)\
                .filter(SpotInfo.town_id == town_id)\
                .filter(SpotDetail.cat3 == el).limit(10).all()
        id_list = list(map(lambda x : x[0].spot_info_id, res))
        response.append({'comment' : lodging_comment_dict[lodging_dict[el]], 'keyword' : lodging_dict[el], 'idList' : id_list})
    return response

def get_spring_recommend(user_id, city_id, town_id ,db: Session):
    user = db.query(User).filter(User.user_id == user_id).first()
    user_styles = [style for style in (user.style1, user.style2) if style]
    keywordBlackList = user_styles

    wish_list = db.query(Wishlist).filter(Wishlist.user_id == user_id).all()
    wish_spot_ids = list(map(lambda x : x.spot_info_id, wish_list))
    spot_descriptions = db.query(SpotDescription).filter(SpotDescription.spot_info_id.in_(wish_spot_ids)).all()
    spot_keywords = []
    for el in spot_descriptions: 
        spot_keywords.extend(el.summary.split())
    wishlist_top_two = [item for item, _ in Counter(spot_keywords).most_common(6) if item not in keywordBlackList][:2]
    keywordBlackList += wishlist_top_two
    
    hot_wish_keywords_two = [item for item in hot_wish_keywords if item not in keywordBlackList][:2]
    keywordBlackList += hot_wish_keywords_two

    hot_bucket_keywords_two = [item for item in hot_bucket_keywords if item not in keywordBlackList][:2]
    keywordBlackList += hot_bucket_keywords_two

    res = []

    keyword_dict = {
        'wishlist1': (wishlist_top_two[0] if len(wishlist_top_two) > 0 else ""),
        'wishlist2': (wishlist_top_two[1] if len(wishlist_top_two) > 1 else ""),
        'style1': user_styles[0],
        'style2': (user_styles[1] if len(user_styles) > 1 else ""),
        'hotwish1': hot_wish_keywords_two[0],
        'hotwish2': hot_wish_keywords_two[1],
        'hotbucket1': hot_bucket_keywords_two[0],
        'hotbucket2': hot_bucket_keywords_two[1]
    }
    for el in keyword_dict:
        keyword = keyword_dict.get(el)
        if not keyword:
            continue
        print(el, keyword)
        document = collection.find_one({'city_id': city_id, 'town_id': town_id, 'keyword': keyword}, {'_id': 0, 'value': 1})
        spot_id_list = document['value'][:10]
        res.append({
            "keyword": keyword,
            "comment": recommend_comment_dict[el][0] + keyword + recommend_comment_dict[el][1],
            "idList": spot_id_list,
        })
    return res

def get_spring_keyword(city_id, town_id, keyword, db: Session):
    document = collection.find_one({'city_id': city_id, 'town_id': town_id, 'keyword': keyword}, {'_id': 0, 'value': 1})
    spot_id_list = document['value']
    return  {
                "keyword": keyword,
                "comment": f"{keyword}관련 관광지",
                "idList": spot_id_list,
            }


# 특정 광관지와 가장 비슷한 관광지 찾아 몽고db에 저장
def save_mongo_spot_sim(db : Session):
    res = db.query(SpotInfo, SpotDescription)\
        .join(SpotDescription, SpotInfo.spot_info_id == SpotDescription.spot_info_id)\
        .all()
    
    spot_summaries = [spot_description.overview for (_, spot_description) in res]
    summary_embeddings = model.encode(spot_summaries, convert_to_tensor=True)
    doc_list = []

    for i, (_, spot_description) in enumerate(res):
        cosine_scores = util.pytorch_cos_sim(summary_embeddings[i], summary_embeddings)[0] 
        cosine_scores[i] = -1.0
        top_results = torch.topk(cosine_scores, k=20)
        top_spot_list = [res[idx][0].spot_info_id for idx in top_results[1]]

        document = {
            'spot_info_id': res[i][0].spot_info_id,  # 현재 Spot ID
            'value': top_spot_list  # 가장 유사한 10개의 Spot ID 리스트
        }
        doc_list.append(document)
    
    spot_collection.insert_many(doc_list)


# 특정 광관지에서 가까운 관광지 찾아 몽고db에 저장
def save_mongo_spot_distance(db: Session):
    res = db.query(SpotInfo).all()
    doc_list = []
    
    for spot in res:
        result = db.query(
            SpotInfo.spot_info_id,
            SpotInfo.latitude,
            SpotInfo.longitude,
            (func.pow(SpotInfo.latitude - spot.latitude, 2) +
                 func.pow(SpotInfo.longitude - spot.longitude, 2)).label('distance')
            ).filter(
                SpotInfo.spot_info_id != spot.spot_info_id,
                SpotInfo.city_id == spot.city_id,
                SpotInfo.town_id == spot.town_id
            ).order_by('distance').limit(20).all()

        top_spot_list = [x.spot_info_id for x in result]
        
        document = {
            'spot_info_id': spot.spot_info_id,
            'value': top_spot_list
        }
        doc_list.append(document)
    # distance_collection.insert_many(doc_list)

# 위 두함수를 합친 함수(비슷한, 가까운) 관광지 한번에 저장
def save_combined_spot_info(db: Session):
    # SpotInfo와 SpotDescription을 조인하여 결과를 가져옵니다.
    res = db.query(SpotInfo, SpotDescription)\
        .join(SpotDescription, SpotInfo.spot_info_id == SpotDescription.spot_info_id)\
        .all()
    
    # SpotDescription의 개요를 임베딩합니다.
    spot_summaries = [spot_description.overview for (_, spot_description) in res]
    summary_embeddings = model.encode(spot_summaries, convert_to_tensor=True)
    
    # 업데이트할 문서들을 담기 위한 리스트
    doc_list = []

    for i, (_, spot_description) in enumerate(res):
        # 유사한 관광지 찾기
        cosine_scores = util.pytorch_cos_sim(summary_embeddings[i], summary_embeddings)[0]
        cosine_scores[i] = -1.0  # 자기 자신과의 유사도는 무시합니다.
        top_results = torch.topk(cosine_scores, k=10)
        sim_spot_list = [res[idx][0].spot_info_id for idx in top_results[1]]

        # 현재 관광지 정보 가져오기
        spot = res[i][0]
        # 가까운 관광지 찾기
        distance_results = db.query(
            SpotInfo.spot_info_id,
            (func.pow(SpotInfo.latitude - spot.latitude, 2) +
             func.pow(SpotInfo.longitude - spot.longitude, 2)).label('distance')
        ).filter(
            SpotInfo.spot_info_id != spot.spot_info_id,
            SpotInfo.city_id == spot.city_id,
            SpotInfo.town_id == spot.town_id
        ).order_by('distance').limit(10).all()

        near_spot_list = [x.spot_info_id for x in distance_results]
        
        # 업데이트할 문서
        document = {
            'spot_info_id': spot.spot_info_id,
            'near_spot_id_list': near_spot_list,
            'sim_spot_id_list': sim_spot_list
        }
        
        # MongoDB에서 문서 업데이트 또는 삽입
        spot_collection.update_one(
            {'spot_info_id': spot.spot_info_id},  # 검색 조건
            {'$set': document},  # 업데이트할 필드
            upsert=True  # 문서가 존재하지 않으면 삽입
        )

def get_spring_plan(user_id, city_id, town_id, plan_id, db:Session):
    user = db.query(User).filter(User.user_id == user_id).first()
    user_styles = [style for style in (user.style1, user.style2) if style]
    keywordBlackList = user_styles

    wish_list = db.query(Wishlist).filter(Wishlist.user_id == user_id).all()
    wish_spot_ids = list(map(lambda x : x.spot_info_id, wish_list))

    bucket_list = db.query(PlanBucket).filter(PlanBucket.plan_id == plan_id).all()
    bucket_spot_ids = list(map(lambda x : x.spot_info_id, bucket_list))

    spot_descriptions = db.query(SpotDescription).filter(SpotDescription.spot_info_id.in_(wish_spot_ids)).all()
    spot_keywords = []
    for el in spot_descriptions: 
        spot_keywords.extend(el.summary.split())
    wishlist_top_two = [item for item, _ in Counter(spot_keywords).most_common(6) if item not in keywordBlackList][:2]

    spot_descriptions = db.query(SpotDescription).filter(SpotDescription.spot_info_id.in_(bucket_spot_ids)).all()
    spot_keywords = []
    for el in spot_descriptions: 
        spot_keywords.extend(el.summary.split())
    bucket_top_two = [item for item, _ in Counter(spot_keywords).most_common(6) if item not in keywordBlackList][:2]

    
    keywordBlackList += wishlist_top_two
    
    hot_wish_keywords_two = [item for item in hot_wish_keywords if item not in keywordBlackList][:2]
    keywordBlackList += hot_wish_keywords_two

    hot_bucket_keywords_two = [item for item in hot_bucket_keywords if item not in keywordBlackList][:2]
    keywordBlackList += hot_bucket_keywords_two

    res = []

    keyword_dict = {
        'wishlist1': (wishlist_top_two[0] if len(wishlist_top_two) > 0 else ""),
        'wishlist2': (wishlist_top_two[1] if len(wishlist_top_two) > 1 else ""),
        'bucket1' : (bucket_top_two[0] if len(bucket_top_two) > 0 else ""),
        'bucket2' : (bucket_top_two[1] if len(bucket_top_two) > 0 else ""),
        'style1': user_styles[0],
        'style2': (user_styles[1] if len(user_styles) > 1 else ""),
        'hotwish1': hot_wish_keywords_two[0],
        'hotwish2': hot_wish_keywords_two[1],
        'hotbucket1': hot_bucket_keywords_two[0],
        'hotbucket2': hot_bucket_keywords_two[1]
    }

    for el in keyword_dict:
        keyword = keyword_dict.get(el)
        if not keyword:
            continue
        print(el, keyword)
        document = collection.find_one({'city_id': city_id, 'town_id': town_id, 'keyword': keyword}, {'_id': 0, 'value': 1})
        spot_id_list = document['value'][:10]
        res.append({
            "keyword": keyword,
            "comment": recommend_comment_dict2[el][0] + keyword + recommend_comment_dict2[el][1],
            "idList": spot_id_list,
        })
    return res