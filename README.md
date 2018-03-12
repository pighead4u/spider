# spider
爬虫的玩具之作

## 技术说明：
* 操作系统：macOS
* python：3.6.4
* 依赖管理：pipreqs
* orm：peewee
* 图表：pyecharts

## jobs文件夹
* 跟工作相关的爬虫
* 创建数据库表：python3 sql.py
* 执行：python3 main.py
* 创建图表：python3 pyecharts.py



## 问题记录：

### 数据存储：
* 一开始用的是excel
* 现在用的是sqlite，同时引入了ORM

### 图表展现：
* 一开始用的是matplotlib，但是由于中文问题，折腾了不少时间
* 现在使用pyecharts，中文问题可以忽略

### 数据过滤：
* 正在尝试Bloom filter

