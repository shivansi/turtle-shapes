# import turtle

# turtle.title("My turtle game")
# turtle.bgcolor("green")
# turtle.setup(600,600)
# turtle.shape("turtle")

# screen=turtle.Screen()
# speedy=turtle.Turtle()

# input_shape=input("what shape do you want to draw?: ")
# input_length=input("choose how big: ")
# input_color=input("choose color: ")

# def triangle(length,color):
#   speedy.fillcolor(color)
#   speedy.begin_fill()

#   x=0
#   while x<3:
#     speedy.forward(int(length))
#     speedy.right(120)
#     x=x+1
#   speedy.end_fill()


# def square(length,color):
#   speedy.fillcolor(color)
#   speedy.begin_fill()

#   x=0
#   while x<4:
#     speedy.forward(int(length))
#     speedy.right(120)
#     x=x+1
#   speedy.end_fill()

# def circle(length,color):
#   speedy.fillcolor(color)
#   speedy.begin_fill()

#   x=0
#   while x<36:
#     speedy.forward(int(length))
#     speedy.right(10)
#     x=x+1
#   speedy.end_fill()

# def star(length,color):
#   speedy.fillcolor(color)
#   speedy.begin_fill()

#   x=0
#   while x<5:
#     speedy.forward(int(length))
#     speedy.right(144)
#     x=x+1
#   speedy.end_fill()

# if input_shape.lower=="triangle":
#   triangle(input_length,input_color)
# elif input_shape.lower()=="square":
#   square(input_length,input_color)
# elif input_shape.lower()=="circle":
#   circle(input_length,input_color)
# elif input_shape.lower()=="star":
#   star(input_length,input_color)

import turtle

turtle.title("my turtle game")
turtle.bgcolor("black")
turtle.setup(600,600)

screen=turtle.Screen()
bob=turtle.Turtle()
bob.color("white")
bob.speed(0)
bob.pensize(3)
bob.shape("turtle")
sides=5

def spiral(angle,increase):
  steps=5
  for i in range(500):
    bob.forward(steps)
    bob.left(angle)
    steps+=increase

spiral(angle=360/sides+1,increase=1)  
