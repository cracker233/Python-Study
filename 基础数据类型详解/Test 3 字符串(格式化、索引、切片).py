# 1.字符串的格式化问题
# 我叫xxx
"""
name = input("请输入你的名字：")
address = input("请输入你的地址：")
age = int(input("请输入你的年龄："))
hobby = input("请输入你的爱好：")

# %s 字符串占位
# %d  占位整数
# %f  占位小数

s = "我叫%s，我住在%s，今年%d岁，我喜欢做%s"% (name, address, age, hobby)
s0 = "我叫%s" % name   #只有一项的时候可以不写 ()
s1 = "我叫{}，我住在{}，今年{}岁，我喜欢做{}".format(name, address, age, hobby)
s2 = f"我叫{name}，我叫{name}，我叫{name}，我叫{name}，今年{age}岁，我叫{name}，我叫{name}"  #****** f-string Python3.5 新出的功能
print(s0)
"""

"""
# 2.字符串的索引和切片

# 索引：按照位置提取元素
s = "我叫周杰伦"
# 可以采用索引的方式来提取某一个字符（文字）
print(s[3])  # 程序员都是从0开始数数,是第4个数字
print(s[0])
print(s[-1])  # -代表倒数
"""

"""
#切片： 从一个字符串中提取一部分内容
#s = "我叫周杰伦，你叫周润发吗？"
#print(s[3:6]) #从索引3位置进行切片，切到6结束，坑！！！！切片拿不到第二个位置的元素。
# 语法： s[start:end] 从start到end进行切片，但是取不到end [start, end)

#print(s[0:5])
#print(s[:5])  # 如果start是从开头进行切片，可以省略
#print(s[6:])  # 从start开始一直截取到末尾
# ： 如果左右两边有空白，表示开头或结尾
#print(s[ : ])
#print(s[-3:-1])  #还是从左往右切片
#print(s[-1:-3])  #没有结果


#s = "我爱你"
# 可以给切片添加步长来控制切片的方向
#print(s[::-1])  # -表示从右往左
#语法： s[start：end：step] 从start切到end，每step个元素出来一个元素

s = "abcdefghijklmn"
print(s[2:11:3])
print(s[-1:-10:-3])
"""

