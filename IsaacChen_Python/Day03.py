"""
       3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
# x = float( input('请输入一个数字'))
# if x > 1 :
#     y = 3 * x - 5
# else:
#     if x < -1:
#         y = 5 * x + 3
#     else:
#         y = x + 2
# print("运算结果%f，请猜下怎么运算的。" % (y))

# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))

# """
# 英制单位英寸和公制单位厘米互换
# 1英寸 = 2.54厘米
# """
# a = float(input("请输入长度"))
# b = str(input("请输入单位"))
# if b == 'int' or b =='英寸':
#     print("%f英寸 = %f 厘米" %  (a , 2.54 * a))
# elif b == 'cm' or b =='厘米':
#     print("%f英寸 = %f 厘米" % (a/2.54 , a))

"""
要求：
如果输入的成绩在90分以上（含90分）
输出A；80分-90分（不含90分）
输出B；70分-80分（不含80分）
输出C；60分-70分（不含70分）
输出D；60分以下输出E。
"""
# a = int(input('输入分数：'))
# string = "获得评级为："
# if a >= 90:
#     print(string,'A')
# elif a >= 80:
#     print(string,'B')
# elif a >= 70:
#     print(string,'C')
# elif a >= 60:
#     print(string,'D')
# else:
#     print(string,'E')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')