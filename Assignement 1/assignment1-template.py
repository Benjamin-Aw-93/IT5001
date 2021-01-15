############################################
### CS1010E Assignment 1 - Hello Turtle! ###
############################################

### Part 1: Closed form calculations ###
# Kindly provide the complete expression, you may be penalized
# for giving only the final numerical result.

## a) Quadratic equations (15 marks) ##
# Provide an expression to find the two roots of 1010x^2 + 1009x - 1008 = 0

from math import sin, pi, asin
from turtle import *
from math import sqrt

a = 1010
b = 1009
c = -1008
# Replace these with your full, complete expressions
ans1 = (- b + sqrt(b**2 - 4 * a * c)) / (2 * a)
ans2 = (- b - sqrt(b**2 - 4 * a * c)) / (2 * a)

## b) Snell's law (15 marks) ##
# Find the incidence angle, theta_1, given that theta_2 = 20 degrees,
# n_1 = 1.33 and n_2 = 2.417.


def deg_to_rad(degree):
    return degree * pi/180


def rad_to_deg(radians):
    return radians * 180/pi


n1 = 1.33
n2 = 2.417
deg2 = deg_to_rad(20)

ans = rad_to_deg(asin((n2 * sin(deg2)) / n1))  # Replace this with your full, complete expression

### Part 2: Simple Turtle ###

## Warmup ##
# In the following sequences of function calls, try to imagine what will be drawn.
# Then, run the calls yourself on Python. Did it draw what you had expected?
# Uncomment each block to run the commands


forward(100)
backward(100)
forward(100)
backward(100)

# Expected answer: A line
# Final answer: A line


backward(100)
pu()
left(90)
forward(100)
right(90)
forward(100)

# Expected answer: A line with the cursor away
# Final answer: A line with the cursor away


backward(100)
left(90)
forward(100)
right(90)
forward(100)


# Expected answer:E without the middle part
# Final answer: E without the middle part


right(90)
left(180)
right(315)
backward(100)
right(90)
backward(100)

# Expected answer: >
# Final answer: >

## Now you try! (20 marks) ##
# With the functions that you have learnt so far, call a sequence of Turtle
# commands to draw an equilateral triangle with a distance of 300 units on each side,
# with the bottom of the triangle being parallel to the (imaginary) x-axis and
# the bottom left corner of the triangle corresponding to the starting point of turtle.
# Refer to the PDF for an example of how it should be drawn.


# Commands go here
forward(300)
left(120)
forward(300)
left(120)
forward(300)
left(120)
