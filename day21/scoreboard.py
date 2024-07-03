from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.goto(0, 270)
        self.clear()
        self.write(
            f"Score: {self.score}", align="center", font=("Courier", 22, "normal")
        )
