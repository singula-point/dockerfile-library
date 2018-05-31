# 2017-12-01 by gym
#从官网下载基础镜像oraclelinux:7-slim(集成rpmkeys 和yum命令)
#构建时从官网下mysql的rpm包。这种构建出来的docker 占空间最小
#启动用的脚本是从网上下载

FROM oraclelinux:7-slim

#构建临时变量
ARG PACKAGE_URL=https://repo.mysql.com/yum/mysql-5.7-community/docker/x86_64/mysql-community-server-minimal-5.7.20-1.el7.x86_64.rpm
ARG PACKAGE_URL_SHELL=https://repo.mysql.com/yum/mysql-tools-community/el/7/x86_64/mysql-shell-1.0.10-1.el7.x86_64.rpm

# 安装服务
RUN rpmkeys --import https://repo.mysql.com/RPM-GPG-KEY-mysql \
  && yum install -y $PACKAGE_URL $PACKAGE_URL_SHELL libpwquality \
  && yum clean all \
  && mkdir /docker-entrypoint-initdb.d

#允许别的容器共享数据卷
VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /entrypoint.sh
COPY healthcheck.sh /healthcheck.sh
RUN  chmod +x /*.sh
ENTRYPOINT ["/entrypoint.sh"]

#检测mysql是否正常启动
HEALTHCHECK CMD /healthcheck.sh
EXPOSE 3306
# change timezone
COPY Shanghai /etc/localtime
# for chinese input
ENV LANG C.UTF-8 
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
CMD ["mysqld"]