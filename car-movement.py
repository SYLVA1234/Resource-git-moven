class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.position = 0
    
    def start(self):
        print(f"The {self.make} {self.model} is starting.")
    
    def drive(self, distance):
        self.position += distance
        print(f"The {self.make} {self.model} is driving {distance} units.")
    
    def stop(self):
        print(f"The {self.make} {self.model} has stopped at position {self.position}.")

# Create a car object
my_car = Car("Toyota", "Corolla")

# Simulate the car's movement
my_car.start()
my_car.drive(10)
my_car.drive(20)
my_car.stop()
