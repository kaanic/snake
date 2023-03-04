from turtle import Turtle
FONT, ALIGNMENT = ('Courier', 18, 'normal'), 'center'


class Scoreboard(Turtle):

    def __init__(self, score=0):
        super().__init__()
        self.score = score
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def get_a_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)