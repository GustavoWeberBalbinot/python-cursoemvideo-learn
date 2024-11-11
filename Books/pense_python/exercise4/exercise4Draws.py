#polygons (tortas de tartaruga)
import turtle
import math

#polygon 1:
def polygon1(bob,lenght):
    bob.lt(35)
    for x in range(0,6):
        bob.fd(lenght)
        bob.lt(121)
        bob.fd(lenght)
        bob.lt(119)
        bob.fd(lenght)
        bob.lt(180)
    turtle.mainloop()


#polygon 2:

def polygon2(bob,lenght):
    bob.lt(90)
    for x in range(0,6):
        bob.fd(lenght)
        bob.lt(120)
        bob.fd(lenght)
        bob.lt(120)
        bob.fd(lenght)
        bob.lt(180)
    turtle.mainloop()

bob = turtle.Turtle()


#polygon 3:

def polygon3(bob, lenght, n):
    angle = 360/n
    for x in range(n):
        bob.fd(lenght)
        current_position = bob.pos()
        bob.goto(lenght/2, lenght)
        bob.goto(current_position)
        bob.lt(angle)
    turtle.mainloop()


#polygon3(bob, 100, 7)


#Flowers2

def flower2(bob, r, angle, n):
    angle_total = 360/n
    circumference = 2 * math.pi * r
    arc_length = circumference * (angle / 360)
    segments = 100 
    segment_length = arc_length / segments + 1
    turn_angle = angle / segments
    for x in range(8):
        for x in range(segments):
            bob.fd(segment_length)
            bob.lt(turn_angle)
        bob.lt(90)
        for x in range(segments):
            bob.fd(segment_length)
            bob.lt(turn_angle)
        bob.lt(45)
    turtle.mainloop()

flower2(bob, 10, 90, 7)