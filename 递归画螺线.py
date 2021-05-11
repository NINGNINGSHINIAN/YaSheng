import turtle
t = turtle.Turtle()


def drawSpiral(lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(lineLen - 4)
    

drawSpiral(64)
