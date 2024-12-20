import turtle as t

import random
tim = t.Turtle()
t.colormode(255)
# colors = ['Indian red','','DarkOrchid','wheat','Gold','DeepSkyBlue',
#           'LawnGreen','Magenta','MediumOrchid','MediumPurple','Red',
#           'SpringGreen','Turquoise','Violet']

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color




directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")



for _ in range(200):
    # tim.color(random.choice(colors))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))