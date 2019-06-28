FROM ubuntu:18.04
MAINTAINER "gaurav.s@hotstar.com"

RUN apt-get update
RUN apt-get install -y python3-dev python3-pip

COPY . /hackathon

WORKDIR /hackathon

RUN pip3 install -r requirements.txt

ENV FLASK_APP /hackathon/app.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENTRYPOINT flask run