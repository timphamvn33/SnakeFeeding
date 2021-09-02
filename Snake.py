from turtle import Turtle
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE =20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def add_segment(self, postion):
        tim = Turtle('square')
        tim.penup()
        tim.color('white')
        tim.goto(postion)
        self.segments.append(tim)

    def move(self):

        for se_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[se_num - 1].xcor()
            new_y = self.segments[se_num - 1].ycor()
            self.segments[se_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)




    def up(self):
        if self.head.heading()!=DOWN:
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

    def collison_wall(self):
        if self.head.xcor()==280 or self.head.xcor()==-280 or self.head.ycor()==280 or self.head.ycor==-280:
            return False




