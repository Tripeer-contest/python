stop_list = ('아', '휴', '아이구', '아이쿠', '아이고', '어', '나', '우리', '저희', '따라', '의해', 
    '을', '를', '에', '의', '가', '으로', '로', '에게', '뿐이다', '의거하여', '근거하여', 
    '입각하여', '기준으로', '예하면', '예를', '들면', '예를', '들자면', '저', '소인', '소생',
    '저희', '지말고', '하지마', '하지마라', '다른', '물론', '또한', '그리고', '비길수', '없다',
    '해서는', '안된다', '뿐만', '아니라', '만이', '아니다', '만은', '아니다', '막론하고',
    '관계없이', '그치지', '않다', '그러나', '그런데', '하지만', '든간에', '논하지', '않다',
    '따지지', '않다', '설사', '비록', '더라도', '아니면', '만', '못하다', '하는', '편이',
    '낫다', '불문하고', '향하여', '향해서', '향하다', '쪽으로', '틈타', '이용하여', '타다',
    '오르다', '제외하고', '이', '외에', '이', '밖에', '하여야', '비로소', '한다면', '몰라도', 
    '외에도', '이곳', '여기', '부터', '기점으로', '따라서', '할', '생각이다', '하려고하다', '이리하여', 
    '그리하여', '그렇게', '함으로써', '하지만', '일때', '할때', '앞에서', '중에서', '보는데서', '으로써', 
    '로써', '까지', '해야한다', '일것이다', '반드시', '할줄알다', '할수있다', '할수있어', '임에', 
    '틀림없다', '한다면', '등', '등등', '제', '겨우', '단지', '다만', '할뿐', '딩동', '댕그', 
    '대해서', '대하여', '대하면', '훨씬', '얼마나', '얼마만큼', '얼마큼', '남짓', '여', '얼마간', 
    '약간', '다소', '좀', '조금', '다수', '몇', '얼마', '지만', '하물며', '또한', '그러나', '그렇지만', 
    '하지만', '이외에도', '대해', '말하자면', '뿐이다', '다음에', '반대로', '반대로', '말하자면', '이와', 
    '반대로', '바꾸어서', '말하면', '바꾸어서', '한다면', '만약', '그렇지않으면', '까악', '툭', '딱', 
    '삐걱거리다', '보드득', '비걱거리다', '꽈당', '응당', '해야한다', '에', '가서', '각', '각각', '여러분', 
    '각종', '각자', '제각기', '하도록하다', '와', '과', '그러므로', '그래서', '고로', '한', '까닭에', 
    '하기', '때문에', '거니와', '이지만', '대하여', '관하여', '관한', '과연', '실로', '아니나다를가', 
    '생각한대로', '진짜로', '한적이있다', '하곤하였다', '하', '하하', '허허', '아하', '거바', '와', '오', 
    '왜', '어째서', '무엇때문에', '어찌', '하겠는가', '무슨', '어디', '어느곳', '더군다나', '하물며', 
    '더욱이는', '어느때', '언제', '야', '이봐', '어이', '여보시오', '흐흐', '흥', '휴', '헉헉', '헐떡헐떡', 
    '영차', '여차', '어기여차', '끙끙', '아야', '앗', '아야', '콸콸', '졸졸', '좍좍', '뚝뚝', '주룩주룩', 
    '솨', '우르르', '그래도', '또', '그리고', '바꾸어말하면', '바꾸어말하자면', '혹은', '혹시', '답다', '및', 
    '그에', '따르는', '때가', '되어', '즉', '지든지', '설령', '가령', '하더라도', '할지라도', '일지라도', 
    '지든지', '몇', '거의', '하마터면', '인젠', '이젠', '된바에야', '된이상', '만큼', '어찌됏든', '그위에', 
    '게다가', '점에서', '보아', '비추어', '보아', '고려하면', '하게될것이다', '일것이다', '비교적', '좀', 
    '보다더', '비하면', '시키다', '하게하다', '할만하다', '의해서', '연이서', '이어서', '잇따라', '뒤따라', 
    '뒤이어', '결국', '의지하여', '기대여', '통하여', '자마자', '더욱더', '불구하고', '얼마든지', '마음대로', 
    '주저하지', '않고', '곧', '즉시', '바로', '당장', '하자마자', '밖에', '안된다', '하면된다', '그래', 
    '그렇지', '요컨대', '다시', '말하자면', '바꿔', '말하면', '즉', '구체적으로', '말하자면', '시작하여', 
    '시초에', '이상', '허', '헉', '허걱', '바와같이', '해도좋다', '해도된다', '게다가', '더구나', '하물며', 
    '와르르', '팍', '퍽', '펄렁', '동안', '이래', '하고있었다', '이었다', '에서', '로부터', '까지', '예하면', 
    '했어요', '해요', '함께', '같이', '더불어', '마저', '마저도', '양자', '모두', '습니다', '가까스로', 
    '하려고하다', '즈음하여', '다른', '다른', '방면으로', '해봐요', '습니까', '했어요', '말할것도', '없고', 
    '무릎쓰고', '개의치않고', '하는것만', '못하다', '하는것이', '낫다', '매', '매번', '들', '모', '어느것', 
    '어느', '로써', '갖고말하자면', '어디', '어느쪽', '어느것', '어느해', '어느', '년도', '라', '해도', 
    '언젠가', '어떤것', '어느것', '저기', '저쪽', '저것', '그때', '그럼', '그러면', '요만한걸', '그래', 
    '그때', '저것만큼', '그저', '이르기까지', '할', '줄', '안다', '할', '힘이', '있다', '너', '너희', 
    '당신', '어찌', '설마', '차라리', '할지언정', '할지라도', '할망정', '할지언정', '구토하다', '게우다', 
    '토하다', '메쓰겁다', '옆사람', '퉤', '쳇', '의거하여', '근거하여', '의해', '따라', '힘입어', '그', 
    '다음', '버금', '두번째로', '', '첫번째로', '나머지는', '그중에서', '견지에서', '형식으로', '쓰여', 
    '입장에서', '위해서', '단지', '의해되다', '하도록시키다', '뿐만아니라', '반대로', '전후', '전자', '앞의것', 
    '잠시', '잠깐', '하면서', '그렇지만', '다음에', '그러한즉', '그런즉', '남들', '아무거나', '어찌하든지', 
    '같다', '비슷하다', '예컨대', '이럴정도로', '어떻게', '만약', '만일', '위에서', '서술한바와같이', '인', 
    '듯하다', '하지', '않는다면', '만약에', '무엇', '무슨', '어느', '어떤', '아래윗', '조차', '한데', '그럼에도', 
    '불구하고', '여전히', '심지어', '까지도', '조차도', '하지', '않도록', '않기', '위하여', '때', '시각', '무렵', 
    '시간', '동안', '어때', '어떠한', '하여금', '네', '예', '우선', '누구', '누가', '알겠는가', '아무도', 
    '줄은모른다', '줄은', '몰랏다', '하는', '김에', '겸사겸사', '하는바', '그런', '까닭에', '한', '이유는', 
    '그러니', '그러니까', '때문에', '그', '너희', '그들', '너희들', '타인', '것', '것들', '너', '위하여', 
    '공동으로', '동시에', '하기', '위하여', '어찌하여', '무엇때문에', '붕붕', '윙윙', '나', '우리', '엉엉', 
    '휘익', '윙윙', '오호', '아하', '어쨋든', '만', '못하다', '하기보다는', '차라리', '하는', '편이', '낫다', 
    '흐흐', '놀라다', '상대적으로', '말하자면', '마치', '아니라면', '쉿', '그렇지', '않으면', '그렇지', '않다면', 
    '안', '그러면', '아니었다면', '하든지', '아니면', '이라면', '좋아', '알았어', '하는것도', '그만이다', '어쩔수', 
    '없다', '하나', '일', '일반적으로', '일단', '한켠으로는', '오자마자', '이렇게되면', '이와같다면', '전부', 
    '한마디', '한항목', '근거로', '하기에', '아울러', '하지', '않도록', '않기', '위해서', '이르기까지', '이', 
    '되다', '로', '인하여', '까닭으로', '이유만으로', '이로', '인하여', '그래서', '이', '때문에', '그러므로', 
    '그런', '까닭에', '알', '수', '있다', '결론을', '낼', '수', '있다', '으로', '인하여', '있다', '어떤것', 
    '관계가', '있다', '관련이', '있다', '연관되다', '어떤것들', '에', '대해', '이리하여', '그리하여', '여부', 
    '하기보다는', '하느니', '하면', '할수록', '운운', '이러이러하다', '하구나', '하도다', '다시말하면', '다음으로', 
    '에', '있다', '에', '달려', '있다', '우리', '우리들', '오히려', '하기는한데', '어떻게', '어떻해', '어찌됏어', 
    '어때', '어째서', '본대로', '자', '이', '이쪽', '여기', '이것', '이번', '이렇게말하자면', '이런', '이러한', 
    '이와', '같은', '요만큼', '요만한', '것', '얼마', '안', '되는', '것', '이만큼', '이', '정도의', '이렇게', 
    '많은', '것', '이와', '같다', '이때', '이렇구나', '것과', '같이', '끼익', '삐걱', '따위', '와', '같은', 
    '사람들', '부류의', '사람들', '왜냐하면', '중의하나', '오직', '오로지', '에', '한하다', '하기만', '하면', 
    '도착하다', '까지', '미치다', '도달하다', '정도에', '이르다', '할', '지경이다', '결과에', '이르다', '관해서는', 
    '여러분', '하고', '있다', '한', '후', '혼자', '자기', '자기집', '자신', '우에', '종합한것과같이', '총적으로', 
    '보면', '총적으로', '말하면', '총적으로', '대로', '하다', '으로서', '참', '그만이다', '할', '따름이다', '쿵', 
    '탕탕', '쾅쾅', '둥둥', '봐', '봐라', '아이야', '아니', '와아', '응', '아이', '참나', '년', '월', '일', 
    '령', '영', '일', '이', '삼', '사', '오', '육', '륙', '칠', '팔', '구', '이천육', '이천칠', '이천팔', 
    '이천구', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉', '령', '영', ',', '.', 
    '(', ')', '{', '}', '[', ']', '이다', '있어', '곳에', '있는', '곳이다', '이후', '수', '곳','위치','메뉴',
    '층','경기도', '시설', '이용', '운영', '지역', '건물', '리', '위', '인근', '개', '제공', '객실', '강원도', '국내', 
    '서울', '제주', '옥', '사용', '길', '판매', '은', '앞', '사이트', '근처', '주변', '부산', '약', '서울특별시',
    '사람','인천', '칸', '중', '전문', '테이블', '내', '속', '주차장', '규모', '이름', '번', '가장', '세계', '관'
    '호선', '도시', '정식', '면', '재료', '갈비', '위해', '전', '영업', '볼', '가지', '칼국수', '외관', 
    '주문', '잡고', '시민', '경북', '충청남도', '정도', '충남', '센터', '양념', '밥', '대구', '지하철', 
    '주민', '길이', '울산', '방', '실', '방문', '돼지', '옆', '도서관', '현재', '생', '고객', '현대', 
    '석', '지정', '꽃', '문', '선생', '탕', '인기', '최고', '지방', '오리', '마련', '사랑', '중심', '단체', '충청북도', 
    '본점', '해물', '자락', '손님', '서비스', '말', '향', '통영', '전라남도', '숯불', '통해', '최대', '국물', '불고기', '우리나라',
    '냉면', '최초', '경주', '예약', '육수', '모습', '도로', '위패', '전국', '설치', '한강', '더', '브런치', '자랑', '개관', '온', 
    '음료', '모든', '높이', '가격', '채', '차', '사이', '비', '국', '중앙', '홀', '정보', '느낌', '개최', '신라',
    '성', '충북', '국제', '아래', '제주도', '대전광역시', '짬뽕', '평','촌', '외국인', '준비', '돌', '존', '가든', 
    '제주시', '건립', '반찬', '경주시', '생활',  '맑은', '변', '뜻', '막국수', '골', '장소', '아트', '봉안', '모임', 
    '호', '출구', '소나무', '사업', '마당', '진행', '시', '생선', '국수', '구성', '메밀', '종', '장어', '명', '절', 
    '남', '여수', '광장', '룸', '지붕', '북한', '경남', '대형', '중구', '선정', '하늘', '남쪽', '회관', '대전', '활동', 
    '가게', '류', '여러', '종류', '남해', '손', '업', '대한민국', '지금', '강릉', '푸른', '두부', '수제', '면적', '고려',
    '대표', '내부', '직접', '전문점', '조성', '물', '집', '분위기', '매장', '한국', '외', '바위', '한우', '인테리어', '비롯', '점', 
    '나무', '도', '때문', '입구', '조선', '눈', '감상', '터', '계', '뒤', '창건', '관광객', '봉', '총', '두',
    '바', '호선', '당시', '듯', '로서', '자료', '형태', '수도', '사진', '그대로', '일반', '관리', '객', '정상', 
    '모양', '편의', '소개', '배', '화장실', '무료', '활용', '물이', '뿐', '통', '전체', '조선시대', '장', '살', '특징', 
    '기본', '계절', '곳곳', '경우', '데크', '연출', '마음', '보존', '부대', '한눈', '세', '대한', '매년', '크기', '가능', '더욱', 
    '좌석', '환경', '배치', '밤', '지하', '일대', '세트', '여유', '추가', '기', '추억', '재', '개발', '단', '포장', '스님', '자동차',
    '만들기', '시대', '관련', '형성', '복원', '입', '피', '청정', '동시', '일품', '용', '구조', '운동', '채소', '단위', '타고', 
    '생산', '선', '움', '추천', '동쪽', '입장', '함', '선택', '쪽', '초', '불', '매우', '이야기', '기도', '광', '가운데', 
    '사계절', '기록', '달', '다리', '조각', '끝', '체육', '소리', '건축', '복합', '정자', '처', '의미', '전복', '서쪽', '역할', 
    '별도', '암', '달리', '폭', '선사', '날', '샐러드', '산이', '구비', '매일', '밑반찬', '불가', '일본', '가치', '처음', '오토', 
    '도착', '정면', '남아', '확인', '먹거리', '청소년','발전', '바비큐', '일반축제', '인접', '아침', '포토', '주말', '청',
    '포함', '이자', '울창', '모텔', '외부', '만날', '보고', '이외', '옛날', '국가', '북쪽', '몸', '바람', '작가', '티', 
    '굴', '현', '서양식', '참여', '정', '기념', '양', '농.산.어촌', '금', '소', '개인', '적', '연결', '치즈', '비빔밥', 
    '부근', '측면', '풀', '만두', '마루', '종합', '지나', '낙지', '갯벌', '연인', '학교', '촬영', '조명', '바닥', 
    '조리', '포', '목', '지은', '식', '소스', '수려', '품', '장군', '임진왜란', '목적', '둘러보기', '숲속', '연구', '농촌', 
    '편', '야채', '조화', '그림', '벚꽃', '구간', '창', '벽', '피자', '기능', '전설', '설립', '크림', '출처', '머리', '좌',
    '안전', '산업', '특산', '유명', '역', '매운탕', '보유', '끼', '재배', '오름', '과정', '대웅전', '차량', '원래', '교통', '간', '무', 
    '비즈니스', '메뉴인', '겸', '숙박', '볶음', '별미', '북', '셀프', '방향', '사장', '연못', '책', '텐트', '유지', '지상', '왕', '부분',
    '오픈', '배경', '고종', '주인', '분', '튀김', '산성', '구매', '노력', '매점', '케이크', '만끽',  '빛', '골프장', '시청', '골프',
    '감', '고택', '여름철', '계단', '절벽', '농장', '구역', '디자인', '중간', '이동', '삶', '저녁', '소품', '간직', '중이', '동해', '맞이', 
    '시골', '추정', '상품', '대중교통', '항', '의자', '가득', '제품', '밭', '전골', '중국', '지점', '짐', '즐거움', '민속',
    '보물', '매력', '삼겹살', '이면', '선조', '절경', '여행객', '기둥', '아메리카노', '재미', '부', '운', '능선', '가로',
    '정성', '하루', '평화', '최근', '국밥', '주위', '차례', '화공', '주요', '터미널', '사당', '주로', '주', '음악', '대회',
    '보이', '주방', '대부분', '발견', '등심', '문화원', '멋', '제작', '시내', '사회', '닭', '과일', '주제', '지구', '별로', 
    '개장', '찜', '접근성', '소고기', '여행지', '지로', '취사', '방문객', '조', '김', '남녀', '이전', '하우스',
    '세운', '언덕', '기념관', '파쇄', '민', '화', '위로', '장관', '오후', '개별', '마리', '해양', '묘', '개방', 
    '샤워', '문화유산', '바닷가', '탁', '자체', '수육', '욕', '그늘', '유', '일부', '친환경', '데', '버섯', '장점', '축', '모래', 
    '침대', '트래킹', '백숙', '육회', '전쟁', '기점', '백제', '국립', '갈치', '브랜드', '중수', '세로', '조림', '라테', 
    '보기', '가량', '가옥', '발굴', '숙성'
    )


