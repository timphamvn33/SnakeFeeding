from turtle import Turtle, Screen
from Snake import Snake
from food import Food
from score import Score
import time

tim =Turtle('square')
staring_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
game_on = True

screen = Screen()
screen.title("Feeding Snake Game")
screen.bgcolor('black')
screen.setup(width =600, height=600)
screen.tracer(0)

food = Food()
snake = Snake()
score=Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:

    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food)<15:
        food.change_locate()
        snake.extend()
        score.count_score()



    if int(snake.head.xcor()) > 280 or int(snake.head.xcor()) < -280 or int(snake.head.ycor()) > 280 or int(snake.head.ycor()) < -280:
        game_on = False
        score.game_over()

    #detect any body of snake
    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            game_on =False
            score.game_over()




    snake.move()
    snake.head.speed("fastest")



screen.exitonclick()




