This image has been deprecated!!!


��Ŀ¼��Ϊ����cuda���ѧϰ������dockerfile

����������docker build -t cuda:8.0 .

����汾�ţ�Python3.5  cuda8.0.61  cudnn6.0.21

�����Ѱ�װ��������ߣ�TensorFlow-gpu��keras��edward�� pandas��sklearn��h5py��jupyter


ע�⣺1.�����о���ʱ��Ҫʹ��nvidia-docker�������docker������ᱨ��
      
      2.��Ҫʹ��jupyterʱʹ�����nvidia-docker run -d -p 8888:8888 cuda:8.0
        ����Ҫʹ��jupyter��ֻҪ�����������д���ʱִ�����nvidia-docker run -it cuda:8.0 bash 
       ���ɸ�����Ҫ�������ݾ� 




jupyter�÷����£�

���룺Ĭ������Ϊ123456�������޸����룬����������ʱ���뻷��������
      �磺�޸����룺xgl666
      ����������������Ϊ��
      docker run -d -e PASSWORD='xgl666'-p 8888:8888 jupyter

����jupyter�������������jupyter����ip:�˿ں�
             �磺192.168.1.20:8888
����·�������ɵĴ����ļ������������ڵ�/homeĿ¼�£���ͨ���������ݾ�ķ�ʽ����

   by lgp