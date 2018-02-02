FROM ubuntu:16.04

LABEL maintainer Li Jiangjin(lijj@singula-poing.com)

RUN apt-get update || true && \
    apt-get install -y \
    vim tree wget curl \
    libssl-dev gdb flex bison \
    cmake autoconf git \
    unzip cppcheck dos2unix \
    apt-transport-https ca-certificates software-properties-common \
    net-tools inetutils-ping pkg-config \
    libreadline-dev libbluetooth-dev libglib2.0-dev \
    python3-pip python3-dev python3 openjdk-8-jdk &&\
    ln -s /usr/bin/python3 /usr/bin/python || true &&\
    ln -s /usr/bin/pip3 /usr/bin/pip || true && \
    pip install --upgrade pip && \
    pip --no-cache-dir install numpy wheel && \
    rm -rf /var/lib/dpkg/info/* /var/lib/apt/lists/* \
    /var/log/*.log /root/.cache

ENV BOOST_SHA 5721818253e6a0989583192f96782c4a98eb6204965316df9f5ad75819225ca9

RUN mkdir -p /tmp/test && \
    cd /tmp/test && \
    wget https://dl.bintray.com/boostorg/release/1.66.0/source/boost_1_66_0.tar.bz2 && echo "$BOOST_SHA boost_1_66_0.tar.bz2" | sha256sum -c - && \
    tar jxf boost_1_66_0.tar.bz2 && cd boost_1_66_0 && \
    sh bootstrap.sh --with-libraries=all -with-toolset=gcc && \
    ./b2 || true && ./b2 install || true && \
    cd / && rm -rf /tmp/test

RUN wget http://fftw.org/fftw-3.3.7.tar.gz && \
    tar zxf fftw-3.3.7.tar.gz && \
    cd fftw-3.3.7 && ./configure && make && make install && \
    cd - && rm -rf fftw-3.3.7*

RUN wget https://github.com/libevent/libevent/releases/download/release-2.1.8-stable/libevent-2.1.8-stable.tar.gz && \
    tar xzf libevent-2.1.8-stable.tar.gz && \
    cd libevent-2.1.8-stable && \
    ./configure && make && make install && \
    cd - && rm -rf libevent-2.1.8-stable.tar.gz libevent-2.1.8-stable

RUN wget https://github.com/openssl/openssl/archive/OpenSSL_1_0_2n.tar.gz && \
    tar zxf OpenSSL_1_0_2n.tar.gz && \
    cd openssl-OpenSSL_1_0_2n && \
    ./config && make && make install && \
    cd - && rm -rf OpenSSL_1_0_2n.tar.gz openssl-OpenSSL_1_0_2n

RUN git clone https://github.com/labapart/gattlib && \
    cd gattlib && mkdir build && cd build && \
    cmake -DGATTLIB_FORCE_DBUS=TRUE .. && \
    make && make install && \
    cd / && rm -rf gattlib

ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-4.0.2.tar.gz
ENV REDIS_DOWNLOAD_SHA b1a0915dbc91b979d06df1977fe594c3fa9b189f1f3d38743a2948c9f7634813

# download redis
RUN wget -O redis.tar.gz "$REDIS_DOWNLOAD_URL" && \
    echo "$REDIS_DOWNLOAD_SHA *redis.tar.gz" | sha256sum -c - && \
    mkdir -p redis && \
    tar -xzf redis.tar.gz -C redis --strip-components=1 && \
    rm redis.tar.gz

# install redis
RUN make -C redis/deps/hiredis && \
    make -C redis/deps/hiredis install && \
    rm -r redis

# install mysql head files & library files
RUN mkdir /usr/local/include/mysql && \
    wget https://dev.mysql.com/get/Downloads/Connector-C/mysql-connector-c-6.1.11-linux-glibc2.12-x86_64.tar.gz && \
    tar zxf mysql-connector-c-6.1.11-linux-glibc2.12-x86_64.tar.gz && \
    cp -a mysql-connector-c-6.1.11-linux-glibc2.12-x86_64/include /usr/local/include/mysql && \
    cp -a mysql-connector-c-6.1.11-linux-glibc2.12-x86_64/lib/* /usr/local/lib/ && \
    rm -rf mysql-connector-c-6.1.11-linux-glibc2.12-x86_64.tar.gz mysql-connector-c-6.1.11-linux-glibc2.12-x86_64


CMD ["bash"]

