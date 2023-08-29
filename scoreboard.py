from turtle import Turtle
from snake import Snake
from food import Food


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 16, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()


    def gameover(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER" , align='center', font=('Arial', 30, 'normal'))