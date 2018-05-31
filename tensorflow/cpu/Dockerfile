#从仓库拉取ubuntu16.04作为基础镜像
FROM  ubuntu:16.04
LABEL maintainer "ligp <ligp@singula-point.com>"
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install redis h5py&& \
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/  \
         https://mirrors.tuna.tsinghua.edu.cn/tensorflow/linux/cpu/tensorflow-1.6.0-cp35-cp35m-linux_x86_64.whl && \
    	 rm -rf /var/lib/apt/lists/* && rm -rf ~/.pip/cache/ && \
	 rm -rf /root/.cache && apt-get autoremove gcc python3-pip -y
# change timezone
COPY Shanghai /etc/localtime
# for chinese input
ENV LANG C.UTF-8 
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8