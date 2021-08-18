from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.title("My snake game")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
	my_screen.update()
	time.sleep(0.1)

	snake.move()

	# detect collision with distance method
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		score.increase_score()

	# detect collision
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		score.reset()
		snake.reset()
		# game_is_on = False
		# score.game_over()

	for segment in snake.my_snake_shape[1:]:
		if snake.head.distance(segment) < 10:
			score.reset()
			snake.reset()
				# game_is_on = False
				# score.game_over()

my_screen.exitonclick()
