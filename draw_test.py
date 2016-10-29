import turtle
import time
import random
#import srceen


#随机画图，随机移动，随机颜色

mycolor = ["blue","yellow","red","green","blown"]
#screen.colormode(255)
turtle.colormode(255)  #设置模式


def drawShape(sides,length):
    sides=int(sides) #需要转换类型，因为随机函数产生的是float型
    length=int(length)
    angle=360.0/sides
    r=random.uniform(1,255)
   
    g=random.uniform(1,255)
    b=random.uniform(1,255)
    r=int(r)
    g=int(g)
    b=int(b)
    print(r,g,b)
    turtle.begin_fill()
    turtle.fillcolor((r,g,b))
    
    for side in range(sides):
        turtle.forward(length)
        turtle.right(angle)
        
    turtle.end_fill()
       

def moveTurtle(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

while True:
    time.sleep(1) #使用定时器
    sides=random.uniform(1,30)  #最多三十边
    l=random.uniform(1,50)  #最长50
    x=random.uniform(-500,500)
    y=random.uniform(-500,500)
    moveTurtle(x,y)
    drawShape(sides,l)

