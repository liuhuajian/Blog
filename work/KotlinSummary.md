# 一、协程（Coroutine）
**参考**<br>
[Kotlin协程笔记](https://www.jianshu.com/p/8dc8abca50e3)
```
GlobalScope.launch(Dispatchers.Main) {
    MyLogger.e("run start11111")
    val name = async(Dispatchers.IO) {
        getName()
    }
    val sex = async(Dispatchers.IO) {
        getSex()
    }
    val age = async(Dispatchers.IO) {
        getAge()
    }
    MyLogger.e("run start22222")
    val info = name.await() + sex.await() + age.await()
    MyLogger.e("info-->$info")
    ToastUtil.getInstance().showToast(info)
}

suspend fun getName():String{
    delay(1000)
    MyLogger.e("name-->liuhuajian")
    return "liuhuajian"
}        
```
**三种启动方式**
1. runBlocking:T     

2. launch:Job

3. async/await:Deferred

# 二、集合
![list](../asset/img3.png)


### 常用for循环
**遍历1-100的数值，包括1和100**
```
for (index in 1..100){
            print(index)
        }
```
**倒序遍历**
```
for (index in 100 downTo 1){
            print(index)
        }
```
**更改遍历的步长**
```
 for (index in 1..100 step 2){
            print(index)//会输出1..3..5......
        }
```
**不包含末尾元素**
```
for (index in 1 until 10){
            println(index)//输出0..9
        }
```
**遍历一个数组/列表，想同时取出下标和元素**
```
 val array = arrayOf("a", "b", "c")
        for ((index,e) in array.withIndex()){
            println("下标=$index----元素=$e")
        }
```
**遍历一个数组/列表，只取出下标**
```
val array = arrayOf("a", "b", "c")
        for (index in array.indices){
            println("index=$index")//输出0，1，2
        }
```
**遍历取元素**
```
val array = arrayOf("a", "b", "c")
        for (element in array){
            println("element=$element")//输出a,b,c
        }
```

# 三、类与对象
## 关键术语
```
主构造函数、次构造函数、初始化代码块

open
```


# 四、基础操作符
### 关键字返回值
![过程](../asset/img2.png)
```
1. run、with、let、also、apply 的比较 
2. takeIf、takeUnless、repeat 的使用 
3. 异常类的使用
```
![过程](../asset/img1.png)

### <b>一元操作符</b>
操作符|函数
-----|------
!a | a.not()
a++ | a.inc()
a-- | a.dec()

### <b>二元操作符</b>
操作符|函数
-----|------
a + b | a.plus(b)
a - b | a.minus(b)
a * b | a.times(b)
a / b | a.div(b)
a % b | a.mod(b)

### <b>构造函数</b>
主构造函数、次构造函数、init初始化
~~~
关键字constructor：在Java中，构造方法名须和类名相同；而在Kotlin中，是通过constructor关键字来标明的，且对于Primary Constructor而言，它的位置是在类的首部（class header）而不是在类体中（class body）。

关键字init：init{}它被称作是初始化代码块（Initializer Block），它的作用是为了Primary Constructor服务的，由于Primary Constructor是放置在类的首部，是不能包含任何初始化执行语句的，这是语法规定的，那么这个时候就有了init的用武之地，我们可以把初始化执行语句放置在此处，为属性进行赋值。
~~~

### <b>延迟属性 lazy</b> 
~~~
lazy() 是接受一个lambda 并返回一个 Lazy <T> 实例的函数，返回的实例可以作为实现延迟属性的委托。也就是说：
第一次调用get() 会执行已传递给 lazy() 的 lambda 表达式并记录结果， 后续调用get() 只是返回记录的结果。
~~~

延迟属性Lazy 与 lateinit 区别
~~~
lazy { ... }代表只能用于val属性，而lateinit只能用于var，因为它不能编译到final字段，因此不能保证不变性;

lateinit var具有存储值的后备字段(backing field)，而by lazy { ... }创建一个委托对象，其中存储一次计算的值，将对代理实例的引用存储在类对象中，并为与委托实例一起使用的属性生成getter。
~~~

### <b>成员变量 自定义getter</b> 
如果我们定义了一个自定义的 getter，那么每次访问该属性时都会调用它
~~~
val isEmpty: Boolean
    get() = this.size == 0
~~~

### <b>类型检测 is</b>

### <b>使用区间</b>
使⽤ in 运算符来检测某个数字是否在指定区间内，step运算符指步骤
~~~
val x = 10
val y = 9
if (x in 1..y+1 step 2) {
    println("fits in range")
}
~~~

### <b>泛型</b>
~~~
1. in out

如果泛型类只将泛型类型作为函数的入参（输入），那么使用 in：

interface Consumer<in T> {
    fun consume(item: T)
}

如果泛型类只将泛型类型作为函数的返回（输出），那么使用 out：

interface Production<out T> {
    fun produce(): T
}

~~~

# 五、关键字使用
## [object](https://blog.csdn.net/xlh1191860939/article/details/79460601)
1. 对象声明（Object Declaration）(单例模式)<br>
**原理**：object declaration的类最终被编译成：一个类拥有一个静态成员来持有对自己的引用，并且这个静态成员的名称为INSTANCE，当然这个INSTANCE是单例的，故这里可以这么去使用。
2. 伴生对象（Companion Object）<br>
companion object {}中用来修饰 静态常量，或者静态方法，单例等等
伴生对象可以理解为内部类
3. 对象表达式（Object Expression）

## vararg
vararg是可变长度参数


# 六、总结：
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
4. 如果有let、also这两个identifier为it的符号嵌套使用，怎么使用不同的层级的内容<br>
可以在方法体内添加data ->标识符，使用data变量
```
                    recyclerview_recommond?.getmNewsAdapter()?.data?.let {
                        data ->
                    }

                    错误示范：
                    recyclerview_recommond?.getmNewsAdapter()?.data?.run {
                        data ->
                    }
```
run、apply、let、also这四种操作符，只有<font color="#f00">let 和also</font>可以使用