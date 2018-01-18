#基础镜像为ubuntu14.04
FROM ubuntu:14.04
#作者信息
MAINTAINER ligp
RUN apt-get update -q \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
      ca-certificates \
      openssh-server \
      wget \
      apt-transport-https 
# 下载安装gitlab 
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/ubuntu trusty main" > /etc/apt/sources.list.d/gitlab_gitlab-ce.list \
    && wget -q -O - https://packages.gitlab.com/gpg.key | apt-key add - \
    && apt-get update || ture &&  apt-get install -y gitlab-ce=10.1.0-ce.0
# Manage SSHD through runit 
RUN mkdir -p /opt/gitlab/sv/sshd/supervise \
    && mkfifo /opt/gitlab/sv/sshd/supervise/ok \
    && printf "#!/bin/sh\nexec 2>&1\numask 077\nexec /usr/sbin/sshd -D" > /opt/gitlab/sv/sshd/run \
    && chmod a+x /opt/gitlab/sv/sshd/run \
    && ln -s /opt/gitlab/sv/sshd /opt/gitlab/service \
    && mkdir -p /var/run/sshd \
	&& apt-get clean && rm -rf /var/lib/apt/lists/* \
# Disabling use DNS in ssh since it tends to slow connecting 
    &&echo "UseDNS no" >> /etc/ssh/sshd_config
# 默认配置
RUN ( \
  echo "" && \
  echo "# Docker options" && \
  echo "# Prevent Postgres from trying to allocate 25% of total memory" && \
  echo "postgresql['shared_buffers'] = '1MB'" ) >> /etc/gitlab/gitlab.rb 
# 开放端口
EXPOSE 443 80 22
# 定义数据卷
VOLUME ["/etc/gitlab", "/var/opt/gitlab", "/var/log/gitlab"]
COPY wrapper /usr/local/bin/
RUN chmod 777 /usr/local/bin/wrapper
COPY RELEASE /
# Wrapper to handle signal, trigger runit and reconfigure GitLab 
CMD ["/usr/local/bin/wrapper"]
