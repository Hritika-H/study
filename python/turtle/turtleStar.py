import turtle
window=turtle.Screen()
window.bgcolor("black")
window.title("Star")
t=turtle.Turtle()

#basic code for a star
"""
t.goto(200,200)
t.color("yellow")
t.pendown()
t.fillcolor("orange")
t.begin_fill()
for i in range(5):
    t.right(144)
    t.forward(100)
    
t.end_fill()
"""
#function to take goto, colour, size and print a star
def printStar(locX,locY,colour,size):
    print("Printing a star for you!")
    t.setposition(locX,locY)
    t.color(colour)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    for i in range(5):
        t.right(144)
        t.forward(size)
    t.end_fill()
    t.penup()
