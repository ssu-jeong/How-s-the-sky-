# How Is The Sky

### 프로젝트 배경

<img width="873" alt="image" src="https://user-images.githubusercontent.com/86764734/177376515-196ef218-8930-4899-8a36-0f999159f99e.png">

- 대기오염으로 인해 일상생활에 피해를 입을 수 있게 되면서 날씨와 함께 미세먼지 오존수치에 대한 정보를 쉽게 확인해볼 수 있게 되었다. 제공해주는 정보는 두가지뿐이지만 대기 측정항목들이 더 있다는 것을 알고 있었고, 많은 사람들이 대기오염에 대한 경각심가질 수 있는 웹서비스를 제공하고 싶다는 생각이 들었다.

- 우리가 보통 제공되고 있는 대기 정보는 미세먼지와 오존수치이다.
- 이와 더불어 각 지역구 대기 측정시스템에서 측정되고 있는 대기항목들이 더 존재한다.
    - SO2, NO2, CO, O3, PM2.5 PM10
- 우리가 쉽게 알 수 있는 미세먼지와 오존에 대한 수치 정보외에 함께 측정되고 있는 다른 대기측정 항목들에 대한 정보 공유와 기준정보를 제공할 수 있게 하기 위함.

### 프로젝트 목표

---

- 대기오염에 대한 정보제공과 측정 항목들의 값을 표준화하여 모델링을 진행하여 측정항목의 수치를 입력하면 종합적으로 대기의 상태를 나타내주는 웹 서비스 구축

### 사용프로그램

---

- HTML5 : 홈페이지 프레임 제작 (수치입력, 결과확인 페이지)
- CSS3 : 구성요소 디자인
- Python (Flask) : 서버 연결 (Django보다 좀 더 가벼운 Flask 사용)
- PosrgreSQL : psycopg2라이브러리를 사용하여 웹과 DB를 연동
- 최종 배포는 heroku를 사용

### 서비스 구성 및 제작 과정

---

**데이터 수집 : 대기측정항목, 대기상태**

- 공공데이터포털을 통해 open api와 .csv파일 다운
    - Measurement_info.csv (3,885,068행)
    
    <img width="591" alt="스크린샷 2022-07-06 오전 2 31 00" src="https://user-images.githubusercontent.com/86764734/177390443-1ad5daf0-7b53-460a-b3b1-d44a42cd2cd1.png">
    
    - Measurement_item_info.csv (7행)
    
    <img width="829" alt="스크린샷 2022-07-06 오전 2 27 45" src="https://user-images.githubusercontent.com/86764734/177390479-e67c7294-e6f8-49c4-802d-6bf8fd1b9330.png">
    
    - Measurement_station_info (26행)
    
    <img width="605" alt="스크린샷 2022-07-06 오전 2 32 08" src="https://user-images.githubusercontent.com/86764734/177390493-14a73124-d223-4c32-bfc4-27ea37c9f9de.png">

**데이터 분석**

- 결측치 확인 및 특성공학
    - Measurement_item_info.csv 파일의 수치를 기준으로하여 컬럼 추가
    
    ```py
    # converting 'SO2' value in their standard
    def measure(x):
    if x<=0.02:
        return 'good'
    elif 0.02<x<=0.05:
        return 'normal'
    elif 0.05<x<=0.15:
        return 'bad'
    else:
        return 'very bad'
    
    SO2_measure=list(map(measure,req_data['SO2']))
    ```
    
    - 주의보 발령 정보를 확인할 수 있는 O3, PM10, PM2.5 항목을 제외하곤 ‘Nomal’수치를 기준으로 나눔
    
    ```py
    #'SO2' 주의보 발령은 '1', 주의보 발령 아닐 경우 '0' 반환받아 'SO2_bad'컬럼 추가
    lst = []
    for i in req_data['SO2']:
        if i > 0.05:
            lst.append(1)
        else:
        l   st.append(0)

    test_df = pd.DataFrame(lst)
    req_data['SO2_bad'] = test_df
    
    ```
    
