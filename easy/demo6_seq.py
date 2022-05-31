# 序列的通用操作
# 1.索引 - 列表，元祖，字符串
# lst = ['red',10,123,'blue']
# print(lst[1:4])
# print(lst[-4:-1])
#
# tp = ('red','hello',2,3,5,6)
# print(tp[3])
# print(tp[-5])
#
# str1 = 'redhello2'
# print(str1[1])
# print(str1[-1])


# 2.序列的切片: seq[start:end:step]，默认从0开始
# lst2 = ['red','green',123,'abc','gold','uuu',999]
# print(lst2[1:5:1])
# print(lst2[1:6:2])
#
# print(lst2[::2])    # 省略了start和end
# print(lst2[0:7:2])
#
# print(lst2[2:])     # 省略了end和step
# print(lst2[2:7:1])
# print(lst2[2::])
#
# print(lst2[1::2])   # 省略end

# 列表中有10个元素，取出其中的奇数个数的元素
# lst2 = ['red','green',123,'abc','gold','uuu',999]
# print(lst2[::2])


# 3.序列的相加和相乘: + *
# alist = [1,2,3]
# blist = [4,5,6]
# clist = alist + blist
# print(clist)
#
# alist = 'hallo'
# blist = 'world'
# print(alist + blist)
# print(alist * 2)
#
# elst = [None] *3
# print(elst)
#
# print('='*40)


# 序列中的方法：list()
# klst = []
klst = list()
print(klst)

cstr = 'abc'
mlst = list(cstr)
print(mlst)

nlst = [1,2,3]
dlst = str(nlst)
print(type(dlst))

lst7 = ['red','green',123,'abc','gold','uuu',999]
for x in lst7:
    print(x,end=' ')

# 循环序列中的索引和值
for 2,5 in enumerate(lst7)
    print(2,'=====',5)



