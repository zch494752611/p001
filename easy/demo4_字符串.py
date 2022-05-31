# 字符串格式化
my_str = 'my name is %s' % ('张三')
print(my_str)

# 整数
my_age = 'my age is %d' % (22)
print(my_age)

# 浮点数
apple = '一斤苹果%.1f元' % (3.5)
print(apple)

apple = '一斤苹果%+9.5f元' % (3.14159)
print(apple)

# f = 3.141592653
# # 最小宽度为8，小数点后保留3位
# print("%8.3f" % f)
# # 最小宽度为8，小数点后保留3位，左边补0
# print("%08.3f" % f)
# # 最小宽度为8，小数点后保留3位，左边补0，带符号
# print("%+8.3f" % f)

# fomrat
my_str2 = '今天星期{},张三给我买了{}个苹果'.format('一','3')
print(my_str2)

# fomrat的位置参数： '{0}{1}{2}{3}'.format（第一个数，第二个数...
my_str3 = '今天星期{1},张三买了{0}斤苹果'.format('一',"5")
print(my_str3)

# 连接字符串: join()
astr = "+"
bstr = astr.join("world")
print(bstr)

# 分割字符串:split(str="")
cstr = "hello world ashka jdoda sdao ww"
dstr = cstr.split(" ")
print(dstr)

# 查找字符串：find()
estr = "helloworld"
print(estr.find("w"))

# 查找以xxx结尾的字符串: endswith("xxx")
fstr = "测试报告.doc"
if fstr.endswith('.doc'):
    print('yes')

# 替换字符串： replace(old_value,new_value)
gstr = "halloworld"
hstr = gstr.replace("world","python")
print(hstr)

# 2. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
ceshi = "abceeddedaj123 @@@  张三"
zf = 0
kg = 0
sz = 0
other = 0
for x in ceshi:
    if x.isalpha():     #判断是字符
        zf += 1
    elif x.isdigit():   #判断是数字
        sz += 1
    elif x.isspace():   #判断是空格
        kg += 1
    else:
        other += 1
print('字符:',zf)
print('数字:',sz)
print('空格:',kg)
print('其他:',other)