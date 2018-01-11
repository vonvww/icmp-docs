#!/bin/bash

cut_date=$(date +"%Y%m%d_%H%M%S")
nginx_log_path=/opt/https/log
nginx_backup=/data/logs/nginx_backup
export TODAY_TIME=`date +%Y-%m-%d`


mv $nginx_log_path/req_stat.log $nginx_backup/req_stat_$TODAY_TIME.log
mv $nginx_log_path/req_slow.log $nginx_backup/req_slow_$TODAY_TIME.log
mv $nginx_log_path/error.log    $nginx_backup/error_$TODAY_TIME.log

/opt/docker/docker kill -s USR1 https_isj-nginx_1
/bin/gzip $nginx_backup/req_stat_$TODAY_TIME.log
/bin/gzip $nginx_backup/req_slow_$TODAY_TIME.log
/bin/gzip $nginx_backup/error_$TODAY_TIME.log

#删除nginx日志30天之前的
find $nginx_backup -type f -name "*.gz" -mtime +30 | xargs rm -f
