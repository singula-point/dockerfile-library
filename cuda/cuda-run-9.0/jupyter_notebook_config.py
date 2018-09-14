# Configuration file for jupyter-notebook.
#by lgp
#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
import os
from IPython.lib import passwd
#所有IP可连接
c.NotebookApp.ip = '*'
#连接端口号为8888
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False
#如果存在环境变量PASSWORD，取其值作为密码，否则使用默认密码123456
if 'PASSWORD' in os.environ:
  password = os.environ['PASSWORD']
  if password:
    c.NotebookApp.password = passwd(password)
  else:
    del os.environ['PASSWORD']
else:
  c.NotebookApp.password = passwd('123456')
