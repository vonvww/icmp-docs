### 掌上办公集群服务器01 ###

#### 主要运行的应用服务
- 掌上办公nginx代理服务
- 掌上办公tomcat服务
- 掌上办公mysql服务

### 定时任务 ###

```
#nginx日志切割
59 23 * * * /opt/task/cut_nginx_log.sh > /dev/null 2>&1

#自动判断容器启动
*/5 * * * * /opt/task/start_docker.sh >> /opt/task/log/start_docker.log

#删除30天之前的tomcat日志
00 12 * * * /opt/script/del_tomcat_log.sh > /dev/null 2>&1
```

### docker 部署命令 ###

> 先将对应目录拷贝至服务器对应目录下,执行以下命令：

```
cd /opt/docker/icmp/
docker-compose up -d
```