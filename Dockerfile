FROM ubuntu:latest
# FROM python:3.8
RUN apt-get update
# pythonとpipをインストール
RUN apt-get install -y python3 python3-pip

# MeCabをインストール
RUN apt-get -y install mecab
# PATHを通す
RUN export MECABRC = '/etc/mecabrc'

WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY /app/requirements.txt ./

RUN pip3 install -r requirements.txt