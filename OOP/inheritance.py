#parent class vehicle
class Vehicle :
    def __init__(self , brand , speed):
        self.brand = brand
        self.speed = speed
    def show_info(self):
        print(f"Brand : {self.brand}")
        print(f"Speed : {self.speed}")
    def move(self):
        print("Vehicle is moving.")

# now creating child class
class Car(Vehicle):
    def __init__(self , brand , speed, num_doors):
        super().__init__(brand , speed)
        self.num_doors = num_doors

