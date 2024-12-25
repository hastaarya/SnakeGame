import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self): #setup food shape,color
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self): #create random food with random class
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)