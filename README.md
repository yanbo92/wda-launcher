# WDA-LAUNCHER

## 项目介绍
wda_launcher顾名思义是用来启动WebDriverAgent的工具，名字是我瞎起的。具体功能是在无Python环境的电脑上，运行一个XCTest会话，Target是WebDriverAgent，启动后将支持Appium以及Airtest等iOS端UI自动化。该项目打包了Python环境以及tidevice库，换言之如果你的电脑上有Python环境并且安装了tidevice，即可通过以下命令达成同样的效果
```
tidevice -u [手机udid] wdaproxy -p [端口号]
```


## 准备工作
- 首先，如果你使用的是Windows电脑，你需要安装iTunes或者爱思助手，他们会帮你安装一些必须的依赖，比如Usbmuxd。
- 其次，运行该程序需要手机上装有WebDriverAgentRunner，通常跑过自动化的手机都会有（不包括Monkey）。它长这样：


## 下载
进入Release页面选择对应的系统文件下载即可


## 运行
- 你可以直接双击运行，如果只识别到一台连接的iPhone手机，将会在这台手机上开启WebDriverAgent服务，并转发到电脑的8100端口
- 当然，最好的方式还是开一个命令行窗口，将文件拉入。这样就可以传入自定义的手机id、端口号等，具体参数说明见下方。


## 接受参数
- udid，指定具体某台手机，默认为空，即让tidevice自行识别，示例：
```
wda_launcher_mac --udid 00008030-000C44D00279802E
```

- port，指定具体要转发的端口，指电脑本机的端口，默认为8100，示例：
```
wda_launcher_mac --port 8200
```

- bundleid，要启动XCTest的包名，默认为`com.*.WebDriverAgentRunner.xctrunner`，包含通配符`*`，示例：
```
wda_launcher_mac --bundleid com.facebook.WebDriverAgentRunner.xctrunner
```
  

