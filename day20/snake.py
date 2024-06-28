from turtle import Turtle

MOVEMENT_SPEED = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:
    def __init__(self, body_length: int = 3):
        self.segments: list[Turtle] = []
        for i in range(body_length):
            turtle = Turtle('square')
            turtle.color('white')
            turtle.penup()
            turtle.setx(-(20 * i))
            self.segments.append(turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[i - 1].pos()
            self.segments[i].goto(new_pos)
        self.segments[0].forward(MOVEMENT_SPEED)

    def up(self):
        head = self.segments[0]
        if head.heading() != DOWN:
            head.setheading(UP)

    def down(self):
        head = self.segments[0]
        if head.heading() != UP:
            head.setheading(DOWN)

    def left(self):
        head = self.segments[0]
        if head.heading() != RIGHT:
            head.setheading(LEFT)

    def right(self):
        head = self.segments[0]
        if head.heading() != LEFT:
            head.setheading(RIGHT)
