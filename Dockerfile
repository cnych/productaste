FROM python:3.6.4

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

EXPOSE 8004

CMD [ "/bin/sh", "start_server.sh" ]
