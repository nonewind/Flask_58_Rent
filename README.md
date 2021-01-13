## 快点回家
一款基于Flask、高德开放api的可视化地图租房规划web

**愿你在陌生冰冷的城市里有一盏属于自己的灯**
[预览地址](http://map.ziheng.xyz)~~pc/pad浏览获得最好体验~~


声明：本项目中的，关于高德API和部分JS代码来自于[蓝桥云课](https://www.lanqiao.cn/courses/599)
- Flask超级小白教程:http://www.pythondoc.com/flask-mega-tutorial/index.html
- 云部署 Flask + WSGI + Nginx 详解:https://www.cnblogs.com/Ray-liang/p/4173923.html
- 前端采用Bootstrap 后端采用Flask 数据库采用Mongo

## 致谢
- JianboWu 感谢他提供的Bootstrap Studio激活码
### Demo展示
- 首页
![img](/img/index_demo.png)****

- 租房页面
![img](/img/Index_demo_1.gif)

### 项目规划
- [x] 抓取并展示58的租房数据 初步完成项目构架
- [x] 定时清理数据库冗余数据
~~对于多数据源 这个会慢慢更新~~
- [ ] 对于租房数据的细分 例如：1. 合租/整租 2.个人房源/中介房源(可信度不高)
- [ ] 抓取并展示安居客的租房数据
### 部署教程
**爬虫强依赖于定时任务**
### 服务器端部署
- 找个ssh连接工具 连接上你的服务器
- 安装[宝塔面板](https://www.bt.cn/bbs/thread-19376-1-1.html)
- 根据命令行 复制输出的面板管理网址 登录面板
- 安装完成请打开软件商店搜索安装 **Nginx** 和 **mongoDB**
- 添加一个新的站点 注意域名解析 注意这里设置为纯静态
![img](/img/web.png)
- 进入到刚才添加的站点的目录 在服务器上克隆我的项目源码
```
git clone https://github.com/nonewind/Flask_58_Rent.git && cd Flask_58_Rent
```
- 检查一下服务器上的Python版本 需要3.x
-  在宝塔中设定好项目目录 建立一个py虚拟环境 并且安装依赖库
```
python -m venv pyvenv && pyvenv/bin/pip install -r requirements.txt
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
    uwsgi_param UWSGI_PYHOME /www/wwwroot/xxxxxx.com/pyvenv; # 指向虚拟环境目录
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
- 启动项目并记录网站日志 ~~不知道为什么日志记录不成功~~
```
nohup uwsgi config.ini >> /www/wwwroot/website_path/web.log &
```
- 在宝塔面板中[添加定时任务](https://jingyan.baidu.com/article/f96699bba208f9c84e3c1b80.html)
```
/www/wwwroot/YourDomain/Flask_58_Rent/pyvenv/bin/python /www/wwwroot/YourDomain/Flask_58_Rent/spider/spider-58.py >> /www/wwwroot/YourDomain/Flask_58_Rent/spider/log.log
```