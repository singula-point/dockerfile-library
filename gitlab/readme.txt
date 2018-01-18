1、Dockerfile文件能够一键构建gitlab，gitlab版本号为10.1.0-ce.0，如需更换版本，可在dockerfile下指定版本，如：
   更换10.2.1-ce.0版本，修改安装gitlab的命令为：apt-get install -y gitlab-ce=10.2.1-ce.0，然后执行build命令即可

2、构建镜像命令：docker build -t gitlab:10.1.0-ce.0 .

3、构建过程需要安装相关软件，需要耐心等待

4、运行容器:docker run -d -e URL=http://192.168.31.136 -p 80:80 gitlab:10.1.0-ce.0
          

注：如果不指定URL，默认的URL为gitlab.example.com

--by lgp