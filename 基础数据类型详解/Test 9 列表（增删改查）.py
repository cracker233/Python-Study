#  列表的增删改查
# lst = []
#像列表中添加内容

# append() 在列表最后面追加

# insert() 插入

# insert(位置，要插入的内容).

# extend([ ])可以合并两个列表，批量添加

# pop(要删除的位置)  删除，ret = lst.pop  给出被删除的索引，返回被删除的元素

# remove(要删除的内容)  删除某个元素（******）

#lst[要替换的位置] = "要替换的内容"   直接用索引就可以进行修改操作

#print(lst[要查询的位置])  直接用索引就可以操作

# lst.append("a")
# lst.append("b")
# lst.append("c")+
# print(lst)

#  把所有姓的人改成姓王
lst = ["张无忌","康峰","王一博","李红梅","张大大"]

# for item in lst:      #此时我们看不到元素的索引位置     （这个循环的是元素）
for i in range(len(lst)):       #  len(lst)；列表的长度   ==>   可以直接得到列表索引的for循环  （这个循环的是索引）
    item = lst[i]               #item任然是列表中的每一项
    if item.startswith("张"):   #判断姓是否是张
        new_name = "王"+item[1:]
        lst[i] = new_name   #修改

print(lst)
