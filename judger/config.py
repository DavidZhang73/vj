"""Judger 全局配置"""
from os import environ

# HOST 地址
if environ.get('ENV') == 'DEV':
    host = 'davidz.cn'
else:
    host = "localhost"

# 数据库
dbhost = "mongodb://{}:27017/".format(host)

# 数据库名
dbname = "vj"

# 超时重试
timeout = 30  # s

# 页面访问间隔
time_interval = 0.5  # s

# 账号信息
# 用于向OJ提交代码
accounts = {
    "POJ": {
        "username": "tester666",
        "password": "tester666",
        "nickname": "tester666",
    },
    "HDU": {
        "username": "sduwhvj",
        "password": "sduwhvj2016",
        "nickname": "sduwhvj",
    },
    "SDUT": {
        "username": "sduwhvj1",
        "password": "sduwhvj1",
        "nickname": "sduwhvj",
    },
}
