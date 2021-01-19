from turtle import Turtle, Screen

def kresliListek(listek, radius):
    heading = listek.heading()
    listek.circle(radius, 60)
    listek.left(120)
    listek.circle(radius, 60)
    listek.setheading(heading)
    listek.hideturtle()
    listek.speed(50)

prumer = int(200)       # velikost kytky
pocetListku = int(input("Kolik mam nakreslit okvetnich listku? "))
listek = Turtle()

for i in range(pocetListku):    #smycka na kresleni
    kresliListek(listek, prumer)
    listek.left(360 / pocetListku) #360 stupnu / poctem kvuli velikosti

screen = Screen()               #bez screenu by to hned zmizelo
screen.exitonclick()
