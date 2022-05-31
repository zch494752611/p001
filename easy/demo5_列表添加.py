# info = A + B  拼接列表
# language = ['JAVA','python','linux']
# bir = ['3.7','4.2','12.31']
# info = language + bir
# print(info)


# listname.append(obj)
# listname 表示要添加元素的列表；obj 表示到添加到列表末尾的数据，它可以是单个元素，也可以是列表、元组等。
# l = ['ABC','CCC','NB']
# l.append('123')  # 追加元素，一次只能添加一个
# print(l)
#
# t = ('java','c#',"c++") #追加元组
# l.append(t)
# print(l)
#
# l.append(['robblt','life']) # 追加列表
# print(l)


# listname.extend(obj)
# extend() 和 append() 的不同之处在于：extend() 不会把列表或者元祖视为一个整体，而是把它们包含的元素逐个添加到列表中。
# l = ['Python', 'C++', 'Java']
# #追加元素
# l.extend('C')
# print(l)
# #追加元组，元祖被拆分成多个元素
# t = ('JavaScript', 'C#', 'Go')
# l.extend(t)
# print(l)
# #追加列表，列表也被拆分成多个元素
# l.extend(['Ruby', 'SQL'])
# print(l)


# append() 和 extend() 方法只能在列表末尾插入元素，如果希望在列表中间某个位置插入元素，那么可以使用 insert() 方法。
# listname.insert(index , obj)
# 其中，index 表示指定位置的索引值。insert() 会将 obj 插入到 listname 列表第 index 个元素的位置。
A = ['haha','123','zhang']
A.insert(2,'C')  # 插入元素
print(A)

t = ('C#', 'Go')
A.insert(1,t)
print(A)

#插入列表，整个列表被当成一个元素
A.insert(3, ['Ruby', 'SQL'])
print(A)
#插入字符串，整个字符串被当成一个元素
A.insert(0, "http://c.biancheng.net")
print(A)