import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
width=wn.window_width()
x1=(0-(width-30)/3)
x2=0
x3=0+(width-30)/3
def TriangleAT(x,y,size):
	t1.setheading(0)
	t1.penup()
	t1.goto(x,y)
	t1.pendown()
	for i in range(1,5):
		t1.fd(size)
		t1.left(120)

def PentagonAT(x,y,size):
	t1.setheading(0)
	t1.penup()
	t1.goto(x,y)
	t1.pendown()
	t1.left(36)
	t1.fd(size)
	for i in range(1,5):
		t1.right(72)
		t1.fd(size)

def StarAT(x,y,size):
	t1.setheading(0)
	t1.penup()
	t1.goto(x,y)
	t1.pendown()
	t1.fd(size)
	for i in range(1,5):
		t1.right(144)
		t1.fd(size)

TriangleAT(x1,0,100)
PentagonAT(x2,0,100)
StarAT(x3,0,100)
wn.exitonclick()