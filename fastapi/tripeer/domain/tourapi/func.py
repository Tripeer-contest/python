from models import (
    TourismDetail, CultureFacilityDetail, FestivalDetail, 
    LeportsDetail, TourCourseDetail, LodgingDetail, 
    FoodDetail, ShoppingDetail
)

# 데이터 받아 content_type에 따라 알맞은 모델 반환
def make_model_from_detail_info(spot_id, content_type, data):
    if content_type == 12:
        res = TourismDetail(
            spot_info_id = spot_id,
            content_type_id = content_type,
            accom_count = data.get('accomcount'),
            chk_baby_carriage = data.get('chkbabycarriage'),
            chk_credit_card = data.get('chkcreditcard'),
            chk_pet = data.get('chkpet'),
            exp_age_range = data.get('expagerange'),
            exp_guide = data.get('expguide'),
            info_center = data.get('infocenter'),
            open_date = data.get('opendate'),
            parking = data.get('parking'),
            rest_date = data.get('restdate'),
            use_season = data.get('useseason'),
            use_time = data.get('usetime')
        )
    elif content_type == 28:
        res = LeportsDetail(
            spot_info_id = spot_id,
            content_type_id = content_type,
            scale_leports = data.get('scaleleports'),
            use_fee_leports = data.get('usefeeleports'),
            chk_credit_card_leports = data.get('chkcreditcardleports'),
            chk_baby_carriage_leports = data.get('chkbabycarriageleports'),
            chk_pet_leports = data.get('chkpetleports'),
            exp_age_range_leports = data.get('expagerangeleports'),
            info_center_leports = data.get('infocenterleports'),
            open_period = data.get('openperiod'),
            parking_fee_leports = data.get('parkingfeeleports'),
            parking_leports = data.get('parkingleports'),
            reservation = data.get('reservation'),
            rest_date_leports = data.get('restdateleports'),
            use_time_leports = data.get('usetimeleports'),
            accom_count_leports = data.get('accomcountleports')
        )
    elif content_type == 14:
        res = CultureFacilityDetail(
            spot_info_id = spot_id,
            content_type_id = content_type,
            chk_baby_carriage_culture = data.get('chkbabycarriageculture'),
            chk_credit_card_culture = data.get('chkcreditcardculture'),
            chk_pet_culture = data.get('chkpetculture'),
            discount_info = data.get('discountinfo'),
            info_center_culture = data.get('infocenterculture'),
            parking_culture = data.get('parkingculture'),
            parking_fee = data.get('parkingfee'),
            rest_date_culture = data.get('restdateculture'),
            use_fee = data.get('usefee'),
            use_time_culture = data.get('usetimeculture'),
            scale = data.get('scale'),
            spend_time = data.get('spendtime')
        )
    elif content_type == 15:
        res = FestivalDetail(
            spot_info_id = spot_id,
            content_type_id = content_type,
            discount_info_festival = data.get('discountinfofestival'),
            event_end_date = data.get('eventenddate'),
            play_time = data.get('playtime'),
            place_info = data.get('placeinfo'),
            event_homepage = data.get('eventhomepage'),
            event_place = data.get('eventplace'),
            event_start_date = data.get('eventstartdate'),
            festival_grade = data.get('festivalgrade'),
            program = data.get('program'),
            spend_time_festival = data.get('spendtimefestival'),
            sponsor_1 = data.get('sponsor1'),
            sponsor_1_tel = data.get('sponsor1tel'),
            sponsor_2 = data.get('sponsor2'),
            sponsor_2_tel = data.get('sponsor2tel'),
            sub_event = data.get('subevent'),
            age_limit = data.get('agelimit'),
            booking_place = data.get('bookingplace'),
            use_time_festival = data.get('usetimefestival')
        )
    elif content_type == 25:
        res = TourCourseDetail(
            spot_info_id = spot_id,
            content_type_id = content_type,
            take_time = data.get('taketime'),
            theme = data.get('theme'),
            distance = data.get('distance'),
            info_center_tour_course = data.get('infocentertourcourse'),
            schedule = data.get('schedule')
        )
    elif content_type == 32:
        res = LodgingDetail(
            spot_info_id = spot_id,
            content_type_id = content_type,
            room_count = data.get('roomcount'),
            reservation_lodging = data.get('reservationlodging'),
            reservation_url = data.get('reservationurl'),
            room_type = data.get('roomtype'),
            scale_lodging = data.get('scalelodging'),
            sub_facility = data.get('subfacility'),
            barbecue = data.get('barbecue'),
            beauty = data.get('beauty'),
            beverage = data.get('beverage'),
            bicycle = data.get('bicycle'),
            campfire = data.get('campfire'),
            fitness = data.get('fitness'),
            parking_lodging = data.get('parkinglodging'),
            pickup = data.get('pickup'),
            public_bath = data.get('publicbath'),
            food_place = data.get('foodplace'),
            good_stay = data.get('goodstay'),
            hanok = data.get('hanok'),
            info_center_lodging = data.get('infocenterlodging'),
            karaoke = data.get('karaoke'),
            public_pc = data.get('publicpc'),
            sauna = data.get('sauna'),
            seminar = data.get('seminar'),
            sports = data.get('sports'),
            refund_regulation = data.get('refundregulation'),
            checkin_time = data.get('checkintime'),
            checkout_time = data.get('checkouttime'),
            chk_cooking = data.get('chkcooking'),
            accom_count_lodging = data.get('accomcountlodging'),
            benikia = data.get('benikia')
        )
    elif content_type == 39:
        res = FoodDetail(
            spot_info_id = spot_id,
            content_type_id = content_type,
            chk_credit_card_food = data.get('chkcreditcardfood'),
            discount_info_food = data.get('discountinfofood'),
            first_menu = data.get('firstmenu'),
            info_center_food = data.get('infocenterfood'),
            kids_facility = data.get('kidsfacility'),
            open_date_food = data.get('opendatefood'),
            open_time_food = data.get('opentimefood'),
            packing = data.get('packing'),
            parking_food = data.get('parkingfood'),
            reservation_food = data.get('reservationfood'),
            rest_date_food = data.get('restdatefood'),
            scale_food = data.get('scalefood'),
            seat = data.get('seat'),
            smoking = data.get('smoking'),
            treat_menu = data.get('treatmenu'),
            lcns_no = data.get('lcnsno')
        )
    elif content_type == 38:
        res = ShoppingDetail(
            spot_info_id = spot_id,
            content_type_id = content_type,
            chk_baby_carriage_shopping = data.get('chkbabycarriageshopping'),
            chk_credit_card_shopping = data.get('chkcreditcardshopping'),
            chk_pet_shopping = data.get('chkpetshopping'),
            culture_center = data.get('culturecenter'),
            fair_day = data.get('fairday'),
            info_center_shopping = data.get('infocentershopping'),
            open_date_shopping = data.get('opendateshopping'),
            open_time = data.get('opentime'),
            parking_shopping = data.get('parkingshopping'),
            rest_date_shopping = data.get('restdateshopping'),
            restroom = data.get('restroom'),
            sale_item = data.get('saleitem'),
            sale_item_cost = data.get('saleitemcost'),
            scale_shopping = data.get('scaleshopping'),
            shop_guide = data.get('shopguide')
        )
    else:
        res = None

    return res
