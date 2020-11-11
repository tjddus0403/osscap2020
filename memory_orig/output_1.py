import random
import turtle
import numpy as np


map = [[0 for col in range(16)] for row in range(32)]

#배열 값을 전부 0으로 두고 사용자가 지나가는 자리에 1로 전환하여 점등
#엔터 치면 고정시키기

for i in map:
	for j in i:
		if (map==1):
			print("■")
print( )


player = turtle.Turtle()
player.shape("square")
player.goto(random.randint(-300,300), random.randint(-300, 300))
screen = player.getscreen()

def left() :
        player.left(30)
def right():
        player.right(30)
def up() :
        player.forward(30)
def down() :
        player.backward(30)
def fix():
		player.enter(30)

screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(fix, "Enter")
