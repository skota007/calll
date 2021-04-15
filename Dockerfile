FROM python:3
WORKDIR /usr/src/app
ADD trebuie.txt /usr/src/app
RUN pip install -r trebuie.txt
ADD . /usr/src/app