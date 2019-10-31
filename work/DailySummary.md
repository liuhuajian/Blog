## 问题
1、打release包 提示gc limit<br>
思路：内存不足，需要新建gradle.properties文件，加上这一行：<br>org.gradle.jvmargs=-Xms1024m -Xmx1024m -Xmx1536M
