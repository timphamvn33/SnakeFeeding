from turtle import Turtle
ALIGN="center"
FONT=("Arial", 24, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.setheading(90)
        self.penup()
        self.forward(250)
        self.write(f"score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def count_score(self):
        self.score +=1
        self.clear()
        self.write(f"score: {self.score}", align=ALIGN, font=FONT)
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"  Score: {self.score}\nGame Over", align=ALIGN, font=FONT)


