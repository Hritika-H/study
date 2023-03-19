import turtle
import random

window=turtle.Screen()
window.title("Turtle Game")
window.bgcolor("black")

p1=turtle.Turtle()
p1.shape("turtle")
p1.pensize(5)
p1.penup()

p2=p1.clone()
p1.color("yellow")
p2.color("green")
p1.setposition(-200,200)
p2.setposition(-200,-200)

home1=turtle.Turtle()
home1.shape("circle")
home1.color("white")
home1.pensize(2)
home1.penup()
home2=home1.clone()
home1.setposition(200,200)
home1.pendown()
home1.circle(20)
home2.setposition(200,-200)
home2.pendown()
home2.circle(20)

dice=[1,2,3,4,5,6]



for i in range(15):
    if(p1.pos()>=home1.pos()):
        print("Yay! Player yellow won the game! Thanks for playing!")
    elif(p2.pos()>=home2.pos()):
        print("Yay! Player green won the game!")
    else:
        #Player1's turn
        aa=input("Player yellow press Enter to roll the dice!")
        outcome=random.choice(dice)
        print("Player1 got:",outcome)
        p1.fd(10*outcome)
        #Player2's turn
        aa=input("Player green press Enter to roll the dice!")
        outcome=random.choice(dice)
        print("Player1 got:",outcome)
        p2.fd(10*outcome)






