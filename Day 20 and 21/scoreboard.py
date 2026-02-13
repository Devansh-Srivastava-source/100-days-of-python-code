from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read()) #because it returns in a string.
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}|Highscore: {self.highscore}",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGNMENT,font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_score()