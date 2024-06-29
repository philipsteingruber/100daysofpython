from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake(body_length=15)
food = Food()
scoreboard = Scoreboard()
scoreboard.draw_scoreboard()

screen.listen()
screen.delay()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

running = True
while running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        running = False
        print(snake.head.pos())

    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            running = False
            print('crashed')

screen.exitonclick()
