# Python-Study
一个小白痛苦自学之路

___2023/02/23___\
 &ensp;主要学习了：\
 ___&ensp;&ensp;1.注释___
 
 ___&ensp;&ensp;2.变量___\
 &ensp;&ensp;&ensp;&ensp;1.必须是数字或者字母和下划线组合\
 &ensp;&ensp;&ensp;&ensp;2.不能是数字开头，更不能是纯数字\
 &ensp;&ensp;&ensp;&ensp;3.不能用Python关键字 eg：if print for while async Ture......\
 &ensp;&ensp;&ensp;&ensp;4.不能用中文\
 &ensp;&ensp;&ensp;&ensp;5.要有意义，别太长\
 &ensp;&ensp;&ensp;&ensp;6.推荐使用下划线/驼峰命名 \
 &ensp;&ensp;&ensp;&ensp;eg：下划线 name_of_teacher = "樵夫"  ***** 常用\
 &ensp;&ensp;&ensp;&ensp;驼峰 Name0of0Teacher = "樵夫"   *****类的时候会用\
 &ensp;&ensp;&ensp;&ensp;     综上，看得舒服看得爽！！！！！\
 
 ___&ensp; &ensp;3.常量___\
 &ensp;&ensp;&ensp;&ensp;1.把变量所有字母都变成大写就可以认为是常量\
 &ensp;&ensp;&ensp;&ensp;2.Python不存在绝对意义上的常量\
 
 ___&ensp; &ensp;4.浅谈数据类型___\
&ensp;&ensp;&ensp;&ensp;1.数字：+-*/ \
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;整数，int\
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;小数，float\
&ensp;&ensp;&ensp;&ensp;2.字符串：str\
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; 操作：\
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; +  左右两端都是字符串 （str + str）\
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; *  一个字符串只能乘以一个数字 （周润发 * 5）
&ensp;&ensp;&ensp;&ensp;3.（bool）：条件判断\
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; 布尔值主要有两个：\
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Ture 真，真命题\
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; False 假，假命\
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; 可以通过计算，也可以通过赋值得到（a = Ture）

 ___&ensp;&ensp;5.浅谈用户交互___\
 &ensp;&ensp;&ensp;&ensp;变量 = input(提示语)\
 &ensp;&ensp;&ensp;&ensp;       坑：input（）得到的结果一定是字符串\
 &ensp;&ensp;&ensp;&ensp;想把谁转化成谁，就用谁套起来\
 &ensp;&ensp;&ensp;&ensp;       eg：str => int     int(str)
        
 ___&ensp; &ensp;6.条件判断___\
 if语句的语法法规：
 
   1.
        if 条件:
             代码
         如果条件成立就执行代码
         如果不成立就不执行
         
    2.
        if 条件：
            代码1
        else：
            代码2
        如果条件成立，执行1，否则 执行2

    3.
        if语句可以互相嵌套
            if 条件：
                 if.....：
                 else：
            else：

    4.
        if 条件：
             代码1
        elif 条件2：
              代码2
        elif 条件3:
              代码3
        ...
        else：
              XXXX

 
 ___2023/02/24___\
&ensp;主要学习了：\
 ___&ensp;&ensp;1.循环语句___\
 &ensp;&ensp可以让我们的代码重复的去执行
while循环：

    while 条件：
        代码
        
    过程：判断条件是否为真，如果真，执行代码，然后再次判断条件，如果为假......直到条件为假，循环结束。
    
 ___&ensp;&ensp;2.break和continue___\
&ensp;&ensp;&ensp;&ensp;  break: 让当前这个循环立即停止
&ensp;&ensp;&ensp;&ensp;  continue: 停止当前本次循环，继续进入下一次循环

 ___&ensp;&ensp;3.for循环___\
 
&ensp;&ensp;字符串是可迭代的
 for循环：
    
    for 变量 in 可迭代的东西：
        代码
    把可迭代的东西中的每一项内容拿出来，挨个赋值给变量，每一次赋值都要执行一次循环体（代码）

    for 想要计数必须借助于range

    range(n):从0数到n，不包含n。
    range(m,n):从m数到n，不包含n
    range(m,n,s):从m数到n，不包含n，间隔是s。

    平时用的多的是for，while一般写死循环
    
 ___&ensp;&ensp;4.pass占位___\
 &ensp;&ensp;pass：代码占位
 
 ___&ensp;&ensp;5.基础数据类型概述___\
 int, float, bool
 str  (*****)
 list (*****)    列表
 tuple (**)      元组
 set   (*)       集合
 dict  (*****)   字典
 bytes (****)
 运算符  (****)
 文件操作 (****)
 
 ___&ensp;&ensp;6.int，float，bool___\
