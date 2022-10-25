FROM python:3.10.0-alpine 

USER root

RUN mkdir mqtt
WORKDIR /mqtt

ENV PYTHONUNBUFFERED 1

ADD requirements.txt /mqtt/
RUN pip install -r requirements.txt

ADD . /mqtt/

# RUN chown -R "$USER:$USER" /mqtt
# USER echo "$USER"

WORKDIR /mqtt