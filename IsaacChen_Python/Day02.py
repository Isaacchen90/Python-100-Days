#整型：int
#浮点型：float
#字符串：string '' ""
#布尔型： bool True False  例如3 < 5 会产生布尔值为True
#负数型：非常用，3+5j
# a = 321
# b = 12
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# c = 100
# d = 12.345
# e = 1 + 5j
# f = "hello,world"
# g = True
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
#类型转换
#int()：将一个数值或字符串转换成整数，可以指定进制。
#float()：将一个字符串转换成浮点数。
#str()：将指定的对象转换成字符串形式，可以指定编码。
#chr()：将整数转换成该编码对应的字符串（一个字符）。
#ord()：将字符串（一个字符）转换成对应的编码（整数）。
# h = int(input('a = '))
# i = int(input('b = '))
#说明：上面的print函数中输出的字符串使用了占位符语法，其中%d是整数的占位符，%f是小数的占位符，%%表示百分号（因为百分号代表了占位符，所以带占位符的字符串中要表示百分号必须写成%%），字符串之后的%后面跟的变量值会替换掉占位符然后输出到终端中，运行上面的程序，看看程序执行结果就明白啦。
# print('%d + %d = %d' % (h, i, h + i))
# print('%d - %d = %d' % (h, i, h - i))
# print('%d * %d = %d' % (h, i, h * i))
# print('%d / %d = %d' % (h, i, h / i))
# print('%d // %d = %d' % (h, i, h // i))
# print('%d %% %d = %d' % (h, i, h % i))
# print('%d ** %d = %d' % (h, i, h ** i))
# 你好  我好大家好  你是我的荣耀  杨洋带你打王者
# a = 10
# b = 3
# a += b        # 相当于：a = a + b
# a *= a + 2    # 相当于：a = a * (a + 2)
# print(a)      # 算一下这里会输出什么

# flag0 = 1 == 1
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not(1 != 2)
# print('flag0 =', flag0)    # flag0 = True
# print('flag1 =', flag1)    # flag1 = True
# print('flag2 =', flag2)    # flag2 = False
# print('flag3 =', flag3)    # flag3 = False
# print('flag4 =', flag4)    # flag4 = True
# print('flag5 =', flag5)    # flag5 = False

# a = float(input('请输入华氏温度:'))
# b = (a-32)/1.8
# print('%.2f华氏度 = %.2f摄氏度' % (a,b))
# print(f'{a:.3f}华氏度 = {b:.3f}摄氏度')

# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * 3.1416 * radius
# area = 3.1416 * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)


# year = int(input('请输入年份: '))
# # 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
# is_leap = year % 4 == 0 and year % 100 != 0 or \
#           year % 400 == 0
# print(is_leap)