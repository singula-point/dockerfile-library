1��Dockerfile�ļ��ܹ�һ������gitlab��gitlab�汾��Ϊ10.1.0-ce.0����������汾������dockerfile��ָ���汾���磺
   ����10.2.1-ce.0�汾���޸İ�װgitlab������Ϊ��apt-get install -y gitlab-ce=10.2.1-ce.0��Ȼ��ִ��build�����

2�������������docker build -t gitlab:10.1.0-ce.0 .

3������������Ҫ��װ����������Ҫ���ĵȴ�

4����������:docker run -d -e URL=http://192.168.31.136 -p 80:80 gitlab:10.1.0-ce.0
          

ע�������ָ��URL��Ĭ�ϵ�URLΪgitlab.example.com

--by lgp