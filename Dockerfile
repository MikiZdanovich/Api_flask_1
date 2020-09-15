FROM python:3.8-slim

MAINTAINER MikiZdanovich

WORKDIR /api
EXPOSE 5000
ENV FLASK_ENV='development'
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements/
RUN pip install -r ./requirements/requirements.txt

ADD ./backend ./backend
ADD ./manage.py ./manage.py


CMD python manage.py run