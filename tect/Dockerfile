FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev \
    build-essential libssl-dev libffi-dev python3-setuptools \
    python3-venv mongodb-clients bash-completion \
    && apt-get install libmysqlclient-dev -y

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# secret key 추가 
ENV TECT_SECRET_KEY 

RUN python3.8 -m venv env
RUN /bin/bash -c "source env/bin/activate"

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

