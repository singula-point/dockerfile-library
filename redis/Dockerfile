FROM redis:4.0.11-alpine
#作者信息
MAINTAINER XGL

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
