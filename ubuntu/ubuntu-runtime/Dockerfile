FROM ubuntu:16.04

LABEL maintainer Li Jiangjin(lijj@singula-point.com)

RUN apt-get update || true && \
    apt-get install -y \
    inetutils-ping && \
    rm -rf /var/lib/dpkg/info/* /var/lib/apt/lists/* \
    /var/log/*.log /root/.cache

# change timezone
COPY Shanghai /etc/localtime

# change locale
# for chinese input
ENV LANG C.UTF-8 
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

CMD ["bash"]

