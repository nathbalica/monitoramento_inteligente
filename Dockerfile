FROM python:3.10.0-alpine 

USER root

RUN mkdir mqtt
WORKDIR /mqtt

ENV PYTHONUNBUFFERED 1

ADD requirements.txt /mqtt/
RUN pip install -r requirements.txt

ADD . /mqtt/

RUN chown -R nathdev:nathdev /mqtt
USER echo nathdev

WORKDIR /mqtt

RUN set POSTGRES_HOST at 127.0.0.1
# CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]