city_town_list = (
    ('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('1', '6'), ('1', '7'), 
    ('1', '8'), ('1', '31'), ('1', '32'), ('1', '33'), ('1', '34'), ('1', '35'), ('1', '36'), 
    ('1', '37'), ('1', '38'), ('2', '1'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), 
    ('2', '6'), ('2', '7'), ('2', '31'), ('2', '32'), ('2', '33'), ('2', '34'), ('2', '35'), 
    ('2', '36'), ('2', '37'), ('2', '38'), ('3', '1'), ('3', '2'), ('3', '3'), ('3', '4'), 
    ('3', '5'), ('3', '6'), ('3', '7'), ('3', '31'), ('3', '32'), ('3', '33'), ('3', '34'), 
    ('3', '35'), ('3', '36'), ('3', '37'), ('3', '38'), ('3', '39'), ('4', '1'), ('4', '2'), 
    ('4', '3'), ('4', '4'), ('4', '5'), ('4', '6'), ('4', '7'), ('4', '31'), ('4', '32'), 
    ('4', '33'), ('4', '34'), ('4', '35'), ('4', '36'), ('4', '37'), ('4', '38'), ('4', '39'), 
    ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4'), ('5', '5'), ('5', '6'), ('5', '7'), 
    ('5', '31'), ('5', '32'), ('5', '33'), ('5', '34'), ('5', '35'), ('5', '36'), ('5', '37'), 
    ('5', '38'), ('6', '1'), ('6', '2'), ('6', '4'), ('6', '6'), ('6', '31'), ('6', '32'), 
    ('6', '33'), ('6', '34'), ('6', '35'), ('6', '36'), ('6', '37'), ('6', '38'), ('7', '1'), 
    ('7', '2'), ('7', '4'), ('7', '6'), ('7', '31'), ('7', '32'), ('7', '33'), ('7', '34'), 
    ('7', '35'), ('7', '36'), ('7', '37'), ('7', '38'), ('8', '1'), ('8', '2'), ('8', '4'), 
    ('8', '6'), ('8', '31'), ('8', '32'), ('8', '33'), ('8', '34'), ('8', '35'), ('8', '36'), 
    ('8', '37'), ('8', '38'), ('9', '1'), ('9', '2'), ('9', '6'), ('9', '31'), ('9', '32'), 
    ('9', '33'), ('9', '34'), ('9', '35'), ('9', '36'), ('9', '37'), ('9', '38'), ('10', '1'), 
    ('10', '2'), ('10', '6'), ('10', '31'), ('10', '32'), ('10', '33'), ('10', '35'), ('10', '36'), 
    ('10', '37'), ('10', '38'), ('11', '1'), ('11', '6'), ('11', '31'), ('11', '32'), ('11', '33'), 
    ('11', '34'), ('11', '35'), ('11', '37'), ('11', '38'), ('12', '1'), ('12', '6'), ('12', '31'), 
    ('12', '32'), ('12', '33'), ('12', '34'), ('12', '35'), ('12', '36'), ('12', '37'), ('12', '38'), 
    ('13', '1'), ('13', '6'), ('13', '31'), ('13', '32'), ('13', '34'), ('13', '35'), ('13', '36'), 
    ('13', '37'), ('13', '38'), ('14', '1'), ('14', '6'), ('14', '31'), ('14', '32'), ('14', '34'), 
    ('14', '35'), ('14', '36'), ('14', '37'), ('15', '1'), ('15', '6'), ('15', '31'), ('15', '32'), 
    ('15', '34'), ('15', '35'), ('15', '36'), ('16', '1'), ('16', '6'), ('16', '31'), ('16', '32'), 
    ('16', '34'), ('16', '35'), ('16', '36'), ('16', '38'), ('17', '1'), ('17', '31'), ('17', '32'), 
    ('17', '35'), ('17', '36'), ('17', '38'), ('18', '1'), ('18', '31'), ('18', '32'), ('18', '35'), 
    ('18', '36'), ('18', '38'), ('19', '1'), ('19', '31'), ('19', '35'), ('19', '36'), ('19', '38'), 
    ('20', '1'), ('20', '31'), ('20', '35'), ('20', '36'), ('20', '38'), ('21', '1'), ('21', '31'), 
    ('21', '35'), ('21', '36'), ('21', '38'), ('22', '1'), ('22', '31'), ('22', '35'), ('22', '38'), 
    ('23', '1'), ('23', '31'), ('23', '35'), ('23', '38'), ('24', '1'), ('24', '31'), ('24', '38'), 
    ('25', '1'), ('25', '31'), ('26', '31'), ('27', '31'), ('28', '31'), ('29', '31'), ('30', '31'), 
    ('31', '31')
)


cat2 = {
    'A0101': '자연', 'A0102': '자연', 'A0201': '역사', 'A0202': '휴양', 'A0203': '체험', 'A0204': '산업', 'A0205': '건축/조형물',
    'A0206': '문화시설', 'A0207': '축제', 'A0208': '공연/행사', 'C0112': '가족코스', 'C0113': '나홀로코스', 'C0114': '힐링코스', 
    'C0115': '도보코스', 'C0116': '캠핑코스', 'C0117': '맛코스',  'A0301': '레포츠', 'A0302': '육상','A0303': '수상',
    'A0304': '항공', 'A0305': '복합', 'B0201': '숙박', 'A0401': '쇼핑', 'A0502': '음식점'
}

cat3 = {
    'A01010100': '국립공원', 'A01010200': '도립공원', 'A01010300': '군립공원', 'A01010400': '산', 'A01010500': '자연생태관광지',
    'A01010600': '자연휴양림', 'A01010700': '수목원', 'A01010800': '폭포', 'A01010900': '계곡', 'A01011000': '약수터',
    'A01011100': '해안절경', 'A01011200': '해수욕장', 'A01011300': '섬', 'A01011400': '항구/포구', 'A01011600': '등대',
    'A01011700': '호수', 'A01011800': '강', 'A01011900': '동굴', 'A01020100': '희귀동.식물', 'A01020200': '기암괴석',
    'A02010100': '고궁', 'A02010200': '성','A02010300': '문', 'A02010400': '고택', 'A02010500': '생가', 'A02010600': '민속마을',
    'A02010700': '유적지/사적지', 'A02010800': '사찰', 'A02010900': '종교성지', 'A02011000': '안보관광', 'A02020200': '관광단지',
    'A02020300': '온천/욕장/스파', 'A02020400': '이색찜질방', 'A02020500': '헬스투어', 'A02020600': '테마공원', 'A02020700': '공원',
    'A02020800': '유람선/잠수함관광', 'A02030100': '농.산.어촌 체험', 'A02030200': '전통체험', 'A02030300': '산사체험',
    'A02030400': '이색체험', 'A02030600': '이색거리', 'A02040400': '발전소', 'A02040600': '식음료', 'A02040800': '',
    'A02040900': '전자-반도체', 'A02041000': '자동차', 'A02050100': '다리/대교', 'A02050200': '기념탑/기념비/전망대',
    'A02050300': '분수', 'A02050400': '동상', 'A02050500': '터널', 'A02050600': '유명건물','A02060100': '박물관',
    'A02060200': '기념관', 'A02060300': '전시관', 'A02060400': '컨벤션센터', 'A02060500': '미술관/화랑', 'A02060600': '공연장',
    'A02060700': '문화원',  'A02060800': '외국문화원', 'A02060900': '도서관', 'A02061000': '대형서점', 'A02061100': '문화전수시설',
    'A02061200': '영화관', 'A02061300': '어학당', 'A02061400': '학교', 'A02070100': '문화관광축제', 'A02070200': '일반축제',
    'A02080100': '전통공연', 'A02080200': '연극', 'A02080300': '뮤지컬', 'A02080400': '오페라', 'A02080500': '전시회',
    'A02080600': '박람회', 'A02080800': '무용', 'A02080900': '클래식음악회', 'A02081000': '대중콘서트', 'A02081100': '영화',
    'A02081200': '스포츠경기', 'A02081300': '기타행사', 'C01120001': '가족코스', 'C01130001': '나홀로코스', 'C01140001': '힐링코스',
    'C01150001': '도보코스', 'C01160001': '캠핑코스', 'C01170001': '맛코스', 'A03010200': '수상레포츠', 'A03010300': '항공레포츠',
    'A03020200': '수련시설', 'A03020300': '경기장', 'A03020400': '인라인(실내 인라인 포함)', 'A03020500': '자전거하이킹',
    'A03020600': '카트', 'A03020700': '골프', 'A03020800': '경마', 'A03020900': '경륜', 'A03021000': '카지노',
    'A03021100': '승마', 'A03021200': '스키/스노보드', 'A03021300': '스케이트', 'A03021400': '썰매장', 'A03021500': '수렵장',
    'A03021600': '사격장', 'A03021700': '야영장,오토캠핑장', 'A03021800': '암벽등반', 'A03022000': '서바이벌게임',
    'A03022100': 'ATV', 'A03022200': 'MTB', 'A03022300': '오프로드', 'A03022400': '번지점프', 'A03022600': '스키(보드) 렌탈샵',
    'A03022700': '트래킹', 'A03030100': '윈드서핑/제트스키', 'A03030200': '카약/카누', 'A03030300': '요트',
    'A03030400': '스노쿨링/스킨스쿠버다이빙', 'A03030500': '민물낚시', 'A03030600': '바다낚시', 'A03030700': '수영',
    'A03030800': '래프팅', 'A03040100': '스카이다이빙', 'A03040200': '초경량비행', 'A03040300': '헹글라이딩/패러글라이딩',
    'A03040400': '열기구', 'A03050100': '복합 레포츠', 'B02010100': '관광호텔', 'B02010500': '콘도미니엄', 'B02010600': '유스호스텔',
    'B02010700': '펜션', 'B02010900': '모텔', 'B02011000': '민박', 'B02011100': '게스트하우스', 'B02011200': '홈스테이',
    'B02011300': '서비스드레지던스', 'B02011600': '한옥', 'A04010100': '5일장', 'A04010200': '상설시장', 'A04010300': '백화점',
    'A04010400': '면세점', 'A04010500': '대형마트', 'A04010600': '전문매장/상가', 'A04010700': '공예/공방',
    'A04010900': '특산물판매점', 'A04011000': '사후면세점', 'A05020100': '한식', 'A05020200': '서양식',
    'A05020300': '일식', 'A05020400': '중식', 'A05020700': '이색음식점', 'A05020900': '카페/전통찻집', 'A05021000': '클럽'
}

keywords_list = ("체험", "공원", "한식", "마을", "공간", "문화", "카페", "산", "자연",
    "캠핑장", "계곡", "식당", "바다", "코스", "관광", "가족", "프로그램", "음식",
    "전시", "박물관", "요리", "펜션", "역사", "커피", "축제", "시장", "맛집",
    "야외", "사찰", "카페/전통찻집", "섬", "해수욕장", "어린이", "교육",
    "캠핑", "휴식", "예술", "정원", "행사", "풍경", "반려동물", "야영장", "오토캠핑장", 
    "해변", "생태", "경관", "공연","습지", "과학",
    "유적지/사적지", "여름", "산책", "낚시", "작품", "가을", "파크",
    "물놀이", "폭포", "탑", "강", "저수지", "호수", "문화재",
    "명소", "수영장", "볼거리", "해안", "전망대", "글램핑", "반려견", "디저트",
    "힐링", "봄", "야영장", "레스토랑", "양식", "서원",
    "놀이", "베이커리", "해산물", "중식", "잔디", "유물", "전망",
    "경험", "미술관", "식물", "도보", "공연장", "겨울", "뷰",
    "리조트", "파스타", "관람", "유적", "일반축제", "놀이터", "승마",
    "산림", "감성", "건강", "자전거", "미술", "별", "일식", "영화",
    "갤러리", "경치", "온천", "국립공원", "등대", "등산", "레저", "한정식", "불상",
    "수목원", "호텔", "낚시터", "게스트하우스", "민박", "상가",
    "쇼핑", "횟집", "이색체험", "자연생태관광지", "동굴", "석탑", "둘레길",
    "금강", "수상", "관찰", "스포츠","유원지", "와인",
    "이색", "휴양", "조형", "이벤트", "수산물", "상설시장", "탐방", "숲",
    "연꽃", "수련", "강변","노을", "야경", "힐링코스", "캠프","테마공원",
    "전통", "일몰", "공룡", "낭만", "경기장", "전통문화", "해변",
    "공예", "목장", "페스티벌", "오션", "천연기념물", "벽화", "나들이", 
    "한옥", "일출","산행", "미술관/화랑", "숙박시설", "관광지", "유적지", "식물원", "전시장"
)

cat_values = [
    '국립공원', '도립공원', '군립공원', '산', '자연생태관광지',
    '자연휴양림', '수목원', '폭포', '계곡', '약수터',
    '해안절경', '해수욕장', '섬', '항구/포구', '등대',
    '호수', '강', '동굴', '희귀동.식물', '기암괴석',
    '고궁', '성', '문', '고택', '생가', '민속마을',
    '유적지/사적지', '사찰', '종교성지', '안보관광', '관광단지',
    '온천/욕장/스파', '이색찜질방', '헬스투어', '테마공원', '공원',
    '유람선/잠수함관광', '농.산.어촌 체험', '전통체험', '산사체험',
    '이색체험', '이색거리', '발전소', '식음료', '', '전자-반도체',
    '자동차', '다리/대교', '기념탑/기념비/전망대', '분수', '동상',
    '터널', '유명건물', '박물관', '기념관', '전시관',
    '컨벤션센터', '미술관/화랑', '공연장', '문화원', '외국문화원',
    '도서관', '대형서점', '문화전수시설', '영화관', '어학당',
    '학교', '문화관광축제', '일반축제', '전통공연', '연극',
    '뮤지컬', '오페라', '전시회', '박람회', '무용',
    '클래식음악회', '대중콘서트', '영화', '스포츠경기', '기타행사',
    '가족코스', '나홀로코스', '힐링코스', '도보코스', '캠핑코스',
    '맛코스', '수상레포츠', '항공레포츠', '수련시설', '경기장',
    '인라인(실내 인라인 포함)', '자전거하이킹', '카트', '골프',
    '경마', '경륜', '카지노', '승마', '스키/스노보드',
    '스케이트', '썰매장', '수렵장', '사격장', '야영장,오토캠핑장',
    '암벽등반', '서바이벌게임', 'ATV', 'MTB', '오프로드',
    '번지점프', '스키(보드) 렌탈샵', '트래킹', '윈드서핑/제트스키',
    '카약/카누', '요트', '스노쿨링/스킨스쿠버다이빙', '민물낚시',
    '바다낚시', '수영', '래프팅', '스카이다이빙', '초경량비행',
    '헹글라이딩/패러글라이딩', '열기구', '복합 레포츠', '관광호텔',
    '콘도미니엄', '유스호스텔', '펜션', '모텔', '민박',
    '게스트하우스', '홈스테이', '서비스드레지던스', '한옥', '5일장',
    '상설시장', '백화점', '면세점', '대형마트', '전문매장/상가',
    '공예/공방', '특산물판매점', '사후면세점', '한식', '서양식',
    '일식', '중식', '이색음식점', '카페/전통찻집', '클럽'
]

union_values = (
    '공룡', '겨울', '숙박시설', '유적지', '동상', '승마', '어학당', '항공레포츠', '생가', '대형마트', '횟집',
    '서비스드레지던스', '맛코스', '힐링코스', '요리', '미술관/화랑', '상가', '수렵장', '자동차', '백화점', '자전거', 
    '사후면세점', '전통공연', '민속마을', '전시관', '수련', '인라인(실내 인라인 포함)', '레저', '이색찜질방', '해수욕장', 
    '오페라', '유적', '베이커리', '카트', '자연휴양림', '홈스테이', '식당', '스포츠경기', '경기장', '바다',  
    '미술관', '산책', '모텔', '국립공원', '유람선/잠수함관광', '유원지', '테마공원', '습지', '행사', '복합 레포츠',  
    '기념탑/기념비/전망대', '관찰', '이색', '강변', '고궁', '윈드서핑/제트스키', '헹글라이딩/패러글라이딩', '탐방', '등산', 
    '스케이트', '기암괴석', 'ATV', '석탑', '문화전수시설', '건강', '자연', '파스타', '오션', '봄', '어린이', '희귀동.식물', 
    '5일장', '공연장', '잔디', '관광지', '전망', '수상레포츠', '산행', '대중콘서트', '서원', '문화관광축제', '페스티벌', 
    '식음료', '축제', '디저트', '문화원', '카페', '파크', '폭포', '뷰', '기타행사', '경륜', '초경량비행', '조형', 
    '일몰', '열기구', '갤러리', '전통', '터널', '래프팅', '공원', '오프로드', '불상', '카약/카누', '이벤트', '발전소', '산림', 
    '이색거리', '경험', '둘레길', '나들이', '전시회', '산사체험', '유적지/사적지', '뮤지컬', '음식', '반려견', '반려동물', 
    '스키(보드) 렌탈샵', '트래킹', '리조트', '쇼핑', '안보관광', '해안', '볼거리', '자연생태관광지', '관광', '연극', '체험', 
    '경치', '공간', '식물원', '교육', '무용', '전통체험', '정원', '수영', '이색음식점', '카지노', '해변', '양식', '레스토랑', 
    '스키/스노보드', '관람', '작품', '군립공원', '헬스투어', '휴식', '물놀이', '마을', '맛집', '캠프', '전문매장/상가', 
    '서바이벌게임', '도보코스', '호수', '경마', '전통문화', '여름', '낚시', '수산물', '관광단지', '썰매장', '휴양', '카페/전통찻집', 
    '한정식', '농.산.어촌 체험', '한옥', '예술', '낭만', '다리/대교', '도서관', '수련시설', '한식', '자전거하이킹', '번지점프', 
    '일식', '사찰', '천연기념물', '전시', '낚시터', '나홀로코스', '항구/포구', '연꽃', '스노쿨링/스킨스쿠버다이빙', '면세점', '야경', 
    '가을', '게스트하우스', '컨벤션센터', '와인', '계곡', '명소', '유스호스텔', '놀이', '클래식음악회', '박물관', '유명건물', '수상', 
    '동굴', '수목원', '일반축제', '스카이다이빙', '암벽등반', '요트', '해안절경', '특산물판매점', '약수터', '사격장', '전시장', 
    '콘도미니엄', '식물', '노을', '목장', 'MTB', '놀이터', '공예/공방', '펜션', '감성', '경관', 
    '온천', '전망대', '도립공원', '힐링', '민물낚시', '골프', '해산물', '고택', '일출', '온천/욕장/스파', '대형서점', '바다낚시', 
    '민박',  '코스', '문화', '상설시장', '공예', '박람회', '역사', '문화재', '가족', '호텔', '벽화', '클럽', '저수지', 
    '기념관', '등대', '공연', '스포츠', '과학', '야영장',  '서양식', '외국문화원', '탑', '도보',
    '이색체험', '중식', '유물', '별', '전자-반도체', '풍경', '분수', '글램핑', '영화', '프로그램', '미술', '생태', '캠핑', 
    '종교성지', '관광호텔', '숲', '가족코스', '시장', '커피')