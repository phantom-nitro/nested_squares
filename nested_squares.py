from turtle import *
from theme import set_theme
import random
setup(1080, 1080)

def draw_square(x, y, s):
	penup()
	goto(x-s/2, y-s/2)
	pendown()
	for i in range(4):
		forward(s)
		left(90)

set_theme(thickness = 2)

noise = 4.5
noise2 = 3
size = 100
shrink = 15
shrink2 = 25

for x in range(-500+size//2, 500, size):
	for y in range(-500+size//2, 500, size):

		#outer square
		draw_square(x, y, size)

		#determine offset

		sampleList = [0,1]
  
		randomList = random.choices(sampleList, weights=(90,10))

		if randomList == [0]:
			x_off = random.uniform(-noise, noise)
			y_off = random.uniform(-noise, noise)

		elif randomList == [1]:
			x_off = random.uniform(-noise2, noise2)
			y_off = random.uniform(-noise2, noise2)

		#draw inner square
		randomList = random.choices(sampleList, weights=(80,20))
		if randomList == [0]:
			for i in range(7):
				draw_square(x+i*x_off, y+i*y_off, size-i*shrink)

		elif randomList == [1]:
			for i in range(4):
				draw_square(x+i*x_off, y+i*y_off, size-i*shrink2)

tracer(True)

exitonclick()
