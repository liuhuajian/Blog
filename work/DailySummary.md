## <b>1、问题</b>
--- 打release包 提示gc limit<br>
## 解决方法：
内存不足，需要新建gradle.properties文件，加上这一行：<br>org.gradle.jvmargs=-Xms1024m -Xmx1024m -Xmx1536M

## <b>2、问题</b>
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

## <b>3、问题</b>
将手机中的文件copy到电脑桌面上
## 解决方法：
adb -s 设备号 pull /mnt/sdcard/XXX C:\Users\User\Desktop\

## <b>4、问题</b>
build variants切换到release无法通过编译<br>
提示：<br>
```
Could not get unknown property 'release' for SigningConfig container of type
 org.gradle.api.internal.FactoryNamedDomainObjectContainer.
```
## 解决办法：
` 1、检查是否有signingConfigs {}。`<br>
`2、将signingConfigs{} 放在 buildTypes{}的前面即可`

## <b>5、问题</b>
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

## <b>6、问题</b>
## 如何获取当前进程处于前台
### 方法一：使用ActivityLifecycleCallbacks
```
        ActivityManager am = (ActivityManager) App.mContext.getSystemService(Context.ACTIVITY_SERVICE);
        //获取到当前正在运行的任务栈
        List<ActivityManager.RunningTaskInfo> tasks = am.getRunningTasks(1);//参数是想获得的个数，可以随意写
        //获取到最上面的进程
        ActivityManager.RunningTaskInfo taskInfo = tasks.get(0);
        //获取到最顶端应用程序的包名
        String pName = taskInfo.topActivity.getPackageName();
        boolean isForeground = context.getPackageName().equals(pName);
```

## <b>7、问题</b>
### kotlin
1. 直接用xml中的id作为控件使用，会有空指针的情况，个别情况还是用findviewbyId()

## <b>8、问题</b>
1. 如何将recyclerview滚动到顶部
### 解决办法：
```
var position = 0
        var firstPosition = (recyclerViewMusicList?.layoutManager as LinearLayoutManager).findFirstVisibleItemPosition()
        adapter?.data?.run {
            for (index in this.indices) {
                if (this[index].songname == title) {
                    position = index
                    break
                }
            }
        }
if (position > firstPosition && position < firstPosition + 5) {
            //如果当前播放的item是在屏幕中，那么无需滚动到顶部
            return
        }
MyLogger.d("position-->$position")

//TopSmoothScroller 继承LinearSmoothScroller

var smoothScroll = TopSmoothScroller(this)
smoothScroll.targetPosition = position
recyclerViewMusicList.layoutManager?.startSmoothScroll(smoothScroll)
</color>
```

### <b>9、问题</b>
## Unable to start adb server: error: protocol fault (couldn't read status): Connection reset by peer

~~~
情况出现：

打开androidstudio，一直连接不上电脑，提示：Unable to start adb server: error: protocol fault (couldn't read status): Connection reset by peer

问题原因：

大多数情况是5037端口被占用。5037为adb默认端口。

解决办法：
查看哪个程序占用了adb端口，结束这个程序，然后重启adb就好了。
使用命令：netstat -aon|findstr "5037"  找到占用5037端口的进程PID。

使用命令：tasklist|findstr "5440"  通过PID找出进程。
调出任务管理器，找到这个进程，结束进程。
使用命令:adb start-server 启动adb就行了
~~~
![process1](../asset/process1.png)
![process1](../asset/process2.png)

### <b>10、将activity设置成dialog样式，但是会有默认背景色，需要移除</b>

~~~
    <style name="dialog_style" parent="@style/AppTheme">
        <!--是否悬浮在activity上-->
        <item name="android:windowIsFloating">true</item>
        <!--透明是否-->
        <item name="android:windowIsTranslucent">true</item>
        <item name="android:background">@null</item>
        <!--设置没有窗口标题、dialog标题等各种标题-->
        <item name="android:windowNoTitle">true</item>
        <item name="android:title">@null</item>
        <item name="android:dialogTitle">@null</item>
    </style>

~~~

解决办法：在样式上设置windowBackground为透明

~~~
        <item name="android:windowBackground">
        @color/transparent
        </item>
~~~

### <b>11、项目涉及到谷歌服务，长时间无法加载</b>
将google()和jcenter()替换成阿里云镜像
~~~
//google()
//jcenter()
maven { url 'https://maven.aliyun.com/repository/google' }
maven { url 'https://maven.aliyun.com/repository/jcenter' }
maven { url 'http://maven.aliyun.com/nexus/content/groups/public' }
~~~

### <b>12、double类型数值过大变成科学计数型，如何完整显示</b>
通过DecimalFormat("0").format方式转换一下
~~~
val completeDoubleValue = DecimalFormat("0")
.format(1.5827148E12).toLong()
~~~

### <b>13、用Gson将字符串转化为List<T></b>
~~~
 val type = object :TypeToken<List<TongueFaqs>>(){}.type
 val data = Gson().fromJson<List<TongueFaqs>>(DataConfig.QUESTION_FAQS,type)
~~~

### <b>14、监听用户按下操作</b>
在activity中监听回调onUserInteraction方法即可

### <b>15、将对象通过Gson().toJson()转换为字符串后无法通过jsonObject()方式获取到</b>
解决办法：将对象字符串放到jsonObject参数中，例如
new JsonObject(对象字符串)

### <b>16、对日期进行格式化</b>
String.format("%d-%02d-%02d", year, month, day)
位数不足两位自动补0

### <b>17、WindowManager弹窗处于底部时添加margin边距</b>
~~~
val layoutParam = WindowManager.LayoutParams()
layoutParam.gravity = Gravity.BOTTOM
layoutParam.y = 30
~~~
给y属性设置30值

### <b>18、NestedScrollView的滚动监听,滚动到指定位置</b>
1. 滚动到底部
~~~
 svscrollouter.fullScroll(NestedScrollView.FOCUS_DOWN);
~~~
2. 滚动到顶部
~~~
svscrollouter.fullScroll(NestedScrollView.FOCUS_UP);
~~~

### <b>19、代码设置view的圆角</b>
~~~
rectangle.outlineProvider = object : ViewOutlineProvider(){
    override fun getOutline(view: View, outline: Outline) {
        outline.setRoundRect(0, 0, view.width, view.height, 40f);
    }
}
rectangle.clipToOutline = true
~~~

### <b>20、JSON获取null数据时直接得到null字符串</b>
解决办法：
~~~
1、用实体类来解析
2、将json中的null替换为空字符串
~~~

### <b>21、颜色值设置可变ARGB值
~~~
将ARGB颜色值拼接：
int color = (A & 0xff) << 24 | (R & 0xff) << 16 | (G & 0xff) << 8 | (B & 0xff);


获取每一位的值：
int A = (color >> 24) & 0xff; // or color >>> 24
int R = (color >> 16) & 0xff;
int G = (color >>  8) & 0xff;
int B = (color      ) & 0xff;
~~~

### <b>22、Android studio 一直卡在Gradle:Build Running
~~~
将maven地址从谷歌换成阿里云镜像

maven { url 'http://maven.aliyun.com/nexus/content/groups/public/'}
~~~

### <b>23、adb 将日志输出到指定目录，日志中出现乱码
~~~
进入控制面板的区域窗口，勾选使用UTF-8提供能全球语言支持
~~~