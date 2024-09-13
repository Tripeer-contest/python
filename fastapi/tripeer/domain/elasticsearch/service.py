import os
from fastapi import HTTPException
from elasticsearch import Elasticsearch
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import SpotInfo, SpotDetail, SpotDescription
from domain.recommend.variable import cat3

# 환경 변수에서 Elasticsearch 계정 정보 가져오기
ES_USER = os.environ.get('ES_USER')
ES_PASSWORD = os.environ.get('ES_PASSWORD')
ES_URL = os.environ.get('ES_URL')

# Elasticsearch 클라이언트 설정
es = Elasticsearch(
    [ES_URL],
    ca_certs='./http_ca.crt',
    basic_auth=(ES_USER, ES_PASSWORD)
)


# 엘라스틱서치에 넣을 모델
class Spot(BaseModel):
    title: str
    addr: str
    description: str
    cat: str

def insert_spot(spot_info_id, title, addr, description, cat, lat, lon):
    doc = {
        "title": title,
        "addr": addr,
        "description": description,
        "cat": cat,
        "location": {
            "lat": lat,
            "lon": lon
        }
    }
    response = es.index(index="test", id=spot_info_id, document=doc)
    return response['_id']


def create_index(index_name):
    # 인덱스 설정 및 매핑
    index_settings = {
        "settings": {
            "analysis": {
                "tokenizer": {
                    "nori_mixed": {
                        "type": "nori_tokenizer",
                        "decompound_mode": "mixed"
                    }
                },
                "analyzer": {
                    "my_analyzer": {
                        "type": "custom",
                        "tokenizer": "nori_mixed",
                        "filter": ["lowercase"]
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "title": {
                    "type": "text", 
                    "analyzer": "my_analyzer",
                    "fields": {
                        "completion": {
                            "type": "completion"
                        }
                    }
                },
                "content_type_id": {"type": "number",},
                "addr": {"type": "text", "analyzer": "my_analyzer"},
                "description": {"type": "text", "analyzer": "my_analyzer"},
                "location": {"type": "geo_point"},
                "cat": {"type": "text", "analyzer": "my_analyzer"} 
            }
        }
    }
    es.indices.create(index=index_name, body=index_settings)    # 인덱스 생성
    return {"message" : "생성 성공"}

def delete_index(index_name):
    es.indices.delete(index=index_name)
    return {"message" : "삭제 성공"}

def test(db : Session):
    (spot_info, spot_detail, spot_description) = db.query(SpotInfo, SpotDetail, SpotDescription)\
            .join(SpotDetail, SpotInfo.spot_info_id == SpotDetail.spot_info_id)\
            .join(SpotDescription, SpotInfo.spot_info_id == SpotDescription.spot_info_id)\
            .first()
    # Elasticsearch에 데이터 삽입
    response = insert_spot(
        spot_info_id = spot_info.spot_info_id,
        title = spot_info.title,
        addr = spot_info.addr1,
        lat = spot_info.latitude,
        lon = spot_info.longitude,
        description = spot_description.overview, 
        cat = cat3.get(spot_detail.cat3)
        )
    return {"message": "Spot added successfully", "id": spot_info.spot_info_id}

def search_all():
    try:
        result = es.search(index="test", query={"match_all": {}})
        return result['hits']['hits']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def search_by_keyword(keyword):
    try:
        query = {
            "multi_match": {
                "query": keyword,
                "fields": ["title", "description", "addr", "cat"]
            }
        }
        result = es.search(index="test", query=query)
        return result['hits']['hits']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

def search_by_keyword_and_location(keyword, min_lat, min_lon, max_lat, max_lon):
    try:
        query = {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": keyword,
                        "fields": ["title", "description", "addr", "cat"]
                    }
                },
                "filter": {
                    "geo_bounding_box": {
                        "location": {
                            "top_right": {
                                "lat": max_lat,
                                "lon": max_lon
                            },
                            "bottom_left": {
                                "lat": min_lat,
                                "lon": min_lon
                            }
                        }
                    }
                }
            }
        }
        
        result = es.search(index="test", query=query)
        return result['hits']['hits']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))