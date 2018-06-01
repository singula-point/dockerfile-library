# 2018-1-17 by ligp
#基础镜像为ubuntu:16.04
FROM ubuntu:16.04
#作者信息
MAINTAINER ligp
#设置环境变量
ARG jre_url=download.oracle.com/otn-pub/java/jdk/10.0.1+10/fb4372174a714e6b8c52526dc134031e/serverjre-10.0.1_linux-x64_bin.tar.gz
ENV JAVA_VERSION="10.0.1"
ENV JAVA_HOME="/usr/local/jdk${JAVA_VERSION}" 
ENV JRE_HOME=${JAVA_HOME} 
ENV PATH="${PATH}:${JAVA_HOME}/bin"
#安装jre
RUN apt-get update \
    && apt-get install wget -y \
    && wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" $jre_url \
    && mkdir /usr/local/jdk10.0.1 \
    && tar xf serverjre-10.0.1_linux-x64_bin.tar.gz -C /usr/local/jdk10.0.1 --strip-components=1 \
    && rm serverjre-10.0.1_linux-x64_bin.tar.gz \ 
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/*
# change timezone
COPY Shanghai /etc/localtime
# for chinese input
ENV LANG C.UTF-8 
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
CMD ["java","Server"]
