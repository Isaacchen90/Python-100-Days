import sys
print(sys.version_info)
print(sys.version)
"""
这是一个注释
"""
print("Hello world!")
# print("你好，世界！")
import turtle#这是一个图形绘制框
turtle.pensize(4)#设置笔刷大小
turtle.pencolor('red')#设置颜色为红色

turtle.forward(100)#向前100
turtle.right(90)#向右90
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()