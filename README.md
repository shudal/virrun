# 关于本软件			

实现自动改变[夜深模拟器]GPS定位，而非手动更改。

### 原理 

* 夜神安卓模拟器自带修改GPS位置功能
* python3调用pywin32库，通过模拟输入，模拟点击，实现自动修改夜神安卓模拟器GPS定位

### 用途

* 学习python3开发与windows api的简单实用

### 使用环境 

* windows系统
* 下载并安装[夜神安卓模拟器]

### 使用步骤示例

- 打开[夜神安卓模拟器]

- 打开侧边栏的[虚拟定位],手动将位置设置到【起点】

  关于【起点】
  默认路径的起点如图
  ![](https://perci-1253331419.cos.ap-chengdu.myqcloud.com/apps/lepao/ori.png)

请勿关闭这个[位置设置]窗口

- 打开[步道乐跑]等软件，登录上后，点击[进入乐跑]->点击[进入乐跑]->点击[开始跑步]

- 运行darvin.exe

- 其他：

  - 如有需要，可以更改config.ini中的配置(鼠标右键以记事本打开config.ini)

  ```
  config.ini中
  mishu 表示跑步总路程，单位为米，最后跑出来的结果只可能少，所以稍微填写大一点
  speed 表示跑步速度，单位为秒，仅表示大概，并不精确
  -----------------
  跑步轨迹为矩形，如需自己设定此矩形的四个点，可在config.ini里的[point]下新增。
  比如新增一个叫做rec的矩形，则config.ini中新增以下两行
  rec_wei = 这里照格式填写四个点的纬度
  rec_jing= 这里照格式填写四个点的经度
  填写的顺序是： 
  	右下角的点，左下角的点，左上角的点，右上角的点。
  其中，经纬度可通过夜深模拟器的位置设置查看到
  ```

  ### 其他

  暂无





