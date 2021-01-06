### 爬虫部分

- [ ] 爬虫从 文档`spider-task`中获取目标任务

```[json]
{
    "task":[], // -> list()
}
```
- [ ] 爬虫将获取到的数据写入到`spider-result`中

```[json]
{
    "city":"", // -> string()
    "updateTime":"", // -> datetime()
    "result":[] // -> list()
}
```
- [ ] 爬虫默认每天启动一次 每次抓取时长间隔为30s 抓取深度为20个Page
- [ ] 租房数据超过30天的视为冗余数据 清理