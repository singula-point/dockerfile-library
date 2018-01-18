#从仓库拉取ubuntu16.04作为基础镜像
FROM  ubuntu:16.04
LABEL maintainer "ligp <ligp@singula-point.com>"
RUN apt-get update && \
    NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5 && \
    NVIDIA_GPGKEY_FPR=ae09fe4bbd223a84b2ccfce3f60f4b3d7fa2af80 && \
    apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub && \
    apt-key adv --export --no-emit-version -a $NVIDIA_GPGKEY_FPR | tail -n +5 > cudasign.pub && \
    echo "$NVIDIA_GPGKEY_SUM  cudasign.pub" | sha256sum -c --strict - && rm cudasign.pub && \
    echo "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/cuda.list && \
    echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list && \
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted\n \
             deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted\n \
             deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial universe\n \
             deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates universe\n \
             deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial multiverse\n \
             deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates multiverse\n \
             deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse\n \
             deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted\n \
             deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security universe\n \ 
             deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security multiverse\n" >> /etc/apt/sources.list 
#版本号说明
ENV CUDA_VERSION 8.0.61
ENV CUDNN_VERSION 6.0.21
ENV CUDA_PKG_VERSION 8-0=$CUDA_VERSION-1

#安装cuda8.0.61
RUN apt-get update && apt-get install -y --no-install-recommends \
        cuda-nvrtc-$CUDA_PKG_VERSION \
        cuda-nvgraph-$CUDA_PKG_VERSION \
        cuda-cusolver-$CUDA_PKG_VERSION \
        cuda-cublas-8-0=8.0.61.2-1 \
        cuda-cufft-$CUDA_PKG_VERSION \
        cuda-curand-$CUDA_PKG_VERSION \
        cuda-cusparse-$CUDA_PKG_VERSION \
        cuda-npp-$CUDA_PKG_VERSION \
        cuda-cudart-$CUDA_PKG_VERSION && \
    ln -s cuda-8.0 /usr/local/cuda && \
    rm -rf /var/lib/apt/lists/*

# nvidia-docker 1.0
LABEL com.nvidia.volumes.needed="nvidia_driver"
LABEL com.nvidia.cuda.version="${CUDA_VERSION}"
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64

#安装cudnn
RUN apt-get update && apt-get install -y --no-install-recommends \
            libcudnn6=$CUDNN_VERSION-1+cuda8.0 \
            libcudnn6-dev=$CUDNN_VERSION-1+cuda8.0 && \
    rm -rf /var/lib/apt/lists/*

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV NVIDIA_REQUIRE_CUDA "cuda>=8.0"

#安装TensorFlow-gpu
RUN apt-get update && apt-get install -y python3  \
        python3-pip python3-dev && \
    pip3 install --upgrade pip && \
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow-gpu && \
    rm -rf /var/lib/apt/lists/* && rm -rf ~/.pip/cache/

#安装keras、edward、 pandas、sklearn、h5py
RUN pip3 install -U --pre keras && \
    pip3 install edward pandas sklearn h5py tornado&& \
    rm -rf ~/.pip/cache/ && \
#安装jupyter
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
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root","/home"]
