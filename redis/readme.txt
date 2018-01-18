本目录为构建Redis镜像的dockerfile与配置文件redis.conf
构建命令：docker build -t redis .
运行容器：docker run -d -p 6379:6379 redis
Redis版本号redis-4.0.2，libevent版本号release-2.1.8-stable
 --by lgp