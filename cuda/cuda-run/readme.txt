This image has been deprecated!!!


本目录下为构建cuda深度学习环境的dockerfile

构建方法：docker build -t cuda:8.0 .

软件版本号：Python3.5  cuda8.0.61  cudnn6.0.21

其他已安装的软件工具：TensorFlow-gpu、keras、edward、 pandas、sklearn、h5py、jupyter


注意：1.在运行镜像时，要使用nvidia-docker命令代替docker，否则会报错。
      
      2.需要使用jupyter时使用命令：nvidia-docker run -d -p 8888:8888 cuda:8.0
        不需要使用jupyter，只要进入容器运行代码时执行命令：nvidia-docker run -it cuda:8.0 bash 
       （可根据需要挂载数据卷） 




jupyter用法如下：

密码：默认密码为123456，如需修改密码，在运行容器时加入环境变量。
      如：修改密码：xgl666
      则运行容器的命令为：
      docker run -d -e PASSWORD='xgl666'-p 8888:8888 jupyter

访问jupyter：浏览器中输入jupyter主机ip:端口号
             如：192.168.1.20:8888
数据路径：生成的代码文件保存在容器内的/home目录下，可通过挂载数据卷的方式导出

   by lgp