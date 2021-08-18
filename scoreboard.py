from turtle import Turtle

ALIGNMENT = "center"
FONTS = ("Courier", 24, "bold")


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		with open("file1.txt", mode="r") as file:
			self.high_score = int(file.read())
		self.color("white")
		self.penup()
		self.goto(0, 260)
		self.hideturtle()
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.color("blue")
		self.write(f"Score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONTS)

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
		with open("file1.txt", mode="w") as file:
			file.write(str(self.high_score))
		self.score = 0
		self.update_scoreboard()

	def increase_score(self):
		self.score += 1
		self.update_scoreboard()


	# def game_over(self):
	# 	self.goto(0, 0)
	# 	self.color("red")
	# 	self.write("GAME OVER 👽", align=ALIGNMENT, font=FONTS)
