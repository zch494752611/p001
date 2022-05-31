class Students():
    name = ''
    grade = ''

    # 申明构造方法： __init__()
    def __init__(self):
        print("此方法会被自动执行")

    def study(self):
        print("{}年级的学生{}正在学习".format(self.grade,self.name))

s1 = Students()
s1.name = '张三'
s1.grade = '5'
# print(s1.study())

# 使用构造方法去实现
class Students1():

    # 申明构造方法： __init__()
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        print("此方法会被自动执行")

    def study(self):
        print("{}年级的学生{}正在学习".format(self.grade,self.name))

s2 = Students1('王五',6)
s2.study()


print("="*20)
class Students2:

    def study(self):
        self.name = "张三"
        self.grade = "五年级"
        print("这里的self是：",self)
        print("{}的学生{}正在学习".format(self.grade,self.name))

    def eat(self):
        print(self.name,"是",self.grade,"正在吃饭")

s3 = Students2()
print(s3.study())

print(s3.eat())


print("="*20)
class Students4():
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def eat2(self):
        print(self.name,"是",self.grade,"正在吃饭")

s4 = Students4("张三","四年级")
print(s4.eat2())




# 需求：实现连接数据库，使用构造方法

"""
1.定义连接数据库的类
2.必须和数据库建立连接，使用构造方法是最合适的
3.进行各种方法调用
"""