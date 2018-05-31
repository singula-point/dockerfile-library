#基础镜像为ubuntu:16.04
FROM ubuntu:16.04
#作者信息
MAINTAINER hexu:redis
#设置环境变量
ENV REDIS_VERSION 4.0.2
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-4.0.2.tar.gz
ENV REDIS_DOWNLOAD_SHA b1a0915dbc91b979d06df1977fe594c3fa9b189f1f3d38743a2948c9f7634813
ENV LIBEVENT_VERSION 4.0.2
#安装相关软件
RUN apt-get update;\
    apt-get install software-properties-common -y;\
    apt-get install wget -y;\
    add-apt-repository ppa:ubuntu-desktop/ubuntu-make;\
    apt-get update;\
    apt-get install ubuntu-make -y;\
    apt-get install build-essential -y;\
        apt-get clean;\
        rm -rf /var/lib/apt/lists/*
#下载redis
RUN wget -O redis.tar.gz "$REDIS_DOWNLOAD_URL"; \
    echo "$REDIS_DOWNLOAD_SHA *redis.tar.gz" | sha256sum -c -; \
    mkdir -p /usr/src/redis; \
    tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1; \
    rm redis.tar.gz; 
#编译Redis
RUN	make -C /usr/src/redis -j "$(nproc)"; \
    make -C /usr/src/redis install; \
    make -C /usr/src/redis/deps/hiredis; \
    make -C /usr/src/redis/deps/hiredis test; \
    make -C /usr/src/redis/deps/hiredis install; \
    ldconfig /usr/local/lib; \
    rm -r /usr/src/redis;
#下载安装 libevent
RUN wget https://github.com/libevent/libevent/releases/download/release-2.1.8-stable/libevent-2.1.8-stable.tar.gz;\
    mkdir -p /usr/src/libevent; \
    tar -xzf libevent-2.1.8-stable.tar.gz  -C /usr/src/libevent --strip-components=1;\
    rm libevent-2.1.8-stable.tar.gz;\
    /usr/src/libevent/configure --prefix=/usr;
#编译libevent
RUN  make && make install;
COPY redis.conf /data/
# change timezone
COPY Shanghai /etc/localtime
#定义数据卷
VOLUME /data
#容器的工作目录
WORKDIR /data
# for chinese input
ENV LANG C.UTF-8 
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
EXPOSE 6379
CMD ["redis-server", "./redis.conf"]
