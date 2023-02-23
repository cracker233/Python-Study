"""
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
        elif 条件3
              代码3
        ...
        else：
              XXXX
"""

"""
# =====第一种=====
money = 500
if money > 300:
    print("铁锅炖")  # 缩进代表了程序层级 类似于 {  }
if money <= 300:
    print("回家")

# =====第二种=====
money = input("请输入你兜里的钱：")
money = int(money)  # input 输入的是str 需要转换为int
if money > 500:
    print("铁锅炖")
else:
    print("回家五姑娘")

# =====第三种=====
money = input("请输入你兜里的钱：")
money = int(money)
if money > 1000:
    if money > 2000:
        if money > 3000:
            print("做全套")
        else:
            print("洗完小头，做spa")
    else:
        print("洗小头")
else:
    print("做足疗")
"""
# =====第四种=====
money = int(input("请输入你兜里的钱："))
if money > 5000:
    print("充卡")
elif money > 3000:
    print("做全套")
elif money > 2000:
    print("洗完小头，做spa")
elif money > 1000:
    print("洗小头")
else:
    print("做足疗")


