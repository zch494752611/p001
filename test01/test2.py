# i = 1   #循环变量，对应当前循环几次
# n = int(9)
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1

i=1
j=1
while i<10:
    while j<(i+1):
        print("%d*%d=%d"%(i,j,i*j),end="\t")
        j+=1
    print()
    i=i+1
    j=1



