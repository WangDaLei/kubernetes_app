FROM ubuntu

RUN apt-get update
RUN apt-get install -y make git mysql-client mysql-common mysql-client-core-5.7 net-tools wget vim libmysqld-dev libmysqlclient-dev gcc libssl-dev supervisor fish
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN wget "https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh"
RUN bash Anaconda3-5.2.0-Linux-x86_64.sh -b
RUN rm -rf Anaconda3-5.2.0-Linux-x86_64.sh
RUN git clone "https://github.com/WangDaLei/kubernetes_app.git"
RUN export PATH=/root/anaconda3/bin:$PATH && cd /kubernetes_app  && pip install -r requirements.txt

ADD entrypoint.sh /
EXPOSE 8000

CMD []
ENTRYPOINT ["/entrypoint.sh"]

