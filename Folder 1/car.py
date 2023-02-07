class Car:
    def __init__(self, current_speed, max_speed):
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.fuel_level = 0
    
    def accelerate(self):
        self.current_speed += 1
        self.fuel_level -= 1
        
    def brake(self):
        self.current_speed -= 1
        
    def refuel(self):
        self.fuel_level += 1
        