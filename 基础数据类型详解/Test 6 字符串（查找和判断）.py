# 3. 字符串的查找和替换
#   ****** 查找*************
# s = "你好呀我是周润发！"

# ret = s.find("周润发") #返回如果是-1，就是没有该字符串。
# print(ret)

# ret = s.index("周润发123")   #返回如果报错，就是没有该字符串。
# print(ret)

# print("周润发" in s )       # in  可以做条件上的判断
# print("周润发" not in s)    # not  判断是否存在
# for c in s:
#     print(c)

#*************判断**********
# name = input("what's your name?")
# #判断你姓不姓张
# if name.startswith("张"):   # 判断开头的字符是否以****，，endswith 结尾是否已
#     print("yes")
# else:
#     print("no")
money = input("多少钱：")
if money.isdigit():      # 判断字符串是否有整数组成，.isdecimal小数
    money = int(money)
    print("yes")
else:
    print("no")

# startswith()    isdigit() in      not int