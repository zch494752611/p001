# 列表推导式： [表达式2 循环体 表达式1],执行的顺序：先执行循环体，其次执行后面表达式1，最后执行表达式2

# 生成一个1-10的列表
lst = []
for x in range(1,11):
    lst.append(x)
print(lst)

lst1 = [x for x in range(1,11)]
print(lst1)

# 生成一个1-10列表，只打印奇数的数
lst2 = [x for x in range(1,11) if x %2 !=0]
print(lst2)

# 生成一个1-10列表,生成的奇数再加上10
lst3 = [x+10 for x in range(1,11) if x % 2 != 0]
print(lst3)




