FROM python:3.9

RUN pip install mysql-connector-python
RUN pip install flask
RUN pip install -U flask-cors
RUN pip install requests
RUN pip install requests-futures

WORKDIR /usr/app/src

COPY api.py ./

COPY  ./src/controller/controller.py ./ 
COPY  ./src/model/model.py ./ 
