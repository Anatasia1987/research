import turtle
import random
# create a green turtle and draw an "R"
colors = ["red", "green", "blue", "yellow", "orange",
          "purple", "pink", "brown", "black", "white"]
t = turtle.Turtle()
# set the pen size to 30
t.pensize(15)

def get_random_color():
    # pick a random color from the colors list
    cooler = (colors[random.randint(0, len(colors) - 1)])
    return cooler

# go to a random location
t.penup()
t.goto(random.randint(-300, 100), random.randint(-300, 100))
t.pendown()
# set the turtle to point up
t.left(90)

def draw_letter_A():
    t.begin_fill()
    t.fillcolor(get_random_color())
    # set the pen color to the random color
    t.pencolor(get_random_color())
    # make sure the pen is down
    t.pendown()
    # draw the letter A
    t.left(15)
    t.forward(200)
    t.left(60)
    t.forward(200)
    # reset the turtle to point up

def draw_letter_R():
    t.begin_fill()
    t.fillcolor(get_random_color())
    # set the pen color to the random color
    t.pencolor(get_random_color())
    # draw the letter R
    t.forward(220)
    t.left(270)
    t.circle(-50, 180)
    t.left(135)
    t.forward(140)
    t.left(135)

def draw_letter_M():
    t.begin_fill()
    t.fillcolor(get_random_color())
    # set the pen color to the random color
    t.pencolor(get_random_color())
    # draw the letter M
    t.forward(200)
    t.right(135)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(135)
    t.forward(200)
    # reset the turtle to point up
      
def draw_dot():
    t.pencolor(get_random_color())
    t.dot(20)

for i in range(1):
    draw_letter_R()
    draw_dot()
    draw_letter_M()
    draw_dot()
    draw_letter_A()
    draw_dot()
# for each letter in the alphabet create a function
# that draws the letter
    
# exit on click
turtle.exitonclick() 
