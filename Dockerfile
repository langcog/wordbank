FROM python:3.8-bullseye

COPY . /app

WORKDIR /app
RUN apt-get -y update
RUN apt-get install gettext -y

RUN pip install -r ./requirements.txt

