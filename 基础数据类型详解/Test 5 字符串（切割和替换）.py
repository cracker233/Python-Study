"""
#3.2 字符串的替换与切割
#strip()  去掉字符串左右两边的空白符（空格、\t、\n）
#s = "    你   好   我是  周结  论！！    "
#s1 = s.strip()
#print(s1)

#案例 用户登录界面
username = input("请输入用户名：").strip()  #去掉左右两边的空格
password = input("请输入密码：").strip()   #去掉左右两边的空格
if username == "admin":
    if password == "admin":
        print("successful！！！")
    else:
        print("no!!!!")
else:
    print("nonononono")
"""

# replace(old,new)  将new替换old
#s = "你好啊，我是大傻逼"
#s1 = s.replace("大傻逼","大帅逼")
#print(s1)

# split(用什么切割)  切割
a = "python_java_c_c#_swift"
#lst = a.split("_")   # 切割后的结果会放在列表当中
#print(lst)
lst = a.split("_java_")  # 用谁切割就会损失掉谁
print(lst)




