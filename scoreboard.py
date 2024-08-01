from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
           super().__init__()
           self.score = 0
           self.color("white")
           self.penup()
           self.goto(0, 250)
           self.hideturtle()
           self.high_score = 0
#self.write(f"Score: {self.score} High Score: {self.high_score}", font=("courier", 25, "bold"), align="center")



    def update_score(self):
           self.write(f"Score: {self.score} High Score: {self.high_score}", font=("courier", 25, "bold"), align="center")


    def add_score(self):
           self.update_score()
           self.clear()
           self.score += 1
           if self.score >= self.high_score:
                self.high_score = self.score


    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #     self.write(f"GAME OVER: {self.score} High Score: {self.high_score}", font=("courier", 25, "bold"), align="center")
