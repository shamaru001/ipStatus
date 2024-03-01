FROM python:3.12.2

ADD . /code

WORKDIR /code

RUN apt update 
RUN apt upgrade -y
RUN apt install iputils-ping -y

RUN pip install -r requirements.txt

CMD ./docker-entrypoint
