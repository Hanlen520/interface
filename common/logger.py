# 封装日志的输出
import logging,time
import os

# 当前脚本所在文件的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

# 获取存放打印日志的文件
log_path = os.path.join(os.path.dirname(cur_path),"logs")
# 如果logs文件夹不存在，就自动创建
if not os.path.exists(log_path):
    os.mkdir(log_path)

class Log():
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))

