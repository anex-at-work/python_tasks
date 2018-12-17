FROM python:3.7
LABEL maintainer="anex.work@gmail.com"
SHELL ["/bin/bash", "-c"]

RUN apt update && \
  apt install -y supervisor && \
  mkdir -p /var/log/supervisor && \
  mkdir /home/src
  
COPY ./src /home/src

RUN cd /home/src && pip install -r requirements.txt

ADD ./assets/supervisor.conf /etc/supervisor.conf
CMD ["supervisord", "-c", "/etc/supervisor.conf"]
WORKDIR /home/src
VOLUME /home/src
