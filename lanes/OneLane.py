"""
A simple class to model a one lane road
"""
import numpy as np
import random

class OneLane:

    def __init__(self, length, n_cars, car_types, car_constructor, safe_dist=1, accident_dist=0.5, 
                 max_speed = 1, max_acc = 1, min_acc = -1, extra_name = "", noise = False):
        
        self.name = "One lane" + extra_name
        self.length = length
        self.noise = noise

        self.cars = []

        self.total_cars = sum(n_cars)
        car_index = 0

        for i in range(len(n_cars)):
            for j in range(n_cars[i]):

                # Create a new car of the type
                car = car_constructor(max_speed = max_speed, max_acc = max_acc, 
                                      min_acc = min_acc, safe_dist = safe_dist, 
                                      accident_dist = accident_dist, mode = car_types[i])

                # Add car to list of cars
                self.cars.append(car)
                car_index += 1

        # Shuffle cars
        random.shuffle(self.cars)

        for i in range(self.total_cars):
            # Random position for the car
            rand_pos = np.random.rand()*self.length/self.total_cars + i/self.total_cars * self.length

            # Set the position and initial speed for the car.
            self.cars[i].start(rand_pos, 0)


    def get_positions(self):
        positions = np.zeros((self.total_cars, ))

        for i in range(self.total_cars):
            positions[i] = self.cars[i].pos
        
        return positions

    def step(self, dt):
        positions = np.zeros((self.total_cars, ))
        speeds = np.zeros((self.total_cars, ))
        n_accidents, flux = 0, 0

        # Simulate
        for i in range(self.total_cars):
            
            front_car = self.cars[(i+1) % self.total_cars]
            back_car = self.cars[(i-1) % self.total_cars]

            positions[i], speeds[i], accident, looped = self.cars[i].step(dt, self.length, front_car, back_car, self.noise)
            
            if (accident):
                n_accidents += 1
            if (looped):
                flux += 1
        
        # Assign new positions and speeds
        for i in range(self.total_cars):
            self.cars[i].pos = positions[i]
            self.cars[i].speed = speeds[i]

        return positions, speeds, n_accidents, flux

