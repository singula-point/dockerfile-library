本目录为mysql5.7.2的dockerfile及健康监测脚本healthcheck.sh、启动脚本docker-entrypoint.sh
构建镜像命令：docker build -t mysql .
运行容器：docker run -d -e MYSQL_ROOT_PASSWORD="123456" -p 3306:3306 mysql
其中，可使用-e MYSQL_ROOT_PASSWORD="mypasswd"设置初始密码，mypasswd为设置的密码，否则为随机密码
mysql版本号：mysql-5.7
   --by lgp