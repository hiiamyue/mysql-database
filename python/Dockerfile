FROM python:3.9

RUN pip install mysql-connector-python

RUN pip install flask

WORKDIR /usr/app/src

COPY api.py ./

COPY  ./src/controller/controller.py ./ 
COPY  ./src/model/model.py ./ 
