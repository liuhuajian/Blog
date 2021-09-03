# BAT与adb联合使用
### 提示用户光标输入日志名，导出指定日志名
~~~
@echo off
echo 请输入文件名：
set /p a=

adb logcat -v threadtime > C:\Users\User\Desktop\%a%.txt

pause
~~~

### 获取时间戳
~~~
日期截取遵从格式 %date:~x,y%，表示从第x位开始，截取y个长度(x,y的起始值为0)

年份从第0位开始截取4位，月份从第5位开始截取2位，日期从第8位开始截取2位

时间截取遵从格式 %time:~x,y%，表示从第x位开始，截取y个长度(x,y的起始值为0)

时钟从第0位开始截取2位，分钟从第3位开始截取2位，秒钟从第6位开始截取2位
~~~

~~~
@echo off
set da=%date%
set time=%time%
set yyyy=%date:~3,4%
set mm=%date:~5,2%
set dd=%date:~8,2%
set hh=%time:~0,2%
set MM=%time:~3,2%
set ss=%time:~6,2%
echo yyyy:%yyyy%
echo mm:%mm%
echo dd:%dd%
echo hh:%hh%
echo MM:%MM%
echo ss:%ss%
pause
~~~
