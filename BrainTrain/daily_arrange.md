# 2019.11.01
## 安排
1. 零秒思考：10个问题
2. 工作内容安排
3. 标题记忆法和数字记忆法巩固

## 总结
1. 剩余主要的工作内容<br>
（1）家庭相册、视频通话、视频监控等bug处理<br>
（2）舌健康、视频通话、体脂秤、血压血糖、购物多轮技能语音处理<br>
（3）唤醒异常、无法识别等情况处理<br>
（4）灯光效果<br>
（5）小康转向情况处理<br>

# 2019.11.04
## 安排
1. 舌健康语音多轮
2. 爱奇艺、奇巴布跳转联调
3. 唤醒后小康转向
4. 添加国民健康宣传片
5. 视频监控bug处理

## 总结
1. 如何区分点击进入技能，还是语音进入技能（有些界面进入后会有语音提示，完毕后自动打开唤醒页面）
2. 唤醒和多轮交互图、未识别图需要区分开（<font color=#ff0000>未完成</font>）
3. 爱奇艺启动已经加好，需要另外加上退出、回到首页指令

## 职称业绩心得（提纲）<br>
（1）维聚的工作内容、工作成果、遇到的技术点以及如何克服的（辅助完成项目）<br>
（2）资腾的工作内容、成果、遇到的技术点以及如何克服（主导者）<br>
（3）国民健康、带屏小康、独立小康技术点<br>

* 六个方面考虑：
1. 参与的项目有何重大技术突破
2. 技术方面有没有遇到重大的问题，提出过哪些有建议的内容
3. 在实际工作中，运用专业知识解决过哪些技术问题，提出过哪些建议，取得什么效益，得到什么奖励
4. 写过哪些技术工作总结，对本部门有何影响
5. 在专业技术领域，有获得哪些知识产权（发明专利，应用专利）<br>

# 2019.11.05
## 安排
1. 多轮技能兼容语音进入以及点击进入
2. 奇巴布跳转（还未验证内容是否正确）
3. 推荐
4. 录屏、截屏、静音方式、录屏截屏数据上传到服务器（上传完删除该文件）
5. 灯效功能
6. 转向

## 总结
1. 推荐资讯完成
2. 跳转奇巴布、爱奇艺等三方技能，退出需要kill掉该技能
3. 奇巴布目前能跳转到搜索页，目前以下需求：只有资源名，需要进入搜索页，有资源名并带有集数，需要进入播放页（至于是否有资源，就是奇巴布自己的事情了）
4. 截屏已实现，录屏还未实现，静音等待融云解决bug，至于录屏、截屏资源上传功能，还<font color=#ff0000>未实现</font>
5. 灯效功能暂时未开始，需要祥哥帮忙
6. 唤醒转向完成，需要提高精确度

# 2019.11.06
## 安排（需要做）
1. 奇巴布跳转（还未验证内容是否正确）
2. 录屏、截屏消息如何发送，是走mqtt，还是融云？
3. 舌健康、体脂秤、血压血糖、购物多轮
4. 异常、多轮、唤醒弹窗需要区分开
5. 兼容融云单点登录（某些场景需要有弹窗提示）

## 总结
1. 奇巴布目前能跳转到搜索页，目前以下需求：只有资源名，需要进入搜索页，有资源名并带有集数，需要进入播放页（至于是否有资源，就是奇巴布自己的事情了）
2. 暂时是融云，需要确定下来
3. 舌健康目前已完成90，最后一步需要有精确的语料，体脂秤类似于舌健康，但是在称重的时候需要有语音提示，血压血糖需要调试，购物下周调试
4. 还未开始
5. 状态变更已判断，需要UI给出具体弹窗样式进行开发

# 2019.11.07
## 安排
1. 奇巴布测试
2. 截屏上传
3. 体脂秤、舌健康、血压血糖联调

## 总结
1. 完成（目前全搜索）
2. 已完成
3. 继续联调

# 2019.11.08
## 安排
1. 体脂秤、舌健康确保完成

## 总结
1. 体脂秤、舌健康、视频通话已完成

# 2019.11.09
## 安排
1. 血压、血糖多轮

