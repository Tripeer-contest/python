from sqlalchemy import Column, Integer, String, Float, DateTime, BigInteger, Date, Boolean
from sqlalchemy.orm import relationship

from database import Base

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
    summary = Column(String(500), nullable=False)

class User(Base):
    __tablename__ = 'user'

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    provider = Column(String(45), nullable=False)
    provider_id = Column(String(128), nullable=False)
    email = Column(String(45), nullable=False)
    nickname = Column(String(30), nullable=False)
    birth = Column(Date, nullable=True)
    profile_image = Column(String(255), nullable=True)
    role = Column(String(30), nullable=False)
    style1 = Column(String(45), nullable=True)
    style2 = Column(String(45), nullable=True)
    style3 = Column(String(45), nullable=True)
    is_online = Column(Boolean, nullable=False, default=False)

class Wishlist(Base):
    __tablename__ = 'wishlist'

    wishlist_id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    spot_info_id = Column(Integer, nullable=False)

class PlanBucket(Base):
    __tablename__ = 'plan_bucket'

    plan_bucket_id = Column(BigInteger, primary_key=True, autoincrement=True)
    plan_id = Column(BigInteger, nullable=False)
    spot_info_id = Column(Integer, nullable=False)
    user_id = Column(BigInteger, nullable=False)

#  --------------     tourApi  (추가된 상세정보)    --------------------
class TourismDetail(Base):
    __tablename__ = 'additional_tourism'  # 관광지 상세정보
    
    spot_info_id = Column(Integer, primary_key=True)
    content_type_id = Column(Integer, nullable=False)
    accom_count = Column(String(255))  # 수용 인원 수
    chk_baby_carriage = Column(String(255))  # 유모차 대여 여부
    chk_credit_card = Column(String(255))  # 신용카드 사용 가능 여부
    chk_pet = Column(String(255))  # 반려동물 동반 가능 여부
    exp_age_range = Column(String(255))  # 경험 적합 연령대
    exp_guide = Column(String(255))  # 체험 안내
    info_center = Column(String(255))  # 안내센터 정보
    open_date = Column(String(255))  # 개장일
    parking = Column(String(255))  # 주차 정보
    rest_date = Column(String(255))  # 휴무일
    use_season = Column(String(255))  # 사용 가능 계절
    use_time = Column(String(255))  # 사용 가능 시간

class CultureFacilityDetail(Base):
    __tablename__ = 'additional_culture_facility'  # 문화시설 상세정보
    
    spot_info_id = Column(Integer, primary_key=True)
    content_type_id = Column(Integer, nullable=False)
    chk_baby_carriage_culture = Column(String(255))  # 유모차 대여 여부
    chk_credit_card_culture = Column(String(255))  # 신용카드 사용 가능 여부
    chk_pet_culture = Column(String(255))  # 반려동물 동반 가능 여부
    discount_info = Column(String(255))  # 할인 정보
    info_center_culture = Column(String(255))  # 안내센터 정보
    parking_culture = Column(String(255))  # 주차 정보
    parking_fee = Column(String(255))  # 주차 요금
    rest_date_culture = Column(String(255))  # 휴무일
    use_fee = Column(String(255))  # 이용 요금
    use_time_culture = Column(String(255))  # 이용 시간
    scale = Column(String(255))  # 규모
    spend_time = Column(String(255))  # 소요 시간

class FestivalDetail(Base):
    __tablename__ = 'additional_festival'  # 축제 상세정보
    
    spot_info_id = Column(Integer, primary_key=True)
    content_type_id = Column(Integer, nullable=False)
    discount_info_festival = Column(String(255))  # 축제 할인 정보
    event_end_date = Column(String(255))  # 행사 종료일
    play_time = Column(String(255))  # 공연 시간
    place_info = Column(String(255))  # 행사 장소 정보
    event_homepage = Column(String(255))  # 행사 홈페이지
    event_place = Column(String(255))  # 행사 장소
    event_start_date = Column(String(255))  # 행사 시작일
    festival_grade = Column(String(255))  # 축제 등급
    program = Column(String(255))  # 프로그램 정보
    spend_time_festival = Column(String(255))  # 축제 소요 시간
    sponsor_1 = Column(String(255))  # 후원사 1
    sponsor_1_tel = Column(String(255))  # 후원사 1 연락처
    sponsor_2 = Column(String(255))  # 후원사 2
    sponsor_2_tel = Column(String(255))  # 후원사 2 연락처
    sub_event = Column(String(255))  # 부대 행사
    age_limit = Column(String(255))  # 연령 제한
    booking_place = Column(String(255))  # 예약 장소
    use_time_festival = Column(String(255))  # 축제 이용 시간

class LeportsDetail(Base):
    __tablename__ = 'additional_leports'  # 레포츠 상세정보
    
    spot_info_id = Column(Integer, primary_key=True)
    content_type_id = Column(Integer, nullable=False)
    scale_leports = Column(String(255))  # 레포츠 규모
    use_fee_leports = Column(String(255))  # 레포츠 이용 요금
    chk_credit_card_leports = Column(String(255))  # 신용카드 사용 가능 여부
    chk_baby_carriage_leports = Column(String(255))  # 유모차 대여 여부
    chk_pet_leports = Column(String(255))  # 반려동물 동반 가능 여부
    exp_age_range_leports = Column(String(255))  # 경험 적합 연령대
    info_center_leports = Column(String(255))  # 안내센터 정보
    open_period = Column(String(255))  # 개장 기간
    parking_fee_leports = Column(String(255))  # 주차 요금
    parking_leports = Column(String(255))  # 주차 정보
    reservation = Column(String(255))  # 예약 정보
    rest_date_leports = Column(String(255))  # 휴무일
    use_time_leports = Column(String(255))  # 이용 시간
    accom_count_leports = Column(String(255))  # 수용 인원 수

