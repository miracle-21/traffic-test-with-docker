## ๐ ๋ชฉ์ฐจ

1. [Service](#-service)
2. [๊ฐ๋ฐ ๊ธฐ๊ฐ](#-๊ฐ๋ฐ-๊ธฐ๊ฐ)
3. [๊ฐ๋ฐ ์ธ์](#-๊ฐ๋ฐ-์ธ์)
4. [๋ชฉ์  ๋ฐ ๊ตฌํ์ฌํญ](#-๋ชฉ์ -๋ฐ-๊ตฌํ์ฌํญ)
5. [๊ธฐ์  ์คํ](#-๊ธฐ์ -์คํ)
6. [๊ตฌ์กฐ](#-๊ตฌ์กฐ)
7. [Docker compose](#-docker-compose)
8. [AWS Lambda/SQS](#-aws-lambda/sqs)

## ๐ Service
- ย ์ ์์ IP ์ฃผ์๋ฅผ ๋ฐํํ๋ ์ฌ์ดํธ

## ๐ ๊ฐ๋ฐ ๊ธฐ๊ฐ
- ย 2022.07.18 ~ 2022.08.02(16์ผ)

## ๐ง๐ปโ๐ป ๊ฐ๋ฐ ์ธ์(1๋ช)
- ๋ฐ๋ฏผํ

## ๐ ๋ชฉ์  ๋ฐ ๊ตฌํ์ฌํญ
- ํธ๋ํฝ์ ํจ๊ณผ์ ์ผ๋ก ๊ด๋ฆฌํ  ์ ์๋ ๋ฐฉ์ ๋ชจ์
1. Docker Compose
- Django, postgreSQL ์ฌ์ฉ
- ์ฌ์ฉ์ IP์ ๋ณด ์ ์ฅ/์กฐํ API(POST)
2. AWS Lambda/SQS
- ์ฌ์ฉ์ IP์ ๋ณด ์ ์ฅ/์กฐํ API(POST/GET)
- Lambda์์ SQS๋ก ๋ฉ์ธ์ง ์ ์ก
- SQS์ dynamoDB ์ฐ๊ฒฐ

## ๐  ๊ธฐ์  ์คํ
Language | Framework | Database | Infra | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/dynamoDB-4053D6?style=for-the-badge&logo=Amazon DynamoDB&logoColor=white">  | <img src="https://img.shields.io/badge/lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white"> </br> <img src="https://img.shields.io/badge/sqs-FF4F8B?style=for-the-badge&logo=amazonsqs&logoColor=white"> </br> <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">

## ๐ ๊ตฌ์กฐ
![](https://velog.velcdn.com/images/miracle-21/post/4a86342a-f24e-4662-bc17-8180aff6c8c0/image.png)


##  ๐ค Docker compose
![](https://velog.velcdn.com/images/miracle-21/post/54672e40-60a8-4b34-8a06-4a3b79e70686/image.png)

- ๊ฒฐ๊ณผ: ๋์ ์ ์์๊ฐ ๋ง์ ๊ฒฝ์ฐ ์ฑ๋ฅ ์ ํ ๋ฐ ๋ฐ์ดํฐ ์์คย 
- ํด๊ฒฐ ๋ฐฉ์: SQS๋ฅผ ์ด์ฉํ dynamoDB bulk insert ์๋

##  ๐ค AWS Lambda/SQS
![](https://velog.velcdn.com/images/miracle-21/post/e835fc32-0e39-4691-a915-7f5f781d1576/image.png)


- ๊ฒฐ๊ณผ: ์ด 60๊ฐ์ ๋ฐ์ดํฐ๊ฐ ์ ์ฅ๋์ด์ผ ํ์ง๋ง 20๊ฐ์ ๋ฐ์ดํฐ๋ง ์ ์ฅ.