## 总结
1. 设置page有风险，毕竟需要将值通过广播传递到桌面应用，可以考虑使用内容提供者，桌面从skillapp中获取数据
2. 如何结束掉爱奇艺和奇巴布等三方app
2. 血压问题点：<br>
①手动设置页面保存血压无效（是否要判断血压是否有值呢）<br>
②输入完两个血压值后，询问是否正确，说正确无效<br>
③血糖无法进入选择用户界面

# 2019.11.10
## 安排
1. 记录血压、查询血压功能完成

## 总结
1. 记录血压完成（当说不想记录的时候，进度条怎么设置为0）
2. 查询血压功能未校验

# 2019.11.11
## 安排
1. 记录血压、查询血压功能完成
2. 录屏倒计时动画设置
3. 购物多轮技能

## 总结
1. 备注：如果出现无法理解技能，尝试说退出后再使用
2. 购物多轮技能未知service，其余都ok，除了地址那块是否需要多轮交互，等待产品回复
3. 正常唤醒、无法识别、多轮三种语音输入弹窗需要分类

# 2019.11.12
## 安排
1. 体脂秤是否要重构
2. 正常唤醒、无法识别、多轮三种语音输入弹窗需要分类
3. 爱奇艺、奇巴布退出功能
4. 在桌面上的其他页面，返回时处理
5. 儿童急救
6. 话费余额判断
7. 静音功能采用禁用麦克风方案

## 总结
1. 体脂秤目前减少过滤条件后，CPU占用率减少到30%，页面不卡顿
2. <font color="#f00">还未实现</font>
3. <font color="#f00">还未实现</font>
4. <font color="#f00">还未实现</font>
5. <font color="#f00">还未实现</font>
6. <font color="#f00">还未实现</font>
7. 已实现

# 2019.11.13
## 安排
1. 正常唤醒、无法识别、多轮三种语音输入弹窗需要分类（未完成）
2. 爱奇艺、奇巴布退出功能（未完成）
3. 在桌面上的其他页面，返回时处理（未完成）
4. 儿童急救（未完成）
5. 话费余额判断（完成）
6. 桌面通用跳转技能工具类（完成）
7. 血压血糖添加查看历史功能（完成）

## 总结
1. 上述未完成需要解决
2. 通话记录时间需要进行细节调整
3. 桌面通用跳转技能工具类（完成）

# 2019.11.14
## 安排
1. 正常唤醒、无法识别、多轮三种语音输入弹窗需要分类（未完成）
2. 爱奇艺、奇巴布退出功能（未完成）
3. 在桌面上的其他页面，返回时处理（未完成）
4. 儿童急救（暂时延后）
5. 话费余额判断（完成）（先取消，还未有充值功能）
6. 血压血糖添加查看历史功能待测试（未完成）
7. 通话记录时间需要进行细节调整

## 总结
1. 独立小康混淆异常

# 2019.11.18
## 安排
1. 独立小康、带屏小康、桌面混淆打包后EventBus无法接受消息

## 总结
1. 替换EventBus第三方库，解决混淆后无法接收消息异常

# 2019.11.19
## 安排
1. 购物流程跳转
2. 邀请申请删除
3. 通知三个接口添加
4. 技能聚合页唤醒词

## 总结
1. 一代小康强制升级完成
2. 购物流程提交订单时本地语音提示
3. 视频通话机型兼容问题

# 2019.11.20
## 安排
1. 未读消息 三个接口添加
2. 重复绑定异常后请求是否绑定接口
3. 接口通用执行对象（统一处理）

## 总结
1. 未实现
2. 已实现
3. 未实现
4. 解决截屏黑白色问题
5. Kotlin优秀项目分析
6. EventBus实现原理解析 

# 2019.11.22
## 安排
1. 目前项目中用到的技术：<br>
① EventBus消息机制<br>
② handler延迟处理<br>
③ 广播进程间通讯<br>
④ AIDI进程间通讯<br>
⑤ 内容提供者进程间通讯<br>
2. SimpleDateFormat的使用，pattern的详细分类
3. 进入设置把技能app页面干掉
4. 