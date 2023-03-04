import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake1 = Snake()
food1 = Food()
scoreboard1 = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake1.go_up)
screen.onkey(key='Down', fun=snake1.go_down)
screen.onkey(key='Left', fun=snake1.go_left)
screen.onkey(key='Right', fun=snake1.go_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()
    if snake1.head.distance(food1) < 15:
        food1.refresh()
        snake1.get_bigger()
        scoreboard1.get_a_score()
    if snake1.head.xcor() > 280 or snake1.head.ycor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() < -280:
        scoreboard1.game_over()
        game_is_on = False
    for square in snake1.squares[1:]:
        if snake1.head.distance(square) < 10:
            scoreboard1.game_over()
            game_is_on = False
print(f'Game over. Your final score is {scoreboard1.score}.')

screen.exitonclick()
