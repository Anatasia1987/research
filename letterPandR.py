import turtle

t = turtle.Turtle()

t.reset()
t.pencolor('purple')
t.pensize(5)
t.penup()
t.goto(-300,200)

#p
t.pendown()
t.fd(20)
t.circle(-30, 180)
t.fd(20)
t.rt(90)
t.fd(60)
t.bk(60)
t.lt(180)
t.fd(60)

t.penup()
t.goto(-230,200)
t.setpos(100,100)

#R
t.pendown()
t.lt(90)
t.fd(20)
t.circle(-30,180)
t.fd(20)
t.rt(90)
t.fd(60)
t.bk(60)
t.lt(180)
t.fd(60)
t.bk(60)
t.lt(45)
t.fd(80)
t.rt(45)

t.penup()
t.goto(-160,200)

turtle.done()
