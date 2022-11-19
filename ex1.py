import turtle
import turtle as tr
from turtle import Turtle, Screen


a = input('Enter the axis: ')
velo = int(input('Enter the velocity: '))
tim = int(input('Enter the time: '))
if velo < 0.01 and tim < 0.01:
    print('---------------RESTART----------------')
    velo = int(input('Enter the velocity: '))
    tim = int(input('Enter the time: '))


t = Screen()
t.setup(700,700)

class Finder:

    gravity = 9.8

    def __init__(self, velocity, time):
        self.v = velocity
        self.t = time

    def find_velocity(self): # v = gt
        self.v = self.gravity * self.t
        return self.v

    def find_time(self):
        self.t = self.v / self.gravity
        return self.t


class Finder2(Finder): # h=vt+at**2/2

    def find_height(self):
        self.height = self.v * self.t + self.gravity * (self.t**2) / 2
        return self.height


f = Finder2(velo, tim)

print('Height = ',f.find_height(), 'm')

if velo == 0 and tim > 0.01:
    fn = Finder2(0, tim)
    print('Velocity = ', fn.find_velocity(), 'm/s')

elif velo > 0.01 and tim == 0:
    fn = Finder2(velo, 0)
    print('Time = ', fn.find_time(), 's')


if a == 'y':
    border = turtle.Turtle()
    border.hideturtle()
    border.speed(0)
    border.pensize(5)
    border.up()
    border.goto(-250, - f.find_height() - 5)
    border.down()
    border.goto(250, - f.find_height() - 5)
    speedY = -1
    t = tr.Turtle()
    t.speed(1)
    t.shape("circle")
    window = tr.Screen()
    tr.color("black")
    window.bgcolor("yellow")
    t.pencolor('yellow')
    t.goto(0, -f.find_height() + speedY)
    t.goto(0, 0)
    window.mainloop()


if a == 'x':
    speedX = -1
    t = tr.Turtle()
    t.shape("circle")
    window = tr.Screen()
    tr.color("black")
    window.bgcolor("white")
    t.pencolor('yellow')
    t.goto(f.find_height() + speedX, 0)
    window.mainloop()







