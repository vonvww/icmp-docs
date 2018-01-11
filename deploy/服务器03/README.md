### 掌上就医集群服务器03 ###

#### 主要运行的应用服务
- 掌上就医tomcat服务
- HIS 的 Web Service [反向代理](./服务器03/opt/docker/ihos/nginx/nginx.conf) 服务
- 掌上就医mongos服务
- 掌上就医mongo集群部分服务
- 掌上就医redis缓存服务
- HIS 的 Web Service反向代理nginx定时任务，日志按天分割，及日志保留天数策略

### 定时任务 ###

```
#备份HIS Web Service nginx日志
10 1 * * * /opt/backup/nginx/backup.sh

#zabbix 监控IO
*/1 * * * * /usr/bin/iostat -k -x -d 1 3 >/data/zabbix/iostat_output 2>&1

#删除30天之前的tomcat日志
00 12 * * * /opt/script/del_tomcat_log.sh > /dev/null 2>&1
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