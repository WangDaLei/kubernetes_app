FROM ubuntu

RUN apt-get update
RUN apt-get install -y mysql-server-5.7

ADD entrypoint.sh /root/
EXPOSE 3306

CMD []
ENTRYPOINT ["/root/entrypoint.sh"]

