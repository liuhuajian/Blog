## 1、问题
--- 打release包 提示gc limit<br>
## 解决方法：
内存不足，需要新建gradle.properties文件，加上这一行：<br>org.gradle.jvmargs=-Xms1024m -Xmx1024m -Xmx1536M

## 2、问题
--- 电脑断点导致Android studio环境异常，打开java文件出现标签化的乱码
思路：

## 解决方法：

1.关闭Android studio<br>
2.打开 C:\Users\UserName.android 删除build-cache<br>
3.打开 C:\Users\UserName.AndroidStudio3.2\system<br>
删除以下文件夹<br>
caches<br>
compiler<br>
compile-server<br>
conversion<br>
external_build_system<br>
frameworks<br>
gradle<br>
resource_folder_cache<br>
4.如果Android studio中的java文件突然出现标签化的乱码，并且修改编码格式无效，也可以试一下以上方法。

## 3、问题
将手机中的文件copy到电脑桌面上
## 解决方法：
adb -s 设备号 pull /mnt/sdcard/XXX C:\Users\User\Desktop\

## 4、问题
build variants切换到release无法通过编译<br>
提示：<br>
```
Could not get unknown property 'release' for SigningConfig container of type
 org.gradle.api.internal.FactoryNamedDomainObjectContainer.
```
## 解决办法：
` 1、检查是否有signingConfigs {}。`<br>
`2、将signingConfigs{} 放在 buildTypes{}的前面即可`

## 5、问题
Android 8.0: java.lang.IllegalStateException: Not allowed to start service Intent<br>
提示：<br>
```
Android 8.0 还对特定函数做出了以下变更：
 
（1）如果针对 Android 8.0 的应用尝试在不允许其创建后台服务的情况下使用 startService() 函数，
     则该函数将引发一个 IllegalStateException。新的 Context.startForegroundService() 函数将启动一个前台服务。
 
（2）即使应用在后台运行，系统也允许其调用 Context.startForegroundService()。不过，
    应用必须在创建服务后的五秒内调用该服务的 startForeground() 函数。
```
```
```