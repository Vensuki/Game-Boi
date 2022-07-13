import turtle

pos = [0, -20, -40]
move_distance = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.add_segment(i)

    def add_segment(self, i):
        timmy = turtle.Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        # timmy.goto(x=pos[i], y=0)
        # timmy.shapesize(0.6,0.6)
        self.segments.append(timmy)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if not self.segments[0].heading() == 270:
            self.segments[0].setheading(90)
            self.segments[0].forward(move_distance)
        else:
            print("Game Over!")

    def down(self):
        if not self.segments[0].heading() == 90:
            self.segments[0].setheading(270)
            self.segments[0].forward(move_distance)
        else:
            print("Game Over!")

    def right(self):
        if not self.segments[0].heading() == 180:
            self.segments[0].setheading(0)
            self.segments[0].forward(move_distance)
        else:
            print("Game Over!")

    def left(self):
        if not self.segments[0].heading() == 0:
            self.segments[0].setheading(180)
            self.segments[0].forward(move_distance)
        else:
            print("Game Over!")

    def position(self):
        self.segments[0].pos()
