### 掌上办公集群服务器02 ###

#### 主要运行的应用服务
- 掌上办公tomcat服务
- 掌上办公mysql从服务
- zabbix监控服务，对各服务器及应用监控
- 掌上办公mysql每天备份定时任务

### 定时任务 ###

```
#备份mysql数据库
00 04 * * * /data/backup/mysql/mysql_backup.sh

#自动判断容器启动
*/5 * * * * /opt/task/start_docker.sh >> /opt/task/log/start_docker.log

#删除30天之前的tomcat日志
00 12 * * * /opt/script/del_tomcat_log.sh > /dev/null 2>&1
```

### docker 部署命令 ###

> 先将对应目录拷贝至服务器对应目录下,执行以下命令：

```
cd /opt/docker/ihos/
docker-compose up -d
```