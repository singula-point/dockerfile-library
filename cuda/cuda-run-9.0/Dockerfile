FROM ubuntu:16.04
LABEL maintainer Late Lee(li@latelee.org)

COPY n163.list /tmp
RUN cat /tmp/n163.list > /etc/apt/sources.list && rm -rf /tmp/n163.list

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates apt-transport-https gnupg-curl && \
    rm -rf /var/lib/apt/lists/* && \
    NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5 && \
    NVIDIA_GPGKEY_FPR=ae09fe4bbd223a84b2ccfce3f60f4b3d7fa2af80 && \
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub && \
    apt-key adv --export --no-emit-version -a $NVIDIA_GPGKEY_FPR | tail -n +5 > cudasign.pub && \
    echo "$NVIDIA_GPGKEY_SUM  cudasign.pub" | sha256sum -c --strict - && rm cudasign.pub && \
    echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/cuda.list && \
    echo "deb https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list

ENV CUDA_VERSION 9.0.176
ENV CUDNN_VERSION 7.2.1.38
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"
ENV CUDA_PKG_VERSION 9-0=$CUDA_VERSION-1

RUN apt-get update && apt-get install -y --no-install-recommends \
        cuda-cudart-$CUDA_PKG_VERSION \
	libcudnn7=$CUDNN_VERSION-1+cuda9.0 && \
	apt-mark hold libcudnn7 && \
    	ln -s cuda-9.0 /usr/local/cuda && \
    	rm -rf /var/lib/apt/lists/*

# nvidia-docker 1.0
LABEL com.nvidia.volumes.needed="nvidia_driver"
LABEL com.nvidia.cuda.version="${CUDA_VERSION}"

RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV NVIDIA_REQUIRE_CUDA "cuda>=9.0"

#install TensorFlow-gpu
RUN apt-get update && apt-get install -y python3  \
        python3-pip python3-dev && \
#    pip3 install --upgrade pip && \
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow-gpu && \
    rm -rf /var/lib/apt/lists/* && rm -rf ~/.pip/cache/

#install keras、edward、 pandas、sklearn、h5py
RUN pip3 install -U --pre keras && \
    pip3 install edward pandas sklearn h5py tornado&& \
    rm -rf ~/.pip/cache/ && \
    # install jupyter
    rm -f /usr/bin/python \
    && ln -s /usr/bin/python3.5 /usr/bin/python \
    && rm -f /usr/bin/pip && ln -s /usr/bin/pip3 /usr/bin/pip \
    &&pip3 install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple \
    ##configurea passwd
    && jupyter notebook --generate-config \
    && mv /root/.jupyter/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py.bak
    #从宿主机拷贝配置文件
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
#ENTRYPOINT jupyter notebook --ip=0.0.0.0 --allow-root /home

# for chinese input
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root","/home"]
