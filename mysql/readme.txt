��Ŀ¼Ϊmysql5.7.2��dockerfile���������ű�healthcheck.sh�������ű�docker-entrypoint.sh
�����������docker build -t mysql .
����������docker run -d -e MYSQL_ROOT_PASSWORD="123456" -p 3306:3306 mysql
���У���ʹ��-e MYSQL_ROOT_PASSWORD="mypasswd"���ó�ʼ���룬mypasswdΪ���õ����룬����Ϊ�������
mysql�汾�ţ�mysql-5.7
   --by lgp