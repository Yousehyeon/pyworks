# 좌표이동
import turtle as t
import time
import random

t.shape('turtle')
t.shapesize(20)
"""
t.up()
time.sleep(1)
t.goto(0, 150)
time.sleep(0)
t.goto(100, 150)
time.sleep(1)
t.goto(0,0)
"""
"""
x = random.randint(-250, 250)
y = random.randint(-250, 250)
t.up()
t.goto(x, y)
"""

#ㅈ대로 걷는 거북이
t.speed(0)
for x in range(100):
    ang = random.randint(1, 360)
    t.setheading(ang)
    t.forward(50)

t.mainloop()