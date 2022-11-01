## 📎 목차

1. [Service](#-service)
2. [개발 기간](#-개발-기간)
3. [개발 인원](#-개발-인원)
4. [목적 및 구현사항](#-목적-및-구현사항)
5. [기술 스택](#-기술-스택)
6. [구조](#-구조)
7. [Docker compose](#-docker-compose)
8. [AWS Lambda/SQS](#-aws-lambda/sqs)

## 🚀 Service
-  접속자 IP 주소를 반환하는 사이트

## 📆 개발 기간
-  2022.07.18 ~ 2022.08.02(16일)

## 🧑🏻‍💻 개발 인원(1명)
- 박민하

## 📝 목적 및 구현사항
- 트래픽을 효과적으로 관리할 수 있는 방안 모색
1. Docker Compose
- Django, postgreSQL 사용
- 사용자 IP정보 저장/조회 API(POST)
2. AWS Lambda/SQS
- 사용자 IP정보 저장/조회 API(POST/GET)
- Lambda에서 SQS로 메세지 전송
- SQS와 dynamoDB 연결

## 🛠 기술 스택
Language | Framework | Database | Infra | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/dynamoDB-4053D6?style=for-the-badge&logo=Amazon DynamoDB&logoColor=white">  | <img src="https://img.shields.io/badge/lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white"> </br> <img src="https://img.shields.io/badge/sqs-FF4F8B?style=for-the-badge&logo=amazonsqs&logoColor=white"> </br> <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">

## 📚 구조
![](https://velog.velcdn.com/images/miracle-21/post/4a86342a-f24e-4662-bc17-8180aff6c8c0/image.png)


##  🤜 Docker compose
![](https://velog.velcdn.com/images/miracle-21/post/54672e40-60a8-4b34-8a06-4a3b79e70686/image.png)

- 결과: 동시 접속자가 많을 경우 성능 저하 및 데이터 소실 
- 해결 방안: SQS를 이용한 dynamoDB bulk insert 시도

##  🤜 AWS Lambda/SQS
![](https://velog.velcdn.com/images/miracle-21/post/e835fc32-0e39-4691-a915-7f5f781d1576/image.png)


- 결과: 총 60개의 데이터가 저장되어야 하지만 20개의 데이터만 저장.