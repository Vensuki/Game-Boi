import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.write(f"Score = {self.score}", align='Center', font=('Arial', 18, 'normal'))
        self.score_count()

    def score_count(self):
        self.clear()
        self.score += 1
        self.goto(x=0, y=270)
        self.write(f"Score = {self.score}", align='Center', font=('Arial', 18, 'normal'))
