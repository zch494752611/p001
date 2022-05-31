# 面向对象

# 1.定义一个电梯的类:class 类名()
class elevator():
    # 2.在类里申明属性（数据）和方法（函数）
    button = "开/关"
    floor = 15
    people_nums = 13

    # 打开电梯
    def start(self):
        print("打开电梯")

    # 关闭电梯
    def stop(self):
        print("关闭电梯")

    # 运行电梯
    def run(self):
        print("电梯运行")

# 3.定义一个具体的对象，叫初始化对象，对象是一个实实在在的对象。=》初始化对象：对象名=类名（）
e = elevator()

# 4.使用对象调用方法或者属性：对象名.属性 || 对象名.方法
e.start()
e.stop()
e.run()


# 使用函数来实现
# 打开电梯
def start():
    print("打开电梯")

# 关闭电梯
def stop():
    print("关闭电梯")

# 运行电梯
def run():
    print("电梯运行")

print("="*20)
start()
stop()
run()

# 实例：创建学生类，要求有属性：姓名和年级；方法有：学习的方法，打印学生的上课情况
class Students():
    name = ''
    grade = ''

    def study(self):
        print("{}年级的学生{}正在学习".format(self.grade,self.name))

s1 = Students()
s1.name = '张三'
s1.grade = '5'
print(s1.study())

s2 = Students()
s2.name = '李四'
s2.grade = '4'
print(s2.study())



