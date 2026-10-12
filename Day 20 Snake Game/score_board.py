from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 24, "italic")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.high_score = self.high_score
        self.goto(-210, 260)
        self.hideturtle()
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                 file.write(f"{self.high_score}")
        # self.score = 0
        # self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0 , 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
