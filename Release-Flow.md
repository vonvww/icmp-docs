移动应用版本发布步骤
=================

### 构建安卓新版应用

1. 确定发布版应用版本，修改 `custom_contents/customs.json` 中相应项目版本号。版本号使用数值形式即可，例 `3 02 00` 对应版本 `3.2.0`。

1. 修改 [持续集成环境](https://cloud.propersoft.cn/teamcities/) 相应构建项目配置中的 `General Settings`，将 `Build counter` 调整为上述版本号数值形式，作为**新版本的起始构建序号**。

1. 调整持续集成环境 `Build Features` 中的 `File Content Replacer`，将 `Find what` 参数配置为**新版本的起始构建序号**。

1. 打 tag，如：

    ```
    # 先在本地打 tag，注意修改 tag 名
    $ git tag v3.2.0-sj-app
    # 将标签推送至远程仓库
    $ git push upstream v3.2.0-sj-app
    ```

1. 在仓库的 [releases](https://github.com/propersoft-cn/ihos/releases) 中，[Draft a new release](https://github.com/propersoft-cn/ihos/releases/new)，选择新推上来的发布标签，编写发版说明。

### iOS 发布新版应用

1. 拉取 `app-dev` 分支最新代码，然后按照构建步骤生成 iOS 平台代码。

   ```
   $ npm install
   $ bower install
   $ grunt build:releaseIOS
   $ ionic state reset
   $ ionic build ios
   ```

    > 因为构建版本上传后不能够删除，所以当上传或审核的版本出现问题时，可以在 `iTunes Contect` 中修改小版本号，以保证发布的大版本号不发生变化。

1. 发布时，在 Xcode 中打开 `PushNotification` 开关。
1. 填写发布信息时需要将发布支持的 iOS 系统选择 `iOS 9`。
1. 利用xCode或者命令行打包后的ipa文件需要上传至 iTunes Connect 中，需要使用工具 [application Loader](https://itunesconnect.apple.com/apploader/ApplicationLoader_3.0.dmg),使用拥有发布权限的账户进行登录。
1. 发布人员需要登录到iTunes Connect进行应用管理，[iTunes Connect](https://itunesconnect.apple.com)，创建好版本号（例如:3.3.0）后，在【此版本的新增内容】中填写相应的更新内容，在【构建版本】中选择通过 application Loader 上传的应用。
1. 点击右上角的保存，然后点击【发布此版本】
1. 在下一个页面的两个选项都选择否，再点击发布。至此完成了ios的APP的发布新版应用的步骤

### 更新热部署代码

[APP 热部署服务更新说明](./hot-code)

> **重要！勿忘记此步骤，否则新版上线后会被退回到之前版本！**

### 发布应用内更新通知

1. 通过 [应用宝](http://sj.qq.com) 找到已经发布在应用宝中的 [掌上盛京医院](http://sj.qq.com/myapp/detail.htm?apkName=com.proper.soft.mobile.isj)，并将下载地址记录下来。
1. 通过 `curl` 命令发版

```
$ curl -H "Content-Type:application/json" -H "Authorization:eyJpZCI6InBlcC1zeXNhZG1pbiIsIm5hbWUiOiJhZG1pbiJ9.eyJlbXBOYW1lIjpudWxsLCJyb2xlcyI6bnVsbH0.K_vRoOmRIONJUCvkI3ohDQSvYx4fESffbFiC5Lhtxbc" -X PUT -d '{"ver":301022, "note":" 版本号：3.1.0：1. 重新开放一网通支付方式，更多支付方式，更加方便快捷2. 挂号单中支付、确认及退款状态更详细3. 挂号单分类，更容易找到未就诊的挂号单4. 挂号时如有未支付的挂号单，可直接跳转至未支付页面进行支付5. 对性能进行优化，更节省流量", "url":"http://42.202.141.13/imtt.dd.qq.com/16891/4C2A85DABF7AEDD5408FE554CC3D5E26.apk?mkey=5852799b924608ce&f=b25&c=0&fsname=com.proper.soft.mobile.isj_3.1.0_301022.apk&csr=4d5s&p=.apk"}' https://sjh.sj-hospital.org/isj/app/latest
```

### 新版更新统计

找到 nginx 访问日志所在路径，从新版发布日期日志开始进行统计，如：

    $ cat req_stat_2017-03-08.log req_stat_2017-03-09.log | grep /latest.*current=30200.*Bearer | awk '{print $5}' | awk -F "." '{print $1}' | sort | uniq | wc -l


