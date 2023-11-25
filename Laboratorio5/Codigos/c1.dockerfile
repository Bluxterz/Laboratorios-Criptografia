FROM ubuntu:14.10

RUN sed -i 's/archive/old-releases/g' /etc/apt/sources.list \
    &&  sed -i  's|http://security.ubuntu.com/ubuntu|http://old-releases.ubuntu.com/ubuntu|g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
