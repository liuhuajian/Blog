### 修改系统虚拟键状态
```
Adb shell<br>
Adb pull system/build.prop 
```
### 去对应文件修改配置-->用户/User/build.prop-->qemu.hw.mainkeys=1 0/显示 1/隐藏
```
Adb root<br>
Adb remount<br>
Adb push build.prop system<br>
Adb shell<br>
Chmod 600 system/build.prop<br>
Reboot<br>
```
### 命令控制
```
Adb shell input keyevent <key><br>
Key-->4返回<br>
Key-->3 回到桌面<br>
```

### 通过包名+类名打开应用
```
adb shell am start -n + 包名/.类名
```

### 查看手机cpu架构
```
adb shell getprop ro.product.cpu.abi
```

### 临时设置端口号
```
Adb tcpip 5555
```

### 查看已装应用列表
```
adb shell pm list package
```

### 查看已知包的具体信息，比如清单文件信息等
```
adb shell dumpsys package XXX
```

### 查看当前app的入口
```
adb shell dumpsys window windows | findstr "Current"
```

### 杀死某个进程
```
adb shell dumpsys window windows | findstr "Current"
```

### 截屏
```
adb screencap -p /sdcard/xxx.png
```

### 控制网络状态
```
adb shell
打开网络
svc wifi enable

关闭网络
svc wifi disable

打开蓝牙
svc bluetooth enable

关闭蓝牙
svc bluetooth disable

```

### log日志相关
```
adb shell 
抓取日志到指定文件
logcat -v time > C:\Users\User\Desktop\logcat.txt

```

### 系统属性写入和读取
``` 

获取XXX属性值：adb shell getprop persist.XXX
设置XXX属性值：adb shell setprop persist.XXX

```

### 拉取手机指定位置文件到桌面
```
adb pull /storage/sdcard0/DCIM/Camera/picture.jpg C:\Users\User\Desktop\
```

### 上传桌面文件到外置存储卡
```
adb push C:\Users\User\Desktop\xiaokang.jpg /storage/sdcard0/DCIM/Camera/
```