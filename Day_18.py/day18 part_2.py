from turtle import Turtle , Screen
import random
tony = Turtle()


colors = ['CornflowerBlue', 'Dark Orchid','wheat', 'Gold', 'DeepSkyBlue', 'LawnGreen', 'Magenta', 'MediumOrchid', 'MediumPurple', 'Red', 'SpringGreen', 'Turquoise', 'Violet']

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):
        tony.right(angle)
        tony.forward(100)
for shape in range(3,11):
    tony.color(random.choice(colors))
    draw_shape(shape)


screen = Screen()
screen.exitonclick()