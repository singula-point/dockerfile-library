#2018-01-16 by ligp
#容器中的tomcat 要用catalina.sh脚本来启动，不能用startup.sh
#基础镜像为singula/jre
FROM singula/jre
#作者信息
MAINTAINER ligp
ARG tomcat_url=http://mirrors.hust.edu.cn/apache/tomcat/tomcat-9/v9.0.4/bin/apache-tomcat-9.0.4.tar.gz
#安装Tomcat
RUN wget $tomcat_url \
    && mkdir /usr/local/java \
    && tar xf apache-tomcat-9.0.4.tar.gz -C /usr/local/java\
    && rm apache-tomcat-9.0.4.tar.gz
RUN  adduser --system --shell /bin/bash --gecos 'Tomcat Java Servlet and JSP engine' --group --disabled-password --home /home/tomcat \tomcat \
     && ln -s /usr/local/java/apache-tomcat-9.0.4 /usr/local/tomcat \
     && chown -R tomcat:tomcat /usr/local/tomcat/* \
     && chmod +x /usr/local/tomcat/bin/*.sh 
EXPOSE 8080
# change timezone
COPY Shanghai /etc/localtime
CMD ["/usr/local/tomcat/bin/catalina.sh","run"]
