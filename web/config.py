"""Web 全局配置"""
# Host
host = "192.168.75.129"

# Web服务端口
port = 8000

# 数据库地址
dbhost = "mongodb://{}:27017/".format(host)

# 数据库名
dbname = "vj"

# 静态文件目录
static_path = "./static"

# 模板文件目录
template_path = "./templates"

# Problem/Submisson/Contest/...每页显示的记录数
rows_per_page = 50
