FROM python:3.8

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./main.py main.py
COPY ./business_objects/ business_objects/
COPY ./dao/ dao/
COPY ./database/database.py database/database.py
COPY ./service/ service/

EXPOSE 8000