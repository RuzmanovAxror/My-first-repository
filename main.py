import turtle as t

t.speed(0)
t.bgcolor('black')
t.pencolor('orange')

def square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

for i in range(80):
    square(170)
    t.right(5)
    t.circle(50)

t.hideturtle()
t.done()