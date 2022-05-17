from turtle import *

def set_theme(canvas_width = 1000, canvas_height = 1000, canvas_color = (242/255,242/255,242/255), pen_color = (0,0,0), thickness = 1, speed_value = 0, tracer_value = False,
	hide_turtle = True):
	setup(canvas_width, canvas_height)
	bgcolor(canvas_color)
	color(pen_color)
	width(thickness)
	speed(speed_value)
	tracer(tracer_value)
	if hide_turtle:
		hideturtle()
