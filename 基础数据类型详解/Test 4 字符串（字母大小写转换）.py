#3.字符串的常规操作
#字符串的操作一般不会对原字符串产生影响，一般是返回一个新的字符串
#3.1 字符串大小写转换
#s = "python"
#s1 = s.capitalize() # 让首字母大写
#print(s1)

#s = "I have a dream"
#s1 = s.title()  #单词首字母大写（一串连贯的英文字母 eg：aa哈哈aa）
#print(s1)

#s = "I HAVE A DREAM"
#s1 = s.lower()  #变成小写字母
#print(s1)

#s = "I have a dream"
#s1 = s.upper()  # 把所有字母变成大写字母
#print(s1)

 #忽略大小写来进行判断   ==> .upper
verify_code = "xAd1"
user_input = input(f"请输入验证码：({verify_code}):")
if verify_code.upper() == user_input.upper():
    print("输入正确！！")
else:
    print("错误！！！")