# 2018-1-17 by ligp
#基础镜像为ubuntu:16.04
FROM ubuntu:16.04
#作者信息
MAINTAINER ligp
#设置环境变量
ARG jre_url=download.oracle.com/otn-pub/java/jdk/9.0.4+11/c2514751926b4512b076cc82f959763f/serverjre-9.0.4_linux-x64_bin.tar.gz
ENV JAVA_VERSION="9.0.4"
ENV JAVA_HOME="/usr/local/jdk${JAVA_VERSION}" 
ENV JRE_HOME=${JAVA_HOME} 
ENV PATH="${PATH}:${JAVA_HOME}/bin"
#安装jre
RUN apt-get update \
    && apt-get install wget -y \
    && wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" $jre_url \
    && mkdir /usr/local/jdk9.0.4 \
    && tar xf serverjre-9.0.4_linux-x64_bin.tar.gz -C /usr/local/jdk9.0.4 --strip-components=1 \
    && rm serverjre-9.0.4_linux-x64_bin.tar.gz \ 
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/*
# change timezone
COPY Shanghai /etc/localtime
CMD ["java","Server"]
