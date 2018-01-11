### 掌上就医集群服务器02 ###

#### 主要运行的应用服务
- 掌上就医mysql主服务
- 掌上就医mongos服务
- 掌上就医mongo集群部分服务
- 长期保存查看日志的mongo服务
- zabbix监控服务，对各服务器及应用监控
- 掌上就医mysql每天备份定时任务
- 掌上就医请求his日志每天备份定时任务，并把每天备份的日志复制到长期保存日志的mongo中
- 掌上就医redis缓存slave服务

### 定时任务 ###

```
#备份mysql数据库
00 04 * * * /data/backup/mysql/mysql_backup.sh

#备份mongo数据库
00 05 * * * /data/backup/mongo/mongo_backup.sh

#获取创建时间超过一天且仍处于未支付状态的挂号单
00 */5 * * * /opt/task/mongo/mongo_count_registration.sh

#zabbix 监控IO
*/1 * * * * /usr/bin/iostat -k -x -d 1 3 >/data/zabbix/iostat_output 2>&1

#导出ws_log
15 2 * * * /opt/backup/mongo/backup.sh

#导入ws_log
45 2 * * * /opt/backup/mongo/wsLogImp.sh
```

### docker 部署命令 ###

> 先将对应目录拷贝至服务器对应目录下,执行以下命令：

```
cd /opt/docker/ihos/
docker-compose up -d
```

> 待所有mongo集群启动成功后执行以下命令：

```
cd /opt/docker/ihos/mongos/
docker-compose up -d
```