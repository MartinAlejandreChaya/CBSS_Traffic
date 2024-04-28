"""
A simple class to model a one lane road
"""
import numpy as np

class OneLane:

    def __init__(self, length, n_cars, car_types, safe_dist=1, max_speed = 1, max_acc = 1, min_acc = -1):
        
        self.name = "One lane"
        self.length = length

        self.cars = []

        self.total_cars = sum(n_cars)
        car_index = 0

        for i in range(len(n_cars)):
            for j in range(n_cars[i]):

                # Create a new car of the type
                car = car_types[i](max_speed = max_speed, max_acc = max_acc, min_acc = min_acc, safe_dist = safe_dist)

                # Random position for the car
                rand_pos = np.random.rand()*self.length/self.total_cars + car_index/self.total_cars * self.length

                # Set the position and initial speed for the car.
                car.start(rand_pos, 0)

                # Add car to list of cars
                self.cars.append(car)
                car_index += 1
    

    def step(self, dt):
        positions = np.zeros((self.total_cars, ))

        for i in range(self.total_cars):
            front_car = self.cars[(i+1) % self.total_cars]
            back_car = self.cars[(i-1) % self.total_cars]
            positions[i] = self.cars[i].step(dt, self.length, front_car, back_car)

        return positions
    
    def show(self):

        print("One lane of dumb cars")
        for i in range(self.total_cars):
            print(i, self.cars[i].pos, self.cars[i].speed)
