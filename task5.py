import turtle
import random
brain = turtle.Turtle()

color = ['red', 'magenta', 'blue']

def get_random_color():
    return random.choice(color)

def draw(length, color):
    brain.fillcolor(color)
    brain.color(get_random_color(), get_random_color())
    brain.begin_fill()

    for i in range(4):
        brain.fd(length)
        brain.left(90)

    brain.end_fill()

for step in range(len(color)):
    draw(100, color[step])
    brain.left(90)

brain.up()
brain.fd(150)
brain.down()
brain.left(90)
brain.circle(150)

input()
