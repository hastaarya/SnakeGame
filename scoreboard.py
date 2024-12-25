from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
            self.high_score = data.read()
            if self.high_score == '':
                self.high_score = 0
            else:
                self.high_score = int(self.high_score)          
        self.color("white") #change color to white 
        self.hideturtle() #hide the arrow at the start of the game
        self.penup() #hide the line 
        self.goto(0,270) #set coordinate to top-center

    def update_scoreboard(self): #writing texts to the screen
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self): #increase score and update the screen by clearing the screen and writing a new one
        self.score+=1        
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score      
            with open("score.txt",mode="w") as data:
                data.write(f"{self.high_score}")  
        self.score = 0
        self.update_scoreboard()

    
