FROM python:3.12.2

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ./docker-entrypoint
