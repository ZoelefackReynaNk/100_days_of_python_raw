import turtle as t
#creating an obj called object1 by accessing the Turtle class from the turtle module
#from turtle import Turtle
object1 = t.Turtle()
myscreen = t.Screen()
#object myscreen with attributes canvheight and canvwidth
y = myscreen.canvheight
x = myscreen.canvwidth
object1.color('yellow')
print(x, y)
object1.forward(200)

#screen.exitonclick()