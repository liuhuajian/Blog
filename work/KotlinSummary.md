## 一、协程（Coroutine）

## 二、集合
可变集合和不可变集合
```
private var disposable = mutableListOf<Disposable>()

private var mNotifyStrokeData: List<NotifyStroke> = mutableListOf()
```
## 三、基础操作符
```
1. run、with、let、also、apply 的比较 
2. takeIf、takeUnless、repeat 的使用 
3. 异常类的使用
```
![过程](../asset/kotlin_process.png)

## 四、关键字使用
### [object](https://blog.csdn.net/xlh1191860939/article/details/79460601)
1. 对象声明（Object Declaration）(单例模式)<br>
**原理**：object declaration的类最终被编译成：一个类拥有一个静态成员来持有对自己的引用，并且这个静态成员的名称为INSTANCE，当然这个INSTANCE是单例的，故这里可以这么去使用。
2. 伴生对象（Companion Object）<br>
companion object {}中用来修饰 静态常量，或者静态方法，单例等等
伴生对象可以理解为内部类
3. 对象表达式（Object Expression）



## 总结：
1. apply和run的区别：apply返回<font color="#f00">对象本身</font>，而run返回最后一行的值，场景不同
2. 集合数组可以使用last()获取最后一个对象，例如<br>
```
mLampEffectSet.takeIf { it.isNotEmpty() }?.run {
            return lampEffect.level <= last().level && last().level != -1
        } ?: return true
```
3. 如何在不使用if进行条件判断，即链式处理
```
item.info.optString("itemid")?.apply {
            //itemid不为空的时候执行
        }.apply {
            //itemid为空的时候执行
        }
```