from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.Rightscore=0
        self.Leftscore=0
        self.color("blue")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"RightScore :{self.Rightscore}  and LeftScore :{self.Leftscore}",align="center",font=("Arial",20,"normal"))

    def increment_rscore(self):
        self.Rightscore+=1
        self.clear()
        self.write(f"RightScore :{self.Rightscore}  and LeftScore :{self.Leftscore}", align="center",
                   font=("Arial", 20, "normal"))

    def increment_lscore(self):
        self.Leftscore+=1
        self.clear()

        self.write(f"RightScore :{self.Rightscore}  and LeftScore :{self.Leftscore}", align="center",
               font=("Arial", 20, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))