- target 설정

```py
# 위에서 만들어준 bad컬럼값을 모두 더해준 뒤 아래 조건을 주어 '1' 또는 '0' 반환

req_data['total_bad'] = req_data['SO2_bad'] + req_data['NO2_bad'] + req_data['O3_bad'] + req_data['CO_bad'] + req_data['PM10_bad'] + req_data['PM2.5_bad']

lst =[]
for i in req_data['total_bad']:
    if i == 4:
        lst.append(1)

    else:
        lst.append(0)
```

- 전처리 진행한 데이터를 훈련/검증 데이터로 나눠 모델링진행
    - 사용한 모델: RandomForestClassifier
    - Pickle을 통해 머신러닝 모델 Flask 프레임워크에 서빙

**검색 페이지** : 사용자가 검색수치를 입력하고 결과를 볼 수 있는 페이지

- 각 항목별 값을 입력할 수 있는 폼 표시
- 결과 버튼을 누르면 입력 수치를 기반으로하여 현재 대기상태 반환

**웹과 DB 연동하기**

- psycopg2라이브러리를 사용하여 웹과 DB를 연동
- 관계형 데이터베이스인 PostgreSQL에 저장

**서버를 통해 배포**

- 본격적으로 heroku를 통해 배포

**대시보드** : 구글 데이터스튜디오

- 구글 데이터스튜디오를 이용하여 대시보드 제작
- 배포된 웹 어플리케이션에서도 대시보드를 열람할 수 있도록 페이지를 구성

### 결과

---

- 기본페이지

<img width="1497" alt="스크린샷 2022-07-06 오전 2 55 07" src="https://user-images.githubusercontent.com/86764734/177392280-34c33bf7-f57a-44da-a34a-fb309301a46e.png">

- 검색폼
<img width="1483" alt="스크린샷 2022-07-06 오전 2 55 20" src="https://user-images.githubusercontent.com/86764734/177391551-4c34f6a9-434a-4ae1-80a6-bc778b4fdb02.png">

- 결과페이지
<img width="1498" alt="스크린샷 2022-07-06 오전 2 55 51" src="https://user-images.githubusercontent.com/86764734/177391568-4b182266-2b7f-46ce-9263-e6b61ac55b93.png">

- 대시보드
<img width="1382" alt="스크린샷 2022-07-06 오전 2 58 42" src="https://user-images.githubusercontent.com/86764734/177391587-1666e5fc-3b61-4f16-8956-18c7626169fe.png">

<img width="1312" alt="스크린샷 2022-07-06 오전 2 58 57" src="https://user-images.githubusercontent.com/86764734/177391595-6596fff4-c5fe-4a2b-9a31-12c192aa5d2f.png">

- 측정 항목들의 값을 표준화하여 총 대기환경을 점수로 내었을 때, 현재 오존, 미세먼지 각각의 수치를 통해 제공되는 경보 횟수보다 좀 더 많은 경보빈도를 나타냄. → 대기오염에 대한 경각심을 심어줄 수 있을 것이라 생각.

### 추후 발전 과제

---

- 모델성능향상
    - 이번 프로젝트는 웹서비스에 초점을 두고 진행을 하다보니 모델성능에 초점을 맞추지 못했음.
    - 모델의 성능이 높지 않아 정확한 결과라고 보기 어려운 부분도 있어 모델 성능을 높여 좀 더 정확한 결과값 제공할 수 있도록
- CSS tnwjd
    - 결과 출력시 화면이 하단에 치우쳐있어서 시각적으로 불편한 부분이 있어 추후 수정
- 부트스트랩
    - 부트스트랩을 적용해보려 했으나 처음하는 작업이다 보니 시간내 적용하기 쉽지 않았기 때문에 다시 시도하여 좀 더 완성도 있는 웹으로 수정