class TourCourseDetail(Base):
    __tablename__ = 'additional_tour_course'  # 여행코스 상세정보
    
    spot_info_id = Column(Integer, primary_key=True)
    content_type_id = Column(Integer, nullable=False)
    take_time = Column(String(255))  # 소요 시간
    theme = Column(String(255))  # 테마
    distance = Column(String(255))  # 거리
    info_center_tour_course = Column(String(255))  # 안내센터 정보
    schedule = Column(String(255))  # 일정

class LodgingDetail(Base):
    __tablename__ = 'additional_lodging'  # 숙소 상세정보
    
    spot_info_id = Column(Integer, primary_key=True)
    content_type_id = Column(Integer, nullable=False)
    room_count = Column(String(255))  # 객실 수
    reservation_lodging = Column(String(255))  # 예약 가능 여부
    reservation_url = Column(String(255))  # 예약 URL
    room_type = Column(String(255))  # 객실 타입
    scale_lodging = Column(String(255))  # 숙박 시설 규모
    sub_facility = Column(String(255))  # 부대시설
    barbecue = Column(String(255))  # 바베큐 시설
    beauty = Column(String(255))  # 미용 시설
    beverage = Column(String(255))  # 음료 제공 여부
    bicycle = Column(String(255))  # 자전거 대여 여부
    campfire = Column(String(255))  # 캠프파이어 가능 여부
    fitness = Column(String(255))  # 피트니스 시설
    parking_lodging = Column(String(255))  # 주차 시설
    pickup = Column(String(255))  # 픽업 서비스
    public_bath = Column(String(255))  # 공용 목욕 시설
    food_place = Column(String(255))  # 음식점
    good_stay = Column(String(255))  # 굿스테이 인증 여부
    hanok = Column(String(255))  # 한옥 여부
    info_center_lodging = Column(String(255))  # 안내센터 정보
    karaoke = Column(String(255))  # 노래방 여부
    public_pc = Column(String(255))  # 공용 PC 제공 여부
    sauna = Column(String(255))  # 사우나 시설
    seminar = Column(String(255))  # 세미나실
    sports = Column(String(255))  # 스포츠 시설
    refund_regulation = Column(String(255))  # 환불 규정
    checkin_time = Column(String(255))  # 체크인 시간
    checkout_time = Column(String(255))  # 체크아웃 시간
    chk_cooking = Column(String(255))  # 취사 가능 여부
    accom_count_lodging = Column(String(255))  # 수용 인원 수
    benikia = Column(String(255))  # 베니키아 호텔 여부

class FoodDetail(Base):
    __tablename__ = 'additional_food'  # 음식점 상세정보
    
    spot_info_id = Column(Integer, primary_key=True)
    content_type_id = Column(Integer, nullable=False)
    chk_credit_card_food = Column(String(255))  # 신용카드 사용 가능 여부
    discount_info_food = Column(String(255))  # 할인 정보
    first_menu = Column(String(255))  # 대표 메뉴
    info_center_food = Column(String(255))  # 안내센터 정보
    kids_facility = Column(String(255))  # 어린이 시설 여부
    open_date_food = Column(String(255))  # 개장일
    open_time_food = Column(String(255))  # 영업 시간
    packing = Column(String(255))  # 포장 가능 여부
    parking_food = Column(String(255))  # 주차 정보
    reservation_food = Column(String(255))  # 예약 가능 여부
    rest_date_food = Column(String(255))  # 휴무일
    scale_food = Column(String(255))  # 음식점 규모
    seat = Column(String(255))  # 좌석 수
    smoking = Column(String(255))  # 흡연 가능 여부
    treat_menu = Column(String(255))  # 제공 메뉴
    lcns_no = Column(String(255))  # 사업자 등록 번호

class ShoppingDetail(Base):
    __tablename__ = 'additional_shopping'  # 쇼핑 상세정보
    
    spot_info_id = Column(Integer, primary_key=True)  # 쇼핑 상세 정보의 고유 ID
    content_type_id = Column(Integer, nullable=False)  # 컨텐츠 타입 ID
    chk_baby_carriage_shopping = Column(String(255))  # 유모차 대여 여부
    chk_credit_card_shopping = Column(String(255))  # 신용카드 사용 가능 여부
    chk_pet_shopping = Column(String(255))  # 반려동물 동반 가능 여부
    culture_center = Column(String(255))  # 문화센터 정보
    fair_day = Column(String(255))  # 장날 정보
    info_center_shopping = Column(String(255))  # 안내센터 정보
    open_date_shopping = Column(String(255))  # 개장일
    open_time = Column(String(255))  # 영업 시간
    parking_shopping = Column(String(255))  # 주차 정보
    rest_date_shopping = Column(String(255))  # 휴무일
    restroom = Column(String(255))  # 화장실 유무
    sale_item = Column(String(255))  # 판매 상품
    sale_item_cost = Column(String(255))  # 판매 상품 가격
    scale_shopping = Column(String(255))  # 쇼핑몰 규모
    shop_guide = Column(String(255))  # 매장 안내

