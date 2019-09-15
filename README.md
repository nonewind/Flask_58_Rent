## Flask 前端框架 + 高德API + 爬虫 + 宝塔安装教程
- 基于高德API  之前看到实验楼有一个实验说的就是如何结合爬虫和高德API 我觉得很有意思 于是就想顺着这个思路做下去 其中部分关于API的部分是借鉴其实验
- 爬虫爬取数据对接数据库  取数据到页面标点 并提供相应的组合网址进行跳转
- 关于域名解析 服务器设置请自行探索
##### 安装宝塔
 - centos ： yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh
 - Ubuntu/Deepin ： wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && sudo bash install.sh
 - Debian ： wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && bash install.sh
##### 宝塔内创建新网站
- ![Image text](https://github.com/nonewind/Flask_58_Rent/blob/master/img/web.png)
- ![Image text](https://github.com/nonewind/Flask_58_Rent/blob/master/img/web_1.png)
- 根据你的设置 修改如下配置并填写
```
server {
  listen  80; 
  server_name xxxxxx.com; #你的网址地址
  location / {
    include      uwsgi_params;
    uwsgi_pass   127.0.0.1:8386;  # 指向uwsgi 所应用的内部地址,所有请求将转发给uwsgi 处理 注意宝塔/服务器供应商需要放行这个端口
    uwsgi_param UWSGI_PYHOME /www/wwwroot/xxxxxx.com/demo; # 指向虚拟环境目录
    uwsgi_param UWSGI_CHDIR  /www/wwwroot/xxxxxx.com; # 指向网站根目录
    uwsgi_param UWSGI_SCRIPT run:app; # 指定启动程序，main是main.py前部分,app是程序内用以启动的 application 变量名
  }
}
```
##### 将项目克隆到本地
- git clone https://github.com/nonewind/Flask_58_Rent.git
##### 新建一个python虚拟环境
- python -m venv demo 
- demo 就是虚拟环境的名字
##### 安装相关依赖
- Linux :  demo/bin/pip install req.txt
##### 在根目录下创建 config.ini
```
[uwsgi]
# uwsgi 启动时所使用的地址与端口，注意服务器提供商和宝塔的端口放行策略
socket = 127.0.0.1:8386
# 指向网站目录
chdir = /www/wwwroot/xxxxx.com
# python 启动程序文件,根据你的实际情况填写
wsgi-file = run.py
# python 程序内用以启动的 application 变量名,根据你的实际情况填写
callable = app
# 处理器数,根据你的实际情况填写
processes = 1
# 线程数
threads = 2
#状态检测地址，注意服务器提供商和宝塔的端口放行策略
stats = 127.0.0.1:9191
```
- 运行并改错
``` 
uwsgi config.ini
```
##### 修改../app/views.py 中的对接地址
```
DATABASE = '/www/wwwroot/yourwebsite/data_loc.db'
```
- 将yourwebsite 改成你的网站
##### 至此，此项目应该可以运行


