import time
from turtle import Turtle

class Time:
    
    def __init__(self) -> None:
        self.start_time = time.time()
        self.body = Turtle()
        self.body.hideturtle()
        self.body.penup()
        self.body.color('grey')
        self.body.setpos(200, 315)
        
    def since_start(self):
        
        zero = '0'
        
        milliseconds = time.time() - self.start_time
        
        milliseconds = int(milliseconds * 1000)
        
        if milliseconds >= 60000:
            minutes = int(milliseconds / 60000)
            milliseconds %= 60000
        else:
            minutes = 0
        
        if milliseconds >= 1000:
            seconds = int(milliseconds / 1000)
            milliseconds %= 1000
        else:
            seconds = 0
            
        milliseconds = int(milliseconds/10)
        
        if minutes < 10:
            minutes = '0' + str(minutes)
            
        if seconds < 10:
            seconds = '0' + str(seconds)
        
        time_clock = f"{minutes}:{seconds}:{milliseconds}"
        
        return time_clock
        
    def write_time(self):
        self.body.clear()
        self.body.write(self.since_start(), False, align='center', font=('Arial', 20 , 'italic'))