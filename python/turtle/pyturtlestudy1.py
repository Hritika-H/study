import turtle

#CREATE THE WINDOW FOR OUTPUT
window=turtle.Screen()
window.bgcolor("black")
window.title("My Turtle Study")

tt=turtle.Turtle()
tt.color("white")
tt.pensize(5)

#SQUARE
"""
for i in range(4):
    tt.forward(50)
    tt.right(90)
turtle.done()
"""

#CIRCLE AND DOT
tt.circle(60)
#tt.dot(40)

#changes only turtle size, not line size
#tt.shapesize(1,5,10) 

#CHANGE PEN LINE SIZE
"""tt.pensize(5)
tt.forward(50)"""

#STAR
"""
for i in range(5): 
    tt.forward(50) 
    tt.right(144) 
"""

#HEXAGON WITH FILL COLOR
"""
tt.fillcolor("orange")
tt.begin_fill()
for i in range(6): 
    tt.forward(50) 
    tt.right(60)
tt.end_fill()
"""

#POLYGON
"""
num_sides = 10
side_length = 70
angle = 360.0 / num_sides  
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for i in range(num_sides): 
    tt.forward(side_length) 
    tt.right(angle)
    tt.pencolor(colors[i%6]) 
"""

# Python program to draw Spiral Helix Pattern 
""" 
tt.speed(2) 
for i in range(100): 
    tt.circle(5*i) 
    tt.circle(-5*i) 
    tt.left(i) 
"""

#RAINBOW BENZENE
"""
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
for x in range(360): 
    tt.pencolor(colors[x%6]) 
    tt.width(x/100 + 1) 
    tt.forward(x) 
    tt.left(59)
"""
#STAMP, TURTLE SHAPE CHANGE, PENUP & PENDOWN
"""
tt.shape("arrow")
tt.stamp()
tt.fd(100)
tt.stamp()
tt.shape("turtle")
tt.fd(100)
tt.stamp()
tt.shape("circle")
tt.fd(100)
tt.stamp()
tt.left(90)
tt.penup()
tt.fd(100)
tt.left(90)
tt.pendown()
tt.fd(300)
"""

#CLONE, POS AND GOTO(setpostion can also be used)
"""
c=tt.clone()
tt.color("red")
c.color("blue")
tt.circle(60)
c.circle(100)
print(c.pos())
c.goto(0,-50)
"""
