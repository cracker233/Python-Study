'''
变量 = input(提示语)
首先会在屏幕中显示出提示语，用户输入内容。然后把用户输入的内容交给前面的变量
    ***坑：input（）得到的结果一定是字符串***

    怎么把字符串转化成其他数据类型？
    py基础数据类型：
        想把谁转化成谁，就用谁套起来
        eg：str => int     int(str)
'''

a = input("请输入第一个数字")
print(type(a)) #用type（）查看一个变量的数据类型
b = input("请输入第二个数字")
print(type(a)) #用type（）查看一个变量的数据类型

a = int(a)
b = int(b)

print(type(a),type(b))

print(a + b)


