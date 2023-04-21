# 거북이 대포 게임
# 화살촉 모양의 포탄이 하늘로 날아감
# 스페이스바로 발사, 키보드 방향키로 발사각도 조절
import turtle as t
import random

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()

    while t.ycor() > 0:
        t.forward(5)
        t.right(5)

    d = t.distance(target, 0)
    t.sety(random.randint(10, 100))
    if d <25:
        t.color('blue')
        t.write('Good!', False, "center",("", 15))
    else:
        t.color('red')
        t.write('Bad!', False, "center",("", 15))
        t.color('black')
        t.goto(-200, 10)
        t.setheading(ang)

t.goto(-300, 0)
t.goto(300, 0)

target = random.randint(50, 150)
t.color('green')
t.pensize(2)
t.up
t.goto(target-25, 1)
t.down
t.goto(target+25, 1)

t.color('black')
t.up()
t.goto(-200, 10)
t.setheading(20)

t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire, "space")
t.listen()

t.mainloop()