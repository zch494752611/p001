# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
# a=2
# b=3
# c=4
# d=5
# print(a+b-c*d)

# 2. 打印1~100内被3整除的所有数的和 。
# a=0
# sum=0
# for a in range(1,101):
#     if a % 3 ==0:
#         sum= a + sum
#         print(sum)

# 3. 使用range()输出1~10内的所有奇数 。
# for a in range(1,10,2):
#     print(a)

# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
# sum1 = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sum1 = sum1 +i
#     i += 1
# print(f"1-100之间偶数的和是：{sum1}")
# sum2 = 0
# for a in range(1,101):
#     if a % 2 != 0:
#         sum2 = sum2 +a
#     a += 1
# print(f"1-100之间奇数的和是：{sum2}")
# print(sum1-sum2)

# 5. 求1+2+3+...+100的和
# print(sum(range(1,101)))

# 6. 判断一个数n能同时被3和5整除
# n=15
# print(n % 3==0 and n % 5 ==0)

# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
# x=102
# for a in range(1,101):
#     if x == a:
#         print(x)
#     else:
#         print('Not in 1-100')
#         break

# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
# x = int(input('x = '))
# y = int(input('y = '))
# z = int(input('z = '))
# if x < y:
#     x,y = y,x
# if x < z:
#     x,z = z,x
# if y < z:
#     y,z = z,y
# print(z, y, x)

# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
# score = int(input('分数'))
# if score >=90:
#     print('A')
# elif score >=60:
#     print('B')
# else:
#     print('C')

# 10. 将一个列表的数据复制到另一个列表中。
alist = [2,45,74,1223,33]
blist = ['aa','bb','22']
clist = ['gg','python',99]
alist.extend(blist)
print(alist)

# 11. 输出 9*9 乘法口诀表。
for x in range(1,10):
    for y in range(1,x+1):
        print(x,'*',y,'=',x*y,end='')
    print()


# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制。



# 14. 题目：打印出如下图案（菱形）
# 上面的循环：
# n=1 3+1+3
# n=2 2+3+2
# n=3 1+5+1
# n=4 0+7+0
#
# space = ' ' * (x-n)
# star = '*' * (2*(n-1)+1)

# 下面的循环：
# n=1 1+5
# n=2 2+3
# n=3 3+1
# space = n * ' '
# star = (5-(n-1)*2) * '*'

num = 5     #总数
x = num - 1     # 循环轮数

for n in range(1,num):
    space = ' ' * (x-n)
    star = '*' * (2*(n-1)+1)
    print(space + star)

for n in range(1,4):
    space = n * ' '
    star = (5-(n-1)*2) * '*'
    print(space + star)


