# 1.中缀表达式转后缀表达式
expression = "1+[(3-1)*(3+2)]/2"

def middle2behind(expresssion):  
    result = []             # 结果列表
    stack = []              # 栈
    if '[' in  expression:
    	res = expression.replace('[', '(')
    	res1 = res.replace(']', ')')
    for item in res1: 
        if item.isnumeric():      # 如果当前字符为数字那么直接放入结果列表
            result.append(item) 
        else:                     # 如果当前字符为一切其他操作符
            if len(stack) == 0:   # 如果栈空，直接入栈
                stack.append(item)
            elif item in '*/(':   # 如果当前字符为*/（，直接入栈
                stack.append(item)
            elif item == ')':     # 如果右括号则全部弹出（碰到左括号停止）
                t = stack.pop()
                while t != '(':   
                    result.append(t)
                    t = stack.pop()
            # 如果当前字符为加减且栈顶为乘除，则开始弹出
            elif item in '+-' and stack[len(stack)-1] in '*/':
                if stack.count('(') == 0:           # 如果有左括号，弹到左括号为止     
                    while stack:
                        result.append(stack.pop())
                else:                               # 如果没有左括号，弹出所有
                    t = stack.pop()
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                    stack.append('(')
                stack.append(item)  # 弹出操作完成后将‘+-’入栈
            else:
                stack.append(item)# 其余情况直接入栈（如当前字符为+，栈顶为+-）

    # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
    while stack:
        result.append(stack.pop())
    # 返回字符串
    return "".join(result)


print(middle2behind(expression))


# 2.后缀表达式转中缀表达式
expression1 = '131-32+*2/+'
def behind2middle(expression):
	result = []
	stack = []
	for item in expression1:
		


'''
### 系统篇
Q:如何用命令行将一个文件传到Linux服务器

	我一般使用xshell连接服务器，使用rz命令即可将本地文件直接上传到服务器上

Q: 从某⽇志⽂件中，查找包含「error」关键词（不区分⼤⼩写）的⾏，并输
出对应前 10 ⾏和后 5 ⾏

	cat ***.log | grep 'error' tail -n head 10 查找前10行
	cat ***.log | grep 'error' tail -n 5 查找后5行

Q: 查找端⼝号 9292 对应的进程名和 PID

	lsof -i:9292

Q:介绍下SSH公钥登录的原理

	一般来说，登录的流程如下：
	1.首先生成秘钥对
	2.将公钥信息写入目标用户的秘钥验证文件
	3.客户端请求登录
	4.服务器发送一段随机字符串，并使用公钥加密
	5.客户端使用私钥解密，返回给服务器解密后的信息
	6.服务器进行信息对比，如果验证成功，则允许连接

### Git篇
Q:git	pull 和 git	fetch 的区别

	git fetch是将远程主机的最新内容拉到本地，用户在检查了以后决定是否合并到工作本机分支中。

而git pull 则是将远程主机的最新内容拉下来后直接合并，即：git pull = git fetch + git merge，这样可能会产生冲突，需要手动解决。

Q: 如何将⼀个分⽀的 commit 引⼊到另外⼀个分⽀

	

Q: git	rebase 和 git	merge 的区别及使⽤场景

	

Q: 介绍下你之前的团队是如何使⽤ git 协同⼯作的

	再上一个项目中，没有使用Git进行协同工作，在之前的工作经历中，主要是用作代码
储存，将自己写好的模块上传，供其他人下载使用。

### 数据库
Q: 使⽤ SQL 输出每个城市的球场数，包含：省份ID / 省份名称 / 城市ID / 城市
名称 / 球场数

	select * from provinces,cities,stadiums where cities.province_id = provinces.id and 
stadiums.city_id = cities.id

Q: 下⾯的 SQL 查询会使⽤索引 idx_stadiums_on_ptc 吗？为什么？你会如何
优化呢？


Q: 多并发的情况下，下⾯事务会出现死锁吗？为什么？如何优化呢？



### python篇
Q: 推荐⼀本你看过的 python 书籍

	狗书

Q: 谈谈python的装饰器，迭代器、yield

		装饰器：本质上还是一个函数，比如声明类方法的@classmethod,声明静态方法的@staticmethod,
	如果想执行某个函数前实现某一功能，又不想改动这个函数，那么就可以通过装饰器来实现,比如写一个计
	算函数执行时间的装饰器。

		迭代器: 简单理解是可以使用for循环来遍历的对象，如常见的list.set和dict。

		yield: 一个带有yield的函数可以成为生成器，它可以保存一个对象的状态信息，当执行到yield时函数
	返回，保存断点，我们可以使用next()继续从yield返回的位置继续执行，也可以使用send()将参数传递给函数
	继续从yield的地方执行。

Q: 如果对⼀个列表做去重
	
		ex = [1,2,2,3,3,4]
		a = set(ex)
		res = list(a)
		print(res)

Q: django/flask/tornado 框架各⾃的特点

		flask适合用于小型应用开发；如果开发团队能力强，也可以用来做大中型应用

		django适合应用用于访问量不大的大中型应用

		tornado适合用于开发长连接多的web应用。比如股票信息推送、网络聊天等。

### 开放性问题

Q：碰到一个技术方面的难题，你一般会如何解决？

	1.分析自己需要达到什么效果，提取关键词使用搜索引擎查找解决方案
	2.浏览论坛或者社区查找是否有相似解决方案，或者发帖寻求帮助
	3.询问朋友，是否有相关解决方案
	4.阅读相关文档或者源码，查看是否有解决的思路

Q:介绍一个你曾经使用的开源项目

	

Q:什么是持续集成

	持续集成是一种软件开发实践，即团队开发成员经常集成他们的工作，通常每个成员每天至少
集成一次，或者更多次，每次集成通过自动化的构建(包括编译，发布，测试)来验证，从而尽快发现
bug。在这个过程中，可以大大节约时间，尽早解决开发中的问题。
'''