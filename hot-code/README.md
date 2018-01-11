APP 热部署服务
============

1. 修改 [update.sh](./update.sh) 中的相关参数
1. 从 TeamCity 中找到要部署版本的构建成果物（Artifacts），点击进入 `Artifacts` 界面后，查看 URL 地址，从中得到 `buildId` 的参数
1. 在服务器相应路径中，执行 `./update.sh $buildId` 即可完成 **debug** 版的发布。以 `buildId` 是 `156` 为例，要进行 `debug` 版的发布时，执行`./update.sh 156`
    > 注意：如果要进行新版的**正式发布**，需增加 `--release` 参数，如 `$ ./update.sh --release`
1. 发布完成后，注意验证是否生效。**若未生效，需重启容器使生效**。
