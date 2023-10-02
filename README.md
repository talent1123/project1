# Project1

# 공공자전거 데이터를 활용한 불편사항 분석

## Why?

공공자전거 이용 시 빈번하게 일어나는 불편사항을 분석 , 시각화하여 개선하
여, 자전거 이용률을 증가시켜 저탄소 녹색성장 실현과 이동 편리성 증진 실
현을 기대할 수 있다.

## 특징

공공자전거 데이터를 이용하여 Numpy, Pandas를 이용하여 불편사항 분석, 이후 Matplolib,Folium등 다양한 시각화 라이브러리를 사용하여 분석 데이터
를 시각화하고, 대시보드 형태로 사이트 제작, 분석별 데이터를 카테고리 화 
하여 정보 제공 및 앱 다운로드, 인스타 등 각종 링크 기능 구현

## Team
Leard: 포트폴리오 작성 & 구군별 대여소 분포 데이터 수집, 분석, 시각화

Member1: Django 서비스 개발 & 기간별 고장 발생사유와 횟수 데이터 수집, 분석

Member2: 이동거리, 이동시간, 성별, 나이대 데이터 수집, 분석, 시각화

Member3:기획안 작성 & 시간별 이용 용도, 대여-반납처 데이터 수집, 분석, 시각화

Member4(ME): Django 서비스 개발 & 지역별 대여현황 데이터 수집, 분석, 시각화 & 발표


## 분석자료 명세

원본 분석데이터 내역

- [공공자전거 고장신고 내역(CSV)](https://data.seoul.go.kr/dataList/OA-15644/F/1/datasetView.do)
- [서울시 공공자전거 대여소정보(6월기준.CSV)](http://data.seoul.go.kr/dataList/OA-13252/F/1/datasetView.do)
- [서울시 공공자전거 대여소별 이용정보(월별)(1~6월.CSV)](https://data.seoul.go.kr/dataList/OA-15249/F/1/datasetView.do)
- [서울시 공공자전거 이용정보(월별)(1~6월.CSV)](http://data.seoul.go.kr/dataList/OA-15248/F/1/datasetView.do)
- [서울시 공공자전거 대여이력정보(1~6월.CSV)](http://data.seoul.go.kr/dataList/OA-15182/F/1/datasetView.do)

이용 분석데이터 내역

- 고장신고 내역 : 자전거번호, 등록일시, 고장구분
- 대여소 정보 : 대여소번호, 대여건수, 자치구, 거치대수,위도,경도,상세주소,보관소명
- 대여소별 이용정보 : 대여소 그룹, 대여 건수
- 이용정보(월별) : 대여일자,대여소번호,대여구분,성별,연령대코드,이용건수,이동거리,이용시간
- 대여이력 정보 : 대여일시, 대여 대여소번호, 반납일시, 반납 대여소번호

## 개발 언어 & 라이브러리

데이터 분석 & 시각화

- Matplotlib 3.6.0

- Numpy 1.23.4

- Folium 0.12.1

- Pandas 1.5.0

- Plotly 5.10.0

- Seaborn 0.12.1

- WordCloud 1.8.2.2

서비스개발

- Django 4.1.2
- jQuery 3.6.1 min
- HTML
- Css

언어

- Python 3.9
- JavaScript(서비스개발)


