# 产生50-150之间的数
# import random
# print(random.randint(50,150))

# 判断三角形
# while True:
#     a=input("请输入第一个边的边长：")
#     a=int(a)
#     b=input("请输入第二个边的边长：")
#     b=int(b)
#     c=input("请输入第三个边的边长：")
#     c=int(c)
#     if a+b>c and a+c>b and b+c>a and a!=0 and b!=0 and c!=0:
#         if a==c!=b or a==b!=c or b==c!=a:
#             print("等腰三角形")
#         elif a==b==c:
#             print("等边三角形")
#         elif a!=b and a!=c and b!=c:
#             print("普通三角形")
#         break
#     else:print("请输入有效数据")

# # 调换位置
# a=int(input("请输入一个数a:"))
# b=int(input("请输入另一个数b:"))
#
# a=a+b
# b=a-b
# a=a-b
#
# print("两个数互换之后a:",a,"两个数互换之后b:",b)

# 密码锁定
# import time
# counter = 0
# while True:
#     pwd=123456
#     text_pwd=input("请输入密码:")
#     text_pwd=int(text_pwd)
#     if text_pwd==pwd:
#         print("密码正确")
#         break
#     elif text_pwd!=pwd:
#         print("输入有误，请重新输入")
#         counter=counter+1
#         while counter==3:
#             print("输入三次密码错误，系统锁定一天")
#             time.sleep(86400)

# 打印图形
# i=0
# while i<=7:
#     print(" " * (7 - i), end="")
#     print("* " * (i + 1))
#     i=i+1

# 倒叙99乘法表
# i=9
# while 0<i<=9:
#     j=1
#     while j<=i:
#         print(j,"*",i,"=",j*i,"    ",end="")
#         j=j+1
#     print()
#     i=i-1

# 青蛙
high=20
num=0
while True:
    num = num + 1
    if high-3<=0:
        break
    else: high=high-3+2
print(num)

# 青蛙
# a=20
# day=0
# s=0 #爬的高度
# while True:
#     s=s+3
#     day=day+1
#     if s>=20:
#         break
#     else:s=s-2
# print(day)


