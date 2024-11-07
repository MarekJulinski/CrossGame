from turtle import *
import random
from crossCar import Car

class World:
    
    def __init__(self, bottom_spawn = -100, top_spawn = 100, lines = 2, cars_per_line_min = 1, cars_per_line_max = 2, car_speed_min = 1, car_speed_max = 4) -> None:
        
        self.bottom_spawn = bottom_spawn
        self.top_spawn = top_spawn
        self.lines = lines
        
        self.cars = []
        
        self.car_speed_min = car_speed_min
        self.car_speed_max = car_speed_max + 1
        
        self.cars_per_line_min = cars_per_line_min
        self.cars_per_line_max = cars_per_line_max
        
    def start_level(self):
        
        self.car_lines_y = self.make_car_lines()
        
        self.car_lines_y = self.populate_world()
            
        self.cars, self.line_cars = self.spawn_cars()
        
        
    def make_car_lines(self):
        amount = (self.top_spawn - self.bottom_spawn) / self.lines
        
        lines = []
        
        for i in range(self.bottom_spawn, self.top_spawn, int(amount)+1):
            lines.append(i)
            
        return lines
        
    def populate_world(self):
        car_lines_y = {}
        
        spawn_point = [-400, 400]
        
        for line in self.car_lines_y:
            data = []
            point = spawn_point[random.randrange(len(spawn_point))]
            direction = point / -(abs(point))
            speed = random.randrange(self.car_speed_min, self.car_speed_max)
            amount_cars = random.randrange(self.cars_per_line_min, self.cars_per_line_max)
            data.append(direction)
            data.append(point)
            data.append(speed)
            data.append(amount_cars)
            
            car_lines_y[line] = data
            
        return car_lines_y
    
    def spawn_cars(self):
        line_cars = {}
        cars = []
        
        for line in self.car_lines_y:
            car = Car(direction=self.car_lines_y[line][0], pos=(self.car_lines_y[line][1], line), speed=self.car_lines_y[line][2])
            cars.append(car)
            cars_line = []
            cars_line.append(car)
            line_cars[line] = cars_line
            
        return cars, line_cars
    
    def move_cars(self):
        
        for car in self.cars:
            car.move()
            
    def populate_line(self):
        
        for line in self.line_cars:
            
            if len(self.line_cars[line]) < self.car_lines_y[line][-1]:
            
                spawning_point = int(800 / self.car_lines_y[line][-1])
                
                starting_point = self.car_lines_y[line][1]
                
                if starting_point > 0:
                    
                    spawning_point *= -1
                    closest_car = self.line_cars[line][0].body.xcor()
                    
                    for car in self.line_cars[line]:
                        if car.body.xcor() > closest_car:
                            closest_car = car.body.xcor()
                        
                    if closest_car < starting_point + spawning_point - self.car_speed_max:
                        new_car = Car(direction=self.car_lines_y[line][0], pos=(self.car_lines_y[line][1], line), speed=self.car_lines_y[line][2])
                        self.line_cars[line].append(new_car)
                        self.cars.append(new_car)
                        break
                        
                elif starting_point < 0:
                    
                    closest_car = self.line_cars[line][0].body.xcor()
                    
                    for car in self.line_cars[line]:
                        if car.body.xcor() < closest_car:
                            closest_car = car.body.xcor()
                        
                    if closest_car > starting_point + spawning_point + self.car_speed_max:
                        new_car = Car(direction=self.car_lines_y[line][0], pos=(self.car_lines_y[line][1], line), speed=self.car_lines_y[line][2])
                        self.line_cars[line].append(new_car)
                        self.cars.append(new_car)
                        break