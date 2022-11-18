FROM python:3.7.2

WORKDIR /usr/src/app
ENV FLASK_APP=app
ENV MECABRC=/etc/mecabrc

COPY /app/requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# MeCabをインストール
RUN apt-get update -qq && apt-get install -y mecab
