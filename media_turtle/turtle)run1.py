# turtle run 게임
import turtle as t
import random

# 적 거북이 생성
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

tf = t.Turtle()
tf.shape('circle')
tf.color('green')
tf.speed(0)
tf.shapesize(0.5)
tf.up()
tf.goto(0, -200)

def turn_right():
    t.setheading(0)
def turn_up():
    t.setheading(90)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)

def play():
    if t.distance(te) > 12:
        t.ontimer(play, 5)
    t.forward(10)
    te.forward(10)

    if random.randint(1, 5) == 4:
        ang = te.towards(t.pos())
        te.setheading(ang)

    if t.distance(tf) < 12:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x, y)

# 주인공 거북이
t.shape('turtle')
t.setup(500, 500) #width, height
t.bgcolor('orange')
t.color('white')
t.speed(0)
t.up()

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
play()

t.mainloop()