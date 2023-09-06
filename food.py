from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.new_x = random.randint(-280, 282)
        self.new_y = random.randint(-282 , 282)
        self.goto(self.new_x, self.new_y)

        