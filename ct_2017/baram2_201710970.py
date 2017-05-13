import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def giyuk(size):
    t1.fd(size)
    t1.right(90)
    t1.fd(size)
i=0
while i in range(0,8) :
    i=i+1
    giyuk(100)
    t1.penup()
    t1.home()
    t1.pendown()
    t1.right(45*i)
wn.exitonclick()