# 프로젝트3 : 탄자니아 수자원 현황 예측 웹 서비스 배포

# 1. Overview

## 1.1. 배경과 목적
- 다수의 아프리카 국가들이 처해 있는 물부족 및 오염 문제를 해결하기 위해 마을 곳곳에 설치된 우물(수자원)
- 우물은 유지보수가 굉장히 중요한데, 소홀한 관리로 물이 오염되거나 수원이 막히는 경우 마을 주민들의 생활과 생존에 큰 피해가 발생함
- 아프리카의 한정된 인적, 물적 자원으로 지역사회 생명의 역할을 하는 우물을 보다 효율적으로 관리할 수 있는 웹 서비스 배포

## 1.2. 데이터 소개
- 탄자니아 수자원부의 데이터를 집계하는 Taarifa waterpoints 대시보드 출처 데이터셋
- 설치 주체, 설치 자금, 관리 주체, 위치, 수자원의 유형과 품질 등 수자원 관리와 관련된 정보
- 총 23개 컬럼 59,400개 행으로 이루어진 데이터

### Columns Description
- id : 해당 우물에 부여된 id
- funder : 자금 제공자
- gps_height : 우물의 고도
- installer : 우물을 설치한 기관
- longitude : GPS 좌표
- latitude : GPS 좌표
- basin : 지리적 유역
- region : 지리적 위치
- lga : 지리적 위치
- ward : 지리적 위치
- amount_tsh : 우물 설치에 소요된 자금 (탄자니아 화폐단위)
- construction_year : 워터포인트가 건설된 연도
- extraction_type : 워터포인트가 사용하는 추출의 종류
- source_type : 물의 근원
- waterpoint_type_group : 워터포인트의 종류
- management : 워터포인트 관리 방법
- payment_type : 물 비용
- quality : 물의 품질
- quantity : 물의 양
- waterpoint_type : 워터포인트의 종류
- population : 우물 주변의 인구
- public_meeting : 미팅 여부
- status : 워터포인트(우물)의 작동여부, 수리 필요 여부 (target)

## 1.3. 스킬셋
- sqlite
- metabase
- pickle
- flask
- heroku



---
<br/>

# 2. 파이프라인  
![image](https://user-images.githubusercontent.com/110115061/223961263-d52e88ff-161f-4a11-a4cf-b318c474021b.png)  
- csv파일 형태의 데이터 sqlite로 저장
- 머신러닝 모델링, 메타베이스로 대쉬보드 생성
- ML모델 피클링, 대쉬보드 플라스크로 연결
- heroku를 통한 웹서비스



---
<br/>

# 3. 데이터 적재, 모델링 
## 3.1. 데이터 적재
![image](https://user-images.githubusercontent.com/110115061/223961605-71904780-7ee0-43db-a5b8-25a42e77f63e.png)  
- 우물의 지리적 위치 정보와 모델링에 사용되는 정보를 나누어 sqlite에 저장

# 4. 웹 서비스 배포  
- https://waterpointtt.herokuapp.com/
- 대시보드  
![image](https://user-images.githubusercontent.com/110115061/223963533-77fd1839-2d35-4174-acf2-65412fa9e256.png)  
- 수자원 상태 예측 모델  
![image](https://user-images.githubusercontent.com/110115061/223964786-a23a616f-b66a-4116-98b6-f50e62d0c57b.png)



---
<br/>

# 5. 한계 및 개선점
- 기존 LightGBM 모델의 설치 오류로 피클링 실패, ML모델 재구성함
  - ML 모델 개선을 통해 성능은 높이고 효율은 올리는 방법을 찾을 필요가 있음
- metabase이 외의 다른 데이터 분석 툴을 활용하여 다양한 기능을 추가하는 것 필요함
- 
