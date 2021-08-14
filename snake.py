from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
	def __init__(self):
		self.my_snake_shape = []
		self.create_snake()
		self.head = self.my_snake_shape[0]

	def create_snake(self):
		for position in STARTING_POSITIONS:
			self.add_snake_shape(position)

	def add_snake_shape(self, position):
		my_snake = Turtle("square")
		my_snake.color("white")
		my_snake.penup()
		my_snake.goto(position)
		self.my_snake_shape.append(my_snake)

	def extend(self):
		self.add_snake_shape(self.my_snake_shape[-1].position())

	def move(self):
		for single in range(len(self.my_snake_shape) - 1, 0, -1):
			new_x = self.my_snake_shape[single - 1].xcor()
			new_y = self.my_snake_shape[single - 1].ycor()
			self.my_snake_shape[single].goto(new_x, new_y)
		self.my_snake_shape[0].forward(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)
