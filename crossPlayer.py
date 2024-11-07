from turtle import Turtle
import time
class Player:
    
    lives = 3
    
    start_cor = (0, -325)
    
    size = 1.3
    shape = 'square'
    color = 'grey'
    speed = 4
    up = False
    down = False
    left = False
    right = False
    
    def __init__(self):
        self.body = Turtle()
    
    def set_up_body(self):
        self.lives = 3
        self.body.penup()
        self.body.shape(self.shape)
        self.body.color(self.color)
        self.body.shapesize(1.3, 1.3)
        self.body.setpos(self.start_cor)
    
    def move(self):
        if self.up:
            self.body.sety(self.body.ycor() + self.speed)
        elif self.down:
            self.body.sety(self.body.ycor() - self.speed)
        elif self.left:
            self.body.setx(self.body.xcor() - self.speed)
        elif self.right:
            self.body.setx(self.body.xcor() + self.speed)
    
    def move_up(self):
        self.up = True
        self.down = False
        self.left = False
        self.right = False
        
    def stop_up(self):
        self.up = False
        
    def move_down(self):
        self.up = False
        self.down = True
        self.left = False
        self.right = False
        
    def stop_down(self):
        self.down = False
        
    def move_left(self):
        self.up = False
        self.down = False
        self.left = True
        self.right = False
        
    def stop_left(self):
        self.left = False
        
    def move_right(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = True
        
    def stop_right(self):
        self.right = False
        
    def check_colision(self, cars):
        
        for car in cars:
            if self.body.distance(car.body) < 55:
                if self.body.ycor() < car.body.ycor() + 25 and self.body.ycor() > car.body.ycor() - 25:
                    self.lives -= 1
                        
                    if self.lives > 0:
                        self.respawn()
                    
                    
    def respawn(self):
        self.body.setpos(self.start_cor)
        time.sleep(1)                    
    