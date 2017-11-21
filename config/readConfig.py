# 用于读取config文件
import configparser
import os

config = configparser.ConfigParser()

# 当前脚本所在文件的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

# 获取配置文件
configPath = os.path.join(cur_path,"config.ini")

config.read(configPath,"utf-8")

# 1、smtp_server
server = config.get("email","smtp_server")
# 2、port
port = config.get("email","port")
# 3、sender
sender = config.get("email","sender")
# 4、pwd
pwd = config.get("email","pwd")
# 5、receiver
receiver = config.get("email","receiver")
# 6、receiver多个时，split

print(server)
print(port)
print(sender)
print(pwd)
print(receiver)





