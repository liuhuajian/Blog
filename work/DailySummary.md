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