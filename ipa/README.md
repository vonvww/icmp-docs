# ipa打包 #

### 打包脚本 ###
- 执行机器需要先配置好开发者证书
- 需要先将工程内的[config.xml]文件的[widget id]修改成[com.neusoft.hcb.shengjing]
- 执行[ipaBuild.sh]生成ipa安装包
- 执行前需要根据本机实际情况调整脚本内的路径
- 打测试包使用[AdHocExportOptions.plist]文件，打发布包使用[AppStoreExportOptions.plist]文件
- 注：有新加入的手机设备时，需要同时修改配置文件，并下载安装到本地后，再进行打包

### 证书及Xcode配置使用文档 ###
- http://blog.csdn.net/jingyipo/article/details/51596135

### xcodebuild命令使用文档 ###
- http://www.jianshu.com/p/bd4c22952e01
- http://blog.csdn.net/potato512/article/details/52172107
- http://blog.csdn.net/hjy323599/article/details/51869519
