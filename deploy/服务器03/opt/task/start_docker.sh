#!/bin/bash

export PATH=/opt/docker/docker:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

nginx=$(docker ps -a|awk '/Up/{print}'|grep 'isjofficial_isj-nginx_official_1'|wc -l)

if 
   [ $nginx == 0 ];then
   echo `date`----- 'isjofficial_isj-nginx_official_1 is down'
   docker restart isjofficial_isj-nginx_official_1
fi

sleep 3
