"""
Modelling a driving agent in a 1-lane continuous road.

The agent actions are either to accelerate or deccelerate.
The agent only sees the cars directly in front and behind him.
    * In particular the agent knows the distance to them
    * And their speed

We will assume that all drivers want to accelerate to the maximum speed all the time.
"""
import numpy as np

# Dumb drivers don't take into account the speed of the car's in front of them.
class OneLaneCar:

    # Create a new dumb driver. 
    def __init__(self, extra_name = "", max_acc = 1, min_acc = -1, max_speed = 1, safe_dist = 1, 
                 mode="safe", accident_dist = 0.5):
        
        self.name = "Dumb" + extra_name

        # Limit the max acceleration and decceleration of the car
        self.max_acc = max_acc
        self.min_acc = min_acc

        # Limit the max velocity of the car (the min velocity is 0)
        self.max_speed = max_speed

        # Set a distance that will be considered to be far enough away from other cars.
        self.safe_dist = safe_dist
        self.accident_dist = accident_dist

        # The mode indicates how risky the driver is
        self.mode = mode
    
    # Place the car into the road
    def start(self, pos, speed):
        self.pos = pos
        self.speed = speed
        self.acc = 0
    

    # Simulate a time step. Returns the new position of the car and a flag indicating if there was an accident.

    #   The dumb driver will actually ignore the car behind him and only address the one in front.
    #   The dumb driver will try to keep at safe distance from the driver in front.
    #   The dumb driver however doesn't take into account the speed of the car for it's calculations.

    #   The risky driver will behave in a similar way to the dumb driver but he will take into account
    #   the front_car speed to brake.
    def step(self, dt, length, front_car, back_car = False, noise = False):
        
        # Compute the distance between the cars
        dist = front_car.pos - self.pos
        if (dist < 0): # The last car to the first car
            dist = length - self.pos + front_car.pos
        
        # If it is less than the accident distance, record an accident and brake completely
        if (dist < self.accident_dist):
            self.speed = 0
            return self.pos, True, False
        
        # Introduce noise in to the reading
        if (noise and noise["read"]):
            if (np.random.rand() < noise["read"]["prob"]):
                dist += (np.random.rand()*2-1) * noise["read"]["mag"]

        # Compute what would happen if the front car didn't move.
        next_dist = dist - self.speed * dt

        # If the distance is going to be less than the safe distance full brake.
        if (next_dist < self.safe_dist):

            # Dumb mode
            if (self.mode == "safe"):
                self.acc = self.min_acc
            elif (self.mode == "smart"):
                # This would be the code for a smarter car, that just brakes enough not to collide
                # Deccelerate
                    # dist - speed * dt = safe_dist --> speed = (dist - safe_dist)/dt
                    # new_speed  = speed + acc*dt  --> acc =  -speed/dt 
                target_speed = (dist - self.safe_dist) / dt
                target_acc = (target_speed - self.speed)/dt

                # Limit acceleration 
                self.acc = max(min(target_acc, self.max_acc), self.min_acc)

        # Otherwise, accelerate to the maximum
        else:
            self.acc = self.max_acc

        
        # introduce noise into the writting
        if (noise and noise["write"]):
            # Randomly brake completely
            if (np.random.rand() < noise["write"]["brake_prob"]):
                self.acc = self.min_acc
            # Otherwise, random fluctuations
            elif (np.random.rand() < noise["write"]["prob"]):
                self.acc += (np.random.rand()*2-1) * noise["write"]["mag"]
        
        # update speed
        self.speed = self.speed + self.acc
        # limit speed
        self.speed = max(min(self.speed, self.max_speed), 0)

        # Update position
        self.pos = self.pos + self.speed
        # If we surpassed the length of the lane, loop back to the beggining
        looped = self.pos > length
        if (looped):
            self.pos -= length
        
        return self.pos, False, looped

