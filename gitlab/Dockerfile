FROM gitlab/gitlab-ce:11.1.4-ce.0

MAINTAINER singulatech

RUN apt-get update
    && \
    apt-get install -y \
    inetutils-ping net-tools \
    && \
    rm -rf /var/lib/apt/lists/*

# for chinese input
ENV LANG C.UTF-8 
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
CMD ["/usr/local/bin/wrapper"]

