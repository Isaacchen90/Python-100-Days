# y = 0
# for n in range(1,100):
#     n += 1
#     y=y+n
# print(y)

# sum = 0
# for x in range(101):
#     sum += x
# print(sum)
#range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
#range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
#range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
#range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
# 用for循环实现1~100之间的偶数求和
# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)
# sum = 0
# for x in range(101):
#     if x % 2 == 0:
#         sum += x
# print(sum)
# import random

# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入100以内的数: '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')
#99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()
#输入一个正整数判断是不是素数（素数指的是只能被1和自身整除到大于1的整数
# 素数只能被1和自身整除
# source = int(input('请输入一个正整数： '))
# for i in range(2,source +1):
#     if source % i == 0:
#         print('%d 不是一个素数' % source)
#         break
#     else:
#         print('%d 是一个素数' % source)
#         break
# 两个数的最大公约数是两个数的公共因子中最大的那个数；
# 两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。

# s1 = int(input("输入第一个数字： "))
# s2 = int(input("输入第二个数字： "))
# if s1>s2:
#     s1,s2 = s2,s1
# max_GY = []
# for i in range(s1,0,-1):#a 到0，采用倒着来就是-1
#     if s1 % i == 0 and s2 % i == 0:
#         max_GY.append(i)
#         print('%d和%d的最大公约数是%d' % (s1, s2, i))
#         print('%d和%d的最小公倍数是%d' % (s1, s2, s1 * s2 // i))
#         break

