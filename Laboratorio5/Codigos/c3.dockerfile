FROM ubuntu:18.10

RUN sed -i 's/archive/old-releases/g' /etc/apt/sources.list \
    &&  sed -i  's|http://security.ubuntu.com/ubuntu|http://old-releases.ubuntu.com/|g' /etc/apt/sources.list
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends openssh-server\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]