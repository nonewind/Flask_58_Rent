## Flask 前端框架 + 高德API + 爬虫 + 宝塔安装教程
- 基于高德API  之前看到实验楼有一个实验说的就是如何结合爬虫和高德API 我觉得很有意思 于是就想顺着这个思路做下去 其中部分关于API的部分是借鉴其实验
- 爬虫爬取数据对接数据库  取数据到页面标点 并提供相应的组合网址进行跳转

### Demo展示
- 首页

![img](/img/index_demo.png)

- 租房页面
![img](/img/Index_demo_1.gif)

### 项目规划
- [x] 抓取并展示58的租房数据 初步完成项目构架
- [ ] 对于租房数据的细分 例如：1. 合租/整租 2.个人房源/中介房源(可信度不高)
- [ ] 抓取并展示安居客的租房数据
### 项目必要/可选组成
- [ ] 为**可选**
- [x]  为**必须**
> |||||||||||||||||||||||||||||||||我是分割线|||||||||||||||||||||||||||||||||
- [ ] 腾讯云~~良心云~~的cos静态存储桶当作国内静态资源的cdn
- [ ] 一个域名~~如果仅仅是局域网或者本地访问就不需要域名~~
- [x] 服务器一台 需要安装 宝塔Linux面板 mongoDB

### 部署教程
**租房子一直是难题，所以我就写了一个租房数据可视化的前端。我会在后面说清楚如何详细配置**
声明：本项目中的，关于高德API和部分JS代码来自于[蓝桥云课](https://www.lanqiao.cn/courses/599)


- Flask超级小白教程:http://www.pythondoc.com/flask-mega-tutorial/index.html
- 云部署 Flask + WSGI + Nginx 详解:https://www.cnblogs.com/Ray-liang/p/4173923.html
## 代码准备
### 服务器端部署
- 找个ssh连接工具 连接上你的服务器
- 安装[宝塔面板](https://www.bt.cn/bbs/thread-19376-1-1.html) <-- 官方教程 
- 根据命令行 复制输出的面板管理网址 登录面板
- 安装完成请打开软件商店搜索安装 **Nginx** 和 **mongoDB**
- 添加一个新的站点 注意域名解析 注意这里设置为纯静态
![img](/img/web.png)
- 进入到刚才添加的站点的目录 在服务器上克隆我的项目源码
```
# git clone https://github.com/nonewind/Flask_58_Rent.git
```
- **检查一下服务器上的Python版本 需要3.x
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
    uwsgi_param UWSGI_SCRIPT run:app;  # 指定启动程序，main是main.py前部分,app是程序内用以启动的 application 变量名
  }
}
```
![img](/img/web_1.png)
在网站根目录下新建一个config.ini 在写完配置以后 **删除注释**
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
nohup uwsgi config.ini >> /www/wwwroot/website_path/web.log &
```
- 启动爬虫

### 本地环境
- 默认为win环境 如果为linux环境仅仅需要更改虚拟环境的指向地址
- 克隆我的项目源码
```
# git clone https://github.com/nonewind/Flask_58_Rent.git
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
http://127.0.0.1:8386
```
## 修改数据库地址
- 打开网站根目录下的config和spider/下的config
- 将其中的`数据库地址`修改为 `mongodb://127.0.0.1:27017`