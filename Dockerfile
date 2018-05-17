FROM python:3.6.4

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt


CMD [ "/bin/sh", "start_server.sh" ]
