本目录下为Tomcat镜像的dockerfile。
构建镜像命令：docker build -t tomcat .
运行镜像：docker run -d -p 8080:8080 tomcat
Tomcat版本号：tomcat-9.0.2
测试：在浏览器输入主机IP+端口号，如：192.168.31.136:8080按回车会出现Tomcat官方的页面