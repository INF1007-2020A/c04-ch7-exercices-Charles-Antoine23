from turtle import *

def draw_tree():
    setheading(90)
    color('green')
    draw_branch()
    done()

def draw_branch(branch_len = 70, pen_size = 7, angle = 35):
    if branch_len > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)



draw_tree()
