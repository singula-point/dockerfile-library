FROM ubuntu:16.04

LABEL maintainer Li Jiangjin(lijj@singula-poing.com)

ARG ZENTAO_URL=http://dl.cnezsoft.com/zentao/9.8.3/ZenTaoPMS.9.8.3.zbox_64.tar.gz

RUN apt-get update && apt-get install -y wget php-ldap \
    --no-install-recommends && rm -r /var/lib/apt/lists/*

RUN wget ${ZENTAO_URL} -O zbox.tar.gz && mv zbox.tar.gz /tmp 

RUN apt-get remove -y wget  && rm -rf /var/lib/apt/lists/*

COPY docker-entrypoint /usr/local/bin/docker-entrypoint

RUN chmod +x           /usr/local/bin/docker-entrypoint

EXPOSE 80 3306
# for chinese input
ENV LANG C.UTF-8 
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
ENTRYPOINT ["docker-entrypoint"]
