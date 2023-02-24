"""
break: 让当前这个循环立即停止
continue: 停止当前本次循环，继续进入下一次循环
"""

"""
while True:
    content = input("请输入你要喷的内容(输入q结束)：")
    if content == "q": #判断左右两端是个否一致
        break # 循环结束 只是终止循环
    print("发送给下路：", content)
"""
 #从1-10 跳过4
i = 1
while i <= 10:
    if i == 4:
        i = i + 1
        continue
        # 终止本次循环，直接4+1 跳过4.
    print(i)
    i = i + 1

