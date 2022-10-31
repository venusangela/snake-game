from turtle import Turtle
FONT = ("Arial", 15, "normal")
ALIGN = 'center'
Y_SCORE = 270

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, Y_SCORE)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = self.read_score()
        self.color("white")
        self.speed("fastest")
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(align=ALIGN, font=FONT, arg=f"Score = {self.score} High Score: {self.high_score}")

    def score_up(self):
        self.score += 1
        self.show_score()

    def read_score(self):
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
            return self.high_score

    def write_score(self):
        with open("data.txt", mode='w') as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(align=ALIGN, font=FONT, arg="Game Over.")
