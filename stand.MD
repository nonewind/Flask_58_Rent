<!--
 * @Author: Ziheng
 * @Date: 2021-03-16 10:50:32
 * @LastEditTime: 2021-03-16 10:50:49
-->
# 🕸🕸🕸🕸部署教程🕸🕸🕸🕸
**爬虫强依赖于定时任务**
### 🕸🕸服务器端部署🕸🕸
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
- 云部署 Flask + WSGI + Nginx 详解:https://www.cnblogs.com/Ray-liang/p/4173923.html
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
