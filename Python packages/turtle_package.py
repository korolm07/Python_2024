from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color('LightGoldenrod')
for i in range(5):
    timmy.forward(100)
    timmy.right(144)
my_screen = Screen()
print (my_screen.canvheight)
my_screen.exitonclick()
