from turtle import Turtle
ALIGHMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.read_text()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.currentscore = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.currentscore} High Score: {self.high_score} ", align=ALIGHMENT, font=FONT)

    def reset(self):
        if self.currentscore > self.high_score:
            self.high_score =self.currentscore
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.currentscore = 0
        self.update()

    def read_text(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())












