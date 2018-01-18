
FROM singula/ubuntu:dev
MAINTAINER ligp
#COPY sources.list /etc/apt/  
COPY jenkins.sh /
#
RUN apt-get update || true
RUN apt-get install dpkg \
    build-essential\
	& chmod +x jenkins.sh

#install JDK docker
RUN apt-get install docker.io -y
#依赖包
RUN apt-get install -y daemon\
                       psmisc

#to install jenkins     
RUN wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | apt-key add -  \
    && wget https://mirrors.tuna.tsinghua.edu.cn/jenkins/debian-stable/jenkins_2.89.1_all.deb \
    && dpkg -i jenkins_2.89.1_all.deb \
    &&rm jenkins_2.89.1_all.deb \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
	
#暴露容器端口
EXPOSE 8080 50000
#定义数据卷
VOLUME ["/var/run/docker.sock","/var/lib/jenkins"]
# Run the jenkins.sh
CMD /jenkins.sh