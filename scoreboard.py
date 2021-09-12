from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.updateLevel()

    def updateLevel(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level} ", align="center", font=FONT)

    def scorePoint(self):
        self.level +=1
        self.updateLevel()
