
build tensorflow:
bazel build -c opt --config=cuda --incompatible_load_argument_is_label=false //tensorflow/tools/pip_package:build_pip_package

generate whl file
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg

then the file will be there:
/tmp/tensorflow_pkg/tensorflow-1.4.1-cp35-cp35m-linux_x86_64.whl 

put the .whl file to your linux and install it:
pip install tensorflow-1.4.1-cp35-cp35m-linux_x86_64.whl 

docker-compose file:

# cuda for tensorflow building Powered by singula
version: '2'
services:
    cuda:
        image: singula/cuda:8.0-cudnn6-devel
        container_name: mycuda
        #restart: always
        volumes:
            - /home/:/home/
            - /usr/local/nvidia:/var/lib/nvidia-docker/volumes/nvidia_driver/384.90
            - /dev/nvidia0:/dev/nvidia0
            - /dev/nvidia-uvm:/dev/nvidia-uvm
            - /dev/nvidia-uvm-tools:/dev/nvidia-uvm-tools
            - /dev/nvidiactl:/dev/nvidiactl
            - /usr/lib/nvidia-384:/usr/lib/nvidia-384
            - /usr/lib/x86_64-linux-gnu/libcuda.so:/usr/lib/x86_64-linux-gnu/libcuda.so
            - /usr/lib/x86_64-linux-gnu/libcuda.so.1:/usr/lib/x86_64-linux-gnu/libcuda.so.1
            - /usr/lib/x86_64-linux-gnu/libcuda.so.384.90:/usr/lib/x86_64-linux-gnu/libcuda.so.384.90
            - /usr/lib/nvidia-384/libnvidia-fatbinaryloader.so.384.90:/usr/lib/x86_64-linux-gnu/libnvidia-fatbinaryloader.so.384.90
        command: sleep 999999999
