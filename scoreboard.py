FONT = ("Courier", 24, "normal")
import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level=1
        self.penup()
        self.color("black")
        self.goto(-250,250)
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def next_level(self):
        self.clear()
        self.level+=1
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)



