APP 热部署服务
============

按照 [README](/hot-code/README.md) 文档中步骤即可完成项目 APP 热部署操作，其中：

1. 操作步骤第一步，需核对或调整 /opt/docker/ihos/nginx_proxy/hc/[update.sh](/hot-code/update.sh) 中参数为如下所示内容
    ```
#!/bin/bash

if [ ! -n "$1" ];
then
    echo "Need to pass version number"
    exit 1;
fi

WORKDIR=/opt/docker/ihos/nginx_proxy/hc
HC_HOME=/hc_grey
HC_BAK_HOME=/hc_grey
TC_HOME=SJ_ZssjV4
TC_SERVER=https://cloud.propersoft.cn/teamcities

if [ "$1" == "--release" ];
then
    HC_HOME=/hc_new
    HC_BAK_HOME=/hc_new_bak
    TC_HOME=IHos_App
fi


if [ "$1" == "--old" ];
then
    HC_HOME=/www
    HC_BAK_HOME=/www_bak
    TC_HOME=SJ_AppMasterSJH
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
    ```  

> 正式版可直接执行：./update --release

1. 操作步骤第二步，可至 [掌上就医项目 TeamCity](https://cloud.propersoft.cn/teamcities/) 在 `app正式热部署` 最后一次成功的构建中找 `Artifacts` URL 里的 `buildId`
2. 发布后验证地址如下，可通过 `release` 后面的时间戳判断是否已成功发布（时间戳可能会有时区问题，需 +8 小时）
    * 灰度版：[http://192.168.1.101/hc_new/chcp.json](http://192.168.1.101/hc_new/chcp.json)
    * 正式版： [http://192.168.1.101/hc_new/chcp.json](http://192.168.1.101/hc_new/chcp.json)