from turtle import Turtle

MOVEMENT_SPEED = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:
    def __init__(self, body_length: int):
        self.segments: list[Turtle] = []
        for i in range(body_length):
            turtle = self.create_segment()
            turtle.setx(-(20 * i))
            self.segments.append(turtle)
        self.head = self.segments[0]

    def create_segment(self) -> Turtle:
        turtle = Turtle('square')
        turtle.color('white')
        turtle.penup()
        return turtle

    def grow(self) -> None:
        new_segment = self.create_segment()
        new_segment.goto(self.segments[-1].pos())
        self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[i - 1].pos()
            self.segments[i].goto(new_pos)
        self.head.forward(MOVEMENT_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
