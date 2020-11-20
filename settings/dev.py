from .base import *

DEBUG = True

ALLOWED_HOSTS = ["172.16.43.131","127.0.0.1"]

# 务必修改以下值，确保运行时系统安全
SECRET_KEY = '7t(5#ae^5^!)c^#cij*w9e4b+0mq7cr4i$jxy538j1s2l_7j)t'

LDAP_AUTH_URL = "ldap://172.16.43.131:389"
LDAP_AUTH_CONNECTION_USERNAME="admin"
LDAP_AUTH_CONNECTION_PASSWORD="123456"



INSTALLED_APPS += (

)






