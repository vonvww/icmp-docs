#!/bin/bash

if [ ! -n "$1" ];
then
    echo "Need to pass version number"
    exit 1;
fi

WORKDIR=/opt/docker/icmp/nginx_proxy/hc
HC_HOME=/hc_grey
HC_BAK_HOME=/hc_grey
TC_HOME=Icmp_App1
TC_SERVER=https://cloud.propersoft.cn/teamcities

if [ "$1" == "--release" ];
then
    HC_HOME=/hc_new
    HC_BAK_HOME=/hc_new_bak
    TC_HOME=Icmp_App1
fi


if [ "$1" == "--old" ];
then
    HC_HOME=/www
    HC_BAK_HOME=/www_bak
    TC_HOME=Icmp_App1
fi

cd $WORKDIR
URL=$TC_SERVER/guestAuth/repository/downloadAll/$TC_HOME/lastSuccessful/artifacts.zip
echo 'Downloading from '$URL
curl -O $URL
if [ -e $WORKDIR/artifacts.zip ];
then
    rm -rf $WORKDIR$HC_BAK_HOME
    mv $WORKDIR$HC_HOME $WORKDIR$HC_BAK_HOME
    echo 'Unziping artifacts.zip...'
    unzip -qq $WORKDIR/artifacts.zip -d $WORKDIR$HC_HOME -x *.apk
    rm -f $WORKDIR/artifacts.zip
    echo 'Done'
fi
