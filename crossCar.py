from turtle import Turtle
import random


class Car:
    
    def __init__(self, direction = 0, pos = (0, 0), speed = 2):
        self.width = 4
        self.height = 1.3
        self.colors = ['red', 'yellow', 'purple', 'black']
        self.color = random.randint(0, len(self.colors)-1)
        
        self.start_pos_x = pos[0]
        self.body = Turtle()
        self.speed = speed
        self.body.penup()
        self.body.shape('square')
        self.body.shapesize(self.height, self.width)
        self.body.color(self.colors[self.color])
        self.direction = direction
        self.body.setposition(pos)
        
    def move(self):
        self.body.setposition(self.body.xcor() + self.speed * self.direction, self.body.ycor())
        self.spawn_back()
        
    def spawn_back(self):
        if self.start_pos_x > 0:
            if self.body.xcor() <= self.start_pos_x - 799 - self.speed/2:
                self.body.setx(self.start_pos_x)
        elif self.start_pos_x < 0:
            if self.body.xcor() >= self.start_pos_x + 799 + self.speed/2:
                self.body.setx(self.start_pos_x)