import turtle
t = turtle.Turtle()


def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(40)
        tree(branch_len - 20)
        t.left(80)
        tree(branch_len - 20)
        t.right(40)
        t.backward(branch_len)


t.left(90)
t.penup()
t.backward(105)
t.pendown()
t.pencolor('green')
t.pensize(3)
tree(75)
t.hideturtle()
turtle.done()