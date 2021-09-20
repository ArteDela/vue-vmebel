FROM python:3.8

WORKDIR /usr/src/app

RUN apt-get -y update --fix-missing
RUN apt-get -y install --fix-missing nano
RUN pip3.8 install --no-cache-dir mysqlclient flask==1.1.2 flask-RESTful flask-SQLAlchemy flask-cors pytest requests

VOLUME /usr/src/app

EXPOSE 5000

CMD [ "python3", "./main.py" ]
