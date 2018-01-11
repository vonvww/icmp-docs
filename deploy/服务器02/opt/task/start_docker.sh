#!/bin/bash

export PATH=/opt/docker:/opt/jdk1.8.0_111/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
nginx=$(docker ps -a|awk '/Up/{print}'|grep 'https_isj-nginx_1'|wc -l)

if 
   [ $nginx == 0 ];then
   echo `date`----- 'https_isj-nginx_1 is down'
   docker restart https_isj-nginx_1
fi

sleep 3
