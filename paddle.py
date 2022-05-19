import constants as c

from turtle import Turtle
from time import sleep


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for index in range(-2, 2):
            segment = Turtle()
            segment.color("green")
            segment.shape("square")
            segment.penup()
            segment.goto(index * 20, 10 - c.HEIGHT / 2)
            segment.setheading(0)
            segment.velocity = 10
            segment.id = index
            self.segments.append(segment)

    def move_left(self):
        if self.segments[0].xcor() > 7 - c.EDGE_LR:
            self.move(180)

    def move_right(self):
        if self.segments[-1].xcor() < c.EDGE_LR - 8:
            self.move(0)

    def move(self, heading):
        for segment in self.segments:
            segment.setheading(heading)
            segment.forward(segment.velocity)


if __name__ == "__main__":
    from turtle import Screen

    screen = Screen()
    screen.colormode(255)
    screen.setup(width=c.WIDTH, height=c.HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    paddle = Paddle()

    screen.onkeypress(paddle.move_left, "a")
    screen.onkeypress(paddle.move_left, "Left")
    screen.onkeypress(paddle.move_right, "d")
    screen.onkeypress(paddle.move_right, "Right")
    screen.listen()

    while True:
        screen.update()
        sleep(0.01)

    screen.exitonclick()