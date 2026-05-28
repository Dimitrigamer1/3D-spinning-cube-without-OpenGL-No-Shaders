#Without OpenGL & No Shaders
#Made by dimitrigamer1

import turtle
import math

points = (
    [1,1,1],
    [1,1,-1],
    [1,-1,1],
    [1,-1,-1],
    [-1,1,1],
    [-1,1,-1],
    [-1,-1,1],
    [-1,-1,-1]
)

edges = (
    (0,1),(1,3),
    (3,2),(2,0),
    (4,5),(5,7),
    (7,6),(6,4),
    (0,4),(1,5),
    (2,6),(3,7)
)

s = turtle.Screen()
s.bgcolor("black")
s.title("3D CUBE")
s.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.color("cyan")


angle = 0

while True:
    t.clear()
    projected_points = []

    for p in points:
        x = p[0]
        y = p[1]
        z = p[2]

        nx = x * math.cos(angle) - z * math.sin(angle)
        nz = x * math.sin(angle) + z * math.cos(angle)
        ny = y

        z_view = nz + 3
        sx = (nx / z_view) * 250
        sy = (ny / z_view) * 250

        projected_points.append((sx, sy))

    for egde in edges:
        p1 = projected_points[egde[0]]
        p2 = projected_points[egde[1]]

        t.penup()
        t.goto(p1)
        t.pendown()
        t.goto(p2)

    s.update()
    angle += 0.001