from turtle import Screen , Turtle
timy = Turtle()
timy.shape("turtle")
timy.color("red", "sky blue")
for _ in range (4):
    timy.forward(100)
    timy.right(90)


tony = Turtle()
tony.shape("turtle")
tony.color("green")
for _ in range (15):
    tony.forward(10)
    tony.penup()
    tony.forward(10)
    tony.pendown()



screen = Screen()
screen.exitonclick()