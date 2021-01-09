## Flask 前端框架 + 高德API + 爬虫 + 宝塔安装教程
- 基于高德API  之前看到实验楼有一个实验说的就是如何结合爬虫和高德API 我觉得很有意思 于是就想顺着这个思路做下去 其中部分关于API的部分是借鉴其实验
- 爬虫爬取数据对接数据库  取数据到页面标点 并提供相应的组合网址进行跳转

### Demo展示
- 首页

![img](/img/index_demo.png)

- 租房页面
![img](/img/Index_demo_1.gif)
## **注意 该项目现在在重构 部分代码已经删除 会慢慢更新上来**
- [x] 复写前端 找大佬帮我改前端
- [x] 爬虫部分的重写 改用mongo
### 部署教程
**租房子一直是难题，所以我就写了一个租房数据可视化的前端。基本上都是东拼西凑出来的东西。本来打算是将这个项目做大的，可是后来不想做了，于是就这样了。我会在后面说清楚如何更改你的地址。**
声明：本项目中的，关于高德API和部分JS代码来自于[蓝桥云课](https://www.lanqiao.cn/courses/599)


- Flask超级小白教程:http://www.pythondoc.com/flask-mega-tutorial/index.html
- 云部署 Flask + WSGI + Nginx 详解:https://www.cnblogs.com/Ray-liang/p/4173923.html


## 准备阶段
- 既然是数据可视化就要使用爬虫，既然有了爬虫就涉及到数据的储存，考虑到租房数据的时效性，采用的是Sqlite。
- 考虑到这个项目未来需要让~~女朋友~~同学使用，所以挂在了服务器上，服务器部署方面采用宝塔，如何部署将会详细说明。

## 代码准备
### 生产环境
- 首先安装宝塔，具体安装命令-百度使用 nginx部署
- 添加一个新的站点 注意域名解析
![img](/img/web.png)
- 进入到刚才添加的站点的目录 在服务器上克隆我的项目源码/或者使用项目发布包 
```
# git clone https://github.com/nonewind/Flask_58_Rent.git
or
# wegt https://github.com/nonewind/Flask_58_Rent/archive/1.0.1.zip && unzip 1.0.1.zip
```
-  在宝塔中设定好项目目录 建立一个py虚拟环境
```
python -m venv venv_name
```
- 在宝塔的网站设置中添加如下内容
```
server {
  listen  80; 
  # listen 443; # 如果配置ssl 就需要添加上这一行
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
![img](/img/web_1.png)
在网站根目录下新建一个config.ini
```
[uwsgi]
# uwsgi
socket = 127.0.0.1:8386  启动时所使用的地址与端口，注意服务器提供商和宝塔的端口放行策略
chdir = /www/wwwroot/xxxxx.com # 指向网站目录
wsgi-file = run.py # python 启动程序文件,根据你的实际情况填写
callable = app # python 程序内用以启动的 application 变量名,根据你的实际情况填写
processes = 1  # 处理器数,根据你的实际情况填写
threads = 2  # 线程数
stats = 127.0.0.1:9191 #状态检测地址，注意服务器提供商和宝塔的端口放行策略
```
- 安装依赖
```
venv_name/bin/pip install -r requirements.txt
```
- 启动项目并记录网站日志
```
uwsgi config.ini > /www/wwwroot/website_path/web.log
```
- 访问你的网站 检查结果
### 本地环境
- 默认为win环境 如果为linux环境仅仅需要更改虚拟环境的指向地址
- 克隆我的项目源码/或者使用项目发布包 
```
# git clone https://github.com/nonewind/Flask_58_Rent.git
or
# wegt https://github.com/nonewind/Flask_58_Rent/archive/1.0.1.zip && unzip 1.0.1.zip
```
- 在本地新建一个虚拟环境
```
python -m venv venv_name
```
- 安装相关依赖
```
venv_name/Scripts/pip install -r requirements.txt
```
- 启动
```
venv_name/Scripts/python run.py
```
- 检查项目
浏览器访问 并检查项目
```
http://127.0.0.1:5000
```

## 需要自己修改的部分
### 数据库修改
- 默认数据库由原先的`sqlite`改为了现在的`mongoDB`

### 爬虫修改

