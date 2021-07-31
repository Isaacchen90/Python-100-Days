#整型：int
#浮点型：float
#字符串：string '' ""
#布尔型： bool True False  例如3 < 5 会产生布尔值为True
#负数型：非常用，3+5j
a = 321
b = 12
print(a+b)
print(a-b)
print(a*b)
print(a/b)
c = 100
d = 12.345
e = 1 + 5j
f = "hello,world"
g = True
print(type(d))
print(type(e))
print(type(f))
print(type(g))
#类型转换
#int()：将一个数值或字符串转换成整数，可以指定进制。
#float()：将一个字符串转换成浮点数。
#str()：将指定的对象转换成字符串形式，可以指定编码。
#chr()：将整数转换成该编码对应的字符串（一个字符）。
#ord()：将字符串（一个字符）转换成对应的编码（整数）。
h = int(input('a = '))
i = int(input('b = '))
#说明：上面的print函数中输出的字符串使用了占位符语法，其中%d是整数的占位符，%f是小数的占位符，%%表示百分号（因为百分号代表了占位符，所以带占位符的字符串中要表示百分号必须写成%%），字符串之后的%后面跟的变量值会替换掉占位符然后输出到终端中，运行上面的程序，看看程序执行结果就明白啦。
# print('%d + %d = %d' % (h, i, h + i))
# print('%d - %d = %d' % (h, i, h - i))
# print('%d * %d = %d' % (h, i, h * i))
# print('%d / %d = %d' % (h, i, h / i))
# print('%d // %d = %d' % (h, i, h // i))
# print('%d %% %d = %d' % (h, i, h % i))
# print('%d ** %d = %d' % (h, i, h ** i))
# 你好  我好大家好  你是我的荣耀  杨洋带你打王者
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 算一下这里会输出什么