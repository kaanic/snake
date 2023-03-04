from turtle import Turtle

LOCATIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create()
        self.head = self.squares[0]

    def create(self):
        for location in LOCATIONS:
            new_square = Turtle('square')
            new_square.color('white')
            new_square.penup()
            new_square.goto(location)
            self.squares.append(new_square)

    def move(self):
        for sq in range(len(self.squares) - 1, 0, -1):
            x = self.squares[sq - 1].xcor()
            y = self.squares[sq - 1].ycor()
            self.squares[sq].goto(x=x, y=y)
        self.head.forward(DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def get_bigger(self):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(self.squares[len(self.squares)-1].xcor(), self.squares[len(self.squares)-1].ycor())
        self.squares.append(new_square)