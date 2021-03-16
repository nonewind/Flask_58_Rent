<!--
 * @Author: Ziheng
 * @Date: 2021-01-11 10:19:28
 * @LastEditTime: 2021-03-16 10:58:47
-->
## 🕸🕸🕸🕸 快点回家 🕸🕸🕸🕸
**愿你在陌生冰冷的城市里有一盏属于自己的灯**
- 一款基于Flask、高德开放api的可视化地图租房规划
- 快速筛选基于自己的心里价位 租房类型 上下班路线规划 

**项目正在进行中 预览可能与实际代码产生页面有区别**
[预览地址](http://map.ziheng.xyz)


**租房数据来自于互联网公开数据 涉及金钱交易时 请注意自身财产安全**

![img](https://img.shields.io/badge/Flask-1.1.2-brightgreen)  ![img](https://img.shields.io/badge/beautifulsoup4-4.9.3-brightgreen)  ![img](https://img.shields.io/badge/pymongo-3.11.2-brightgreen)  ![img](https://img.shields.io/badge/requests-2.25.1-brightgreen)

## 🕸🕸🕸致谢🕸🕸🕸
- JianboWu 感谢他提供的Bootstrap Studio激活码
### 🕸🕸Demo展示🕸🕸
- 首页
![img](/img/index_demo.png)

- 租房页面
![img](/img/Index_demo_1.gif)

### 🕸🕸🕸🕸🕸项目规划🕸🕸🕸🕸🕸
#### 🕸完成🕸
- [x] 抓取并展示**某同城**的租房数据 初步完成项目构架
- [x] 定时清理数据库冗余数据
- [x] 优化前端展示
  - [x] 聚合筛选结果
  - [x] 由上部导航栏 改为左侧导航栏
  - [x] 增加多个筛选条件
  - [x] 点击标记点 左侧导航栏展示房源详细信息
  - [x] 标记点聚合 点击清除按钮时 完全清除
#### 🕸正在进行🕸
- [ ] 爬虫部分
  - [x] 抓取速度优化 改为~~分布式爬虫~~一个价格只抓200信息
  - [x] 删除库内冗余数据
  - [x] 对应前端详细信息 爬虫新增抓取项目
  - [x] 整租或者单间
- [ ] 房源增加**某居客**

### 部署教程请看 stand.MD