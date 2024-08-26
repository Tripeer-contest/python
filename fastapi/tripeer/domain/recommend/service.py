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
from .variable import stop_list, city_town_list, cat2, cat3, union_values, my_keywords_list, city_id_list
from .schema import SpotInfoResponse

mongodb = get_mongo()
collection = mongodb['recommend2']
collection.create_index([('city_id', ASCENDING), ('town_id', ASCENDING), ('keyword', ASCENDING)], unique=True)

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

def ckeck_keywords(db: Session):
    spot_detail = db.query(SpotDescription).all()
    lst = []
    for spot in spot_detail:
        lst.extend(spot.summary.split())
    freq = Counter(lst)
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    return sorted_freq

# 내가 만든 키워드로 추천해주는 로직(tripeer 1.0에 추천 로직)
def get_custom_recommend(user_id,db: Session):
    user = db.query(User).filter(User.user_id == user_id).first()
    user_styles = [style for style in (user.style1, user.style2) if style]
    keywordBlackList = user_styles

    wish_list = db.query(Wishlist).filter(Wishlist.user_id == user_id).all()
    spot_ids = list(map(lambda x : x.spot_info_id, wish_list))
    spot_descriptions = db.query(SpotDescription).filter(SpotDescription.spot_info_id.in_(spot_ids)).all()
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
        'bucket1': [],
        'bucket2': [],
        'style1': [],
        'style2': [],
        'hotbucket': [],
        'hotwish': []
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

    print(keyword_dict)
    
    # for el in plan_town_list:
    #     city_id = el.city_only_id if el.city_only_id else el.city_id
    #     town_id = -1 if el.city_only_id else el.town_id

    #     embedding_path = f"csv/{city_id}/{town_id}/embedding.csv"
    #     loaded_df = pd.read_csv(embedding_path, delimiter=",", dtype=np.float32)
    #     loaded_tensor = torch.tensor(loaded_df.values)
    #     id_list = np.loadtxt(f"csv/{city_id}/{town_id}/id_list.csv", delimiter=",")

    #     for i, wishlist_keyword in enumerate(wishlist_top_two):
    #         mongodb_data = read_data(city_id, town_id, wishlist_keyword)
    #         if mongodb_data:
    #             res[f'wishlist{i+1}'].extend(mongodb_data)

    #     for i, bucket_keyword in enumerate(bucket_top_two):
    #         mongodb_data = read_data(city_id, town_id, bucket_keyword)
    #         if mongodb_data:
    #             res[f'bucket{i+1}'].extend(mongodb_data)

    #     for i, style_keyword in enumerate(user_styles):
    #         mongodb_data = read_data(city_id, town_id, style_keyword)
    #         if mongodb_data:
    #             res[f'style{i+1}'].extend(mongodb_data)
        
        
    #     mongodb_data = read_data(city_id, town_id, most_wish_keyword)
    #     if mongodb_data:
    #         res['hotwish'].extend(mongodb_data)
            
    #     mongodb_data = read_data(city_id, town_id, most_bucket_keyword)
    #     if mongodb_data:
    #         res['hotwish'].extend(mongodb_data)
    
    
    # final_data = []
    # for key, value in res.items():
    #     if value:
    #         response_data = []
    #         value = sorted(value, key=lambda x: x[1], reverse=True)
    #         for el in value[:15]:
    #             if el[0] in black_list:
    #                 continue
    #             spot_info = db.query(SpotInfo).filter(SpotInfo.spot_info_id == int(el[0])).first()
                
    #             if spot_info:
    #                 spot_info_res = SpotInfoResponse(
    #                     spotInfoId=spot_info.spot_info_id,
    #                     contentType=content_type_dic.get(spot_info.content_type_id, "Unknown"),
    #                     title=spot_info.title,
    #                     addr=spot_info.addr1,
    #                     img=spot_info.first_image,
    #                     latitude=float(spot_info.latitude),
    #                     longitude=float(spot_info.longitude),
    #                     isWishlist=False,
    #                     spot=False,
    #                     recommended_comment=f"{key}에서 찾은 키워드 '{keyword_dict[key]}'과 관련된 관광지",
    #                     keyword=str(keyword_dict[key])
    #                 )
    #                 response_data.append(spot_info_res)
    #         recommend_response = RecommendResponse(
    #             main=keyword_dict[key],
    #             sub=key,
    #             spotItemList=response_data
    #         )
    #         final_data.append(recommend_response)

    return "final_data"


# 각 시도, 타운, 키워드 기준 추천 리스트를 미리만들어 몽고db에 저장
# 반복되는 부분 함수로 따로 빼기
def save_mongo(db: Session):
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


def get_home_recommend(user_id, city_id, town_id, content_type, db: Session):
    if city_id == -1 and town_id == -1 and content_type == -1:
        res = db.query(SpotInfo, SpotDetail)\
            .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
            .all()
    elif city_id != -1 and town_id == -1:
        res = db.query(SpotInfo, SpotDetail)\
            .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
            .filter(SpotInfo.spot_info_id == id).first()


    # SQLAlchemy ORM 객체를 딕셔너리로 변환
    spot_info, spot_detail = res

    def serialize(obj):
        return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

    # JSON 직렬화 가능한 딕셔너리로 변환
    result = {
        "spot_info": serialize(spot_info),
        "spot_detail": serialize(spot_detail),
    }
    return result

def test():
    return hot_wish_keywords