本目录下为Jenkins的dockerfile及其启动脚本
构建Jenkins镜像：docker build -t jenkins .
运行容器：docker run -p 8080:8080 -p 50000:50000 jenkins
访问：在浏览器输出主机IP+端口号
如主机IP为192.168.31.136，则输入192.168.31.136:8080
Jenkins版本号：jenkins_2.89.1
   --by lgp