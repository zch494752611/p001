str='C语言是最美的语言'

# 序列索引
# print(str[0],str[-9])
# print(str[4],str[-5])

# 序列切片
# #取索引区间为[0,3]之间（不包括索引2处的字符）的字符串
# print(str[:3])
# #隔 1 个字符取一个字符，区间是整个字符串
# print(str[::2])
# #取整个字符串，此时 [] 中只需一个冒号即可
# print(str[:])

# 序列相加相乘
# print('玩机器'+'6657'+str)
# print('玩机器'*3)

# # 检查元素是否包含在序列中
# print('C' not in str)
#
# print(sorted(str)) # 对'str'进行排序


# 创建列表
#将字符串转换成列表
# list1 = list('hallo,2,3,4')
# print(list1)
# #将元组转换成列表
# tuple1 = ('abc','黑子','123','ufo')
# list2 = (tuple1)
# print(list2)
# #将字典转换成列表
# dict1 = {"a":1,'b':102,'c':30}
# list3 = (dict1)
# print(list3)
# #将区间转换成列表
# range1 = range(1, 6)
# list4 = list(range1)
# print(list4)
# #创建空列表
# print(list())

# # 访问列表元素
# ur1 = list("1234567890")
# #使用索引访问列表中某个元素
# print(ur1[4])
# print(ur1[-4])
#
# print(ur1[2:5])
# print(ur1[2:8:2])
# print(ur1[-6:-1])

# 删除列表 del listname
# intlist = [1,2,3,4,5,6]
# print(intlist)
# del intlist
# print(intlist)