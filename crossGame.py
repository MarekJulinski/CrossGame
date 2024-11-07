from turtle import *
import time
from world import World
from crossPlayer import Player
from crossTime import Time



def create_screen():
    
    screen = Screen()
    screen.screensize(canvwidth=700, canvheight=700, bg='white')
    screen.tracer(0)
    
    return screen

def control_player(player, screen):
    screen.onkeypress(player.move_down, "s")
    screen.onkeypress(player.move_up, "w")
    screen.onkeypress(player.move_left, "a")
    screen.onkeypress(player.move_right, "d")
    
    screen.onkeyrelease(player.stop_down, 's')
    screen.onkeyrelease(player.stop_up, 'w')
    screen.onkeyrelease(player.stop_left, 'a')
    screen.onkeyrelease(player.stop_right, 'd')
    
    screen.listen()

def create_finish():
    finish = Turtle()
    return finish

def spawn_finish(finish):
    finish.penup()
    finish.shape('square')
    finish.shapesize(1.3, 1.3)
    finish.color('green')
    finish.sety(325)

def best_score():
    best_score = Turtle()
    best_score.hideturtle()
    best_score.penup()
    best_score.color('grey')
    best_score.setpos(-200, 315)
    with open('./Cross/highscore.txt', 'r') as f:
        score = f.readline()
        
    milliseconds = int(score)
        
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
        
    time_clock = f"Best Time: {minutes}:{seconds}:{milliseconds}"
    
    best_score.write(time_clock, False, align='center', font=('Arial', 20 , 'italic'))
    return best_score

if __name__ == "__main__":
    
    screen = create_screen()
    
    level_1 = World(bottom_spawn= 200, top_spawn= 350, lines= 2, cars_per_line_min=1, cars_per_line_max=2, car_speed_min=2, car_speed_max= 3)
    level_2 = World(bottom_spawn= 100, top_spawn= 350, lines= 3, cars_per_line_min=2, cars_per_line_max=3, car_speed_min=2, car_speed_max= 4)
    level_3 = World(bottom_spawn= 0, top_spawn= 300, lines= 4, cars_per_line_min=3, cars_per_line_max=4, car_speed_min=3, car_speed_max= 5)
    level_4 = World(bottom_spawn= -100, top_spawn= 350, lines= 5, cars_per_line_min=4, cars_per_line_max=5, car_speed_min=4, car_speed_max= 6)
    level_5 = World(bottom_spawn= -250, top_spawn= 400, lines= 6, cars_per_line_min=4, cars_per_line_max=5, car_speed_min=5, car_speed_max= 7)

    levels = [level_1, level_2, level_3, level_4, level_5]
    
    time_clock = Time()
    
    
    for level in levels:
        high_score = best_score()
        player = Player()
        player.set_up_body()
        control_player(player, screen)
        
        finish = create_finish()
        spawn_finish(finish)
        
        level.start_level()
        
        screen.update()
        
        game = True
        
        while game:
            time_clock.write_time()
            
            level.move_cars()
            
            level.populate_line()
            
            player.check_colision(level.cars)
            
            if player.lives <= 0:
                game = False
            
            player.move()
            
            screen.update()
            
            if player.body.distance(finish) < 25:
                win = True
                screen.clear()
                screen = create_screen()
                game = False
            
            time.sleep(0.01)
            
        if player.lives <= 0:
            win = False
            break
        
    if win:
        score = time.time() - time_clock.start_time
        
        score = int(score * 1000)
        
        with open('./Cross/highscore.txt', 'r') as f:
            best_time = int(f.readline())
            f.close()
            
        if score < best_time:
            with open('./Cross/highscore.txt', 'w') as f:
                f.write(str(score))
                f.close()
    
    screen.exitonclick()