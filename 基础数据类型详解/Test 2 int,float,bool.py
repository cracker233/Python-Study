"""
int:整数，加减乘除，大小比较。

float: 小数，浮点数
#小数的数据范围是无限的。
print(10/3)  （3.33333333333335）
计算机表示一个小数是有误差的。（不能接受就放大 eg：0.00001*10000）

bool：用来做条件判断的
    取值范围： True， False


"""

"""
##基础数据类型之间的转换
a = "10"
print(type(a))
b = int(a)
print(type(b))
"""

"""
a = 0  # 在Python中，所有非0的数字都是 True，零是False。
b = bool(a)
print(type(b))
print(b)
"""

"""
while 1:  # 死循环，恒为真
    print("还钱")
"""

"""
s = ""  #在Python基本数据类型中，所有的非空字符串都是True，空字符串是False
print(bool(s))

综上，在python中，表示空的东西都为False，不空的东西都是True

lst = [0]  #表格不空，所以是True
print(bool(lst))
"""

while 1:
    content = input("请输入你要喷的内容：")
    if content:
        print("你要发给打野的内容", content)
    else:
        break


