# 函数调用 def xxx（x，y）
def add(x,y):
    z = x + y
    return z

print(add(3,4))    # 调用函数

def delt(a,b):
    return a - b
print(delt(8,4))    # 直接return

def calc(c,d):
     jia = c + d
     jian = c - d
     return jia,jian
print(calc(10,5))   # 返回两个值


# 关键字参数 key = value
def st_lesson(gra,sub):
    z = "{}年级上{}课".format(gra,sub)
    return z

print(st_lesson(3,'英语'))
print(st_lesson(gra=4,sub='数学'))     #关键字参数
print(st_lesson(sub='语文',gra=5))     #关键字参数可以调换位置
print(st_lesson(6,sub='体育'))   #关键字参数和位置参数混合使用。


# 默认参数
def st_lan(name,lan='python'):
    info =('{}要学习{}语言'.format(name,lan))
    return info

print(st_lan('张三'))


# 可变参数
# 需求：可以输入任何个数进行相加

# 1.定义列表形式调用
def add(x,y,*args):
    z = x + y + sum(args)
    return z

print(add(3,4,5,6,7))
print(add(1,2,3))

# 使用列表形式调用
print(add(3,4,*[5,6,7]))

# 2.可变化参数-字典形式的参数
def show_info(**kwargs):
    print(kwargs)

print(show_info(a='hallo',b='world',c=123))

dt_data = {'x':1,'y':2}
print(show_info(**dt_data))




