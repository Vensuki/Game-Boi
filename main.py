import turtle
import random
import time
import snake
import food
import score
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
timmy = turtle.Turtle()
timmy.speed("fastest")
timmy.hideturtle()
for i in range(72):
    timmy.circle(125)
    timmy.left(5)
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]
    timmy.color(random.choice(colours))

timmy.color("white")
timmy.penup()
timmy.goto(0, 150)
timmy.write("GAME-BOY", align='Center', font=('Courier', 60, 'bold'))
timmy.goto(0, 75)
time.sleep(0.2)
timmy.write("1. Turtle Race", align='Center', font=('Times New Roman', 30, 'italic'))
timmy.goto(0, -35.5)
time.sleep(0.2)
timmy.write("2. Turtle Crossing", align='Center', font=('Times New Roman', 30, 'italic'))
timmy.goto(0, -150)
time.sleep(0.2)
timmy.write("3. Snake ", align='Center', font=('Times New Roman', 30, 'italic'))

time.sleep(2)
choice = screen.textinput(title="Let's Play!", prompt="Enter the game number you would like to play")
print(choice)
chosen = int(choice)
screen.clear()
if chosen == 1:
    screen = turtle.Screen()
    is_race_on = False
    screen.setup(width=500, height=500)
    colors = ["blue", "pink", "red", "yellow", "green", "purple"]
    y_pos = [-100, -50, 0, 50, 100, 150]
    turtles = []
    tommy = turtle.Turtle()
    tommy.penup()
    tommy.goto(x=210, y=240)
    tommy.right(90)
    tommy.pendown()
    tommy.forward(480)
    tommy.speed("fastest")
    tommy.hideturtle()
    for i in range(6):
        timmy = turtle.Turtle(shape="turtle")
        timmy.color(colors[i])
        timmy.penup()
        timmy.goto(x=-240, y=y_pos[i])
        turtles.append(timmy)
        timmy.speed("fastest")

    choice = screen.textinput(title="Place your bets", prompt="Which turtle you think will win the race?")
    print(choice)
    if choice:
        is_race_on = True
    while is_race_on:
        for i in turtles:
            if i.xcor() > 210:
                winner = i.pencolor()
                is_race_on = False
                if winner == choice:
                    print(f"You win! The winner is {winner}")
                else:
                    print(f"You lose! The winner is {winner}")
            i.forward(random.randint(1, 15))

    screen.exitonclick()

elif chosen==2:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    turtle_player = Player()
    cars = CarManager()
    score = Scoreboard()
    screen.listen()
    screen.onkey(turtle_player.up, "Up")
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        cars.create_car()
        cars.move()
        if turtle_player.ycor() > 290:
            turtle_player.player_reset()
            cars.level_up()
            score.next_level()
        for car in cars.all_cars:
            if car.distance(turtle_player) < 25:
                score.game_over()
                game_is_on = False

    screen.exitonclick()

elif chosen==3:
    snake = snake.Snake()
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("Snake")
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()
    # boundary=turtle.Turtle()
    # boundary.penup()
    # boundary.goto(-287,287)
    # boundary.pendown()
    # boundary.color("white")
    # for i in range(4):
    #     boundary.forward(574)
    #     boundary.right(90)
    # boundary.hideturtle()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    is_game_on = True
    food = food.Food()
    game_score = score.Score()
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        a = snake.position()
        x_cor = snake.segments[0].xcor()
        y_cor = snake.segments[0].ycor()
        if x_cor > 280 or x_cor < -280 or y_cor > 280 or y_cor < -280:
            game = turtle.Turtle()
            game.color("white")
            game.hideturtle()
            game.write("GAME OVER!", align="center", font=('Arial', 20, 'normal'))
            is_game_on = False

        if food.distance(snake.segments[0]) < 18:
            food.food_location()
            snake.extend()
            game_score.score_count()

    screen.exitonclick()
screen.exitonclick()

