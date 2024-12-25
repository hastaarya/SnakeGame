from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen() 
screen.setup(600,600) #setup screen 600x600
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

#Listen for any keyboard inputs
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

#while loop to start the game
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15: #if the snake has < 15 distance from the food meaning it has collided (each pixel is around 20)
        food.refresh() #reset the food
        snake.extend() #increase snake length
        score.increase_score() #update score

    # Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280: #if the snake goes out of bound
        snake.reset_snake()
        score.reset_score()

    #Detect collision with tail
    for segment in snake.segments[1:]: #check whether or not the snake head hit the other segment starting from second (first one is head)
        if snake.head.distance(segment)<10: #checking for every segment of the snake 
            snake.reset_snake()
            score.reset_score()

screen.exitonclick()