&ensp;&ensp;&ensp;&ensp; int:整数，加减乘除，大小比较。\
&ensp;&ensp;&ensp;&ensp; float: 小数，浮点数\
&ensp;&ensp;&ensp;&ensp; 小数的数据范围是无限的,计算机表示一个小数是有误差的。（不能接受就放大 eg：0.00001*10000）
 
 ___&ensp;&ensp;7.字符串(格式化、索引、切片)___\
1.  %s 字符串占位     %d  占位整数      %f  占位小数\
&ensp;&ensp;&ensp;&ensp;   f-string Python3.5 新出的功能\
2.索引：按照位置提取元素\
&ensp;&ensp;&ensp;&ensp;   print(s[3])  # 程序员都是从0开始数数,是第4个数字, -  代表倒数\
3.切片： 从一个字符串中提取一部分内容\
&ensp;&ensp;&ensp;&ensp;   如果start是从开头进行切片，可以省略;  从start开始一直截取到末尾\
&ensp;&ensp;&ensp;&ensp;   语法： s[start:end] 从start到end进行切片，但是取不到end [start, end)\
&ensp;&ensp;&ensp;&ensp;   语法： s[start：end：step] 从start切到end，每step个元素出来一个元素

 ___&ensp;&ensp;8.字符串（字母大小写转换）___\
&ensp;&ensp;    字符串的操作一般不会对原字符串产生影响，一般是返回一个新的字符串\
&ensp;&ensp;&ensp;&ensp;    .capitalize() # 让首字母大写\
&ensp;&ensp;&ensp;&ensp;    .title()  #单词首字母大写（一串连贯的英文字母 eg：aa哈哈aa）\
&ensp;&ensp;&ensp;&ensp;    .lower()  #变成小写字母\
&ensp;&ensp;&ensp;&ensp;    .upper()  # 把所有字母变成大写字母

 ___&ensp;&ensp;9.字符串（切割和替换）___\
&ensp;&ensp;&ensp;&ensp;     strip()  去掉字符串左右两边的空白符（空格、\t、\n）v\
&ensp;&ensp;&ensp;&ensp;     replace(old,new)  将new替换old\
&ensp;&ensp;&ensp;&ensp;     split(用什么切割)  切割;切割后的结果会放在列表当中;用谁切割就会损失掉谁

 ___2023/02/25___\
&ensp;主要学习了：\
 ___&ensp;&ensp;1.字符串（查找和判断）___\
&ensp;&ensp; 1.查找
&ensp;&ensp;&ensp;&ensp;     .find(" ")    返回如果是-1，就是没有该字符串\
&ensp;&ensp;&ensp;&ensp;     .index(" ")   返回如果报错，就是没有该字符串\
&ensp;&ensp;&ensp;&ensp;     print(" " in s )      in  可以做条件上的判断\
&ensp;&ensp;&ensp;&ensp;     print(" " not in s)   not in  判断是否存在\
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;     for c in s:     将s中的每一个字符依次赋值给c\
&ensp;&ensp; 2.判断\
&ensp;&ensp;&ensp;&ensp;      .startswith("  ")判断开头的字符是否以****，.endswith 结尾是否\
&ensp;&ensp;&ensp;&ensp;      .isdigit():      判断字符串是否有整数组成，.isdecimal小数

 ___2023/02/26___\
&ensp;主要学习了：\
 ___&ensp;&ensp;1.列表的概念___\
&ensp;&ensp;&ensp; 列表定义：能装东西的东西\
&ensp;&ensp;&ensp; 在Python中用[]来表示一个列表，列表中的元素用,隔开

&ensp;&ensp;特性：
&ensp;&ensp;&ensp;&ensp;   1.列表页和字符串一样，也有索引和切片\
&ensp;&ensp;&ensp;&ensp;   2.索引如果超出范围会报错\
&ensp;&ensp;&ensp;&ensp;   3.可以用 for 循环进行遍历\
&ensp;&ensp;&ensp;&ensp;   4.用len可以拿到列表的长度

 ___&ensp;&ensp;2.列表(增删改查)___\
&ensp;&ensp;&ensp;&ensp;   append()                        在列表最后面追加\
&ensp;&ensp;&ensp;&ensp;   insert(位置，要插入的内容)        插入\
&ensp;&ensp;&ensp;&ensp;   extend([ ])                     可以合并两个列表，批量添加\
&ensp;&ensp;&ensp;&ensp;   pop(要删除的位置)                删除，ret = lst.pop  给出被删除的索引，返回被删除的元素\
&ensp;&ensp;&ensp;&ensp;   remove(要删除的内容)             删除某个元素（******）\
&ensp;&ensp;&ensp;&ensp;   lst[要替换的位置] = "要替换的内容"   直接用索引就可以进行修改操作\
&ensp;&ensp;&ensp;&ensp;   print(lst[要查询的位置])         直接用索引就可以操作\

