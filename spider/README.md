### 爬虫部分

- [ ] 爬虫从 文档`spider_task`中获取目标任务

```[json]
{
    "city_task":[],  -> list()
}
```
- [ ] 爬虫将获取到的数据写入到`spider-result`中
- [ ] 爬虫需要写入的数据包括房子的名称and房源url放入一个json中 再顺序打包放入list中

```[json]
{
    "title":"",    -> string()
    "url":"",      -> string()
    "priceLevel":,    -> int()
    "cityname":""     - >string()
}
```
- [x] 爬虫默认每周启动一次 每次抓取时长间隔为30s 抓取深度为20个Page
- [ ] 租房数据超过7天的视为冗余数据 清理
- [x] 优化清洗`url`部分的正则表达式 让数据库更小 让后端传递过去的json更小

- [ ] 将处理数据库冗余数据的db_clean.py 整合进爬虫文件 保证线上使用一直有数据