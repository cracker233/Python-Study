#列表的其他操作
#  1.排序
#lst = [1,2,3,"a","s"]    #列表会按照你存放的顺序来保存
# lst = [2,555,654,235,896,663]
# lst.sort()   #对列表进行升序
# lst.sort(reverse = True)  # reverse = 翻转
# print(lst)

#  2.嵌套
# lst = ["abc","sdf",["呵呵哒","妈妈呀","sdsd",["呼吸","dsdadasd"]],123,556]
# print(lst[2][3][1]) #查找 按嵌套顺序。
#
# lst[2][3][1] = lst[2][3][1].upper()    #字符串是不可变的，再将改大写的字符塞回去
# print(lst)

#   3.列表的循环删除（*********）
lst = ["赵敏","张绍刚",'张无忌','武则天',"嬴政",'马超']
temp = []  #临时列表，负责村春马上要删的内容

for item in lst:            #  for循环中会有一个记录当前循环到第几个的功能，删除一个后，后面的元素会补上来，就会跳过删除后面紧挨的一个元素
    if item.startswith("张"):
        temp.append(item)    #把要删除的内容记录下来
        #lst.remove(item)    #直接去删，删不干净

for item in temp:
    lst.remove(item)   # 去原列表中进行删除操作
print(lst)

  安全稳妥的循环删除方式：
        将要删除的内容保存在新列表中，循环新列表，删除老列表。


