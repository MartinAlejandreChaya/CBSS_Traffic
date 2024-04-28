"""
Modelling a driving agent in a 1-lane continuous road.

The agent actions are either to accelerate or deccelerate.
The agent only sees the cars directly in front and behind him.
    * In particular the agent knows the distance to them
    * And their speed

We will assume that all drivers want to accelerate to the maximum speed all the time.
"""


# Dumb drivers don't take into account the speed of the car's in front of them.
class DumbOneLane:

    # Create a new dumb driver. 
    def __init__(self, extra_name = "", max_acc = 1, min_acc = -1, max_speed = 1, safe_dist = 1):
        self.name = "Dumb" + extra_name

        # Limit the max acceleration and decceleration of the car
        self.max_acc = max_acc
        self.min_acc = min_acc

        # Limit the max velocity of the car (the min velocity is 0)
        self.max_speed = max_speed

        # Set a distance that will be considered to be far enough away from other cars.
        self.safe_dist = safe_dist
    
    # Place the car into the road
    def start(self, pos, speed):
        self.pos = pos
        self.speed = speed
        self.acc = 0
    
    # Simulate a time step. The dumb driver will actually
    # ignore the car behind him and only address the one in front.
    # The dumb driver will try to keep at safe distance from the driver in front.
    # The dumb driver however doesn't take into account the speed of the car
    # for it's calculations.
    def step(self, dt, length, front_car, back_car = False):
        
        # Compute the distance between the cars
        dist = front_car.pos - self.pos
        if (dist < 0): # The last car to the first car
            dist = length - self.pos + front_car.pos

        # Compute what would happen if the front car didn't move.
        next_dist = dist - self.speed * dt

        # If the distance is going to be less than the safe distance full brake.
        if (next_dist < self.safe_dist):
            self.acc = self.min_acc
            """
            # This would be the code for a smarter car, that just brakes enough not to collide
            # Deccelerate
                # dist - speed * dt = safe_dist --> speed = (dist - safe_dist)/dt
                # new_speed  = speed + acc*dt  --> acc =  -speed/dt 
            target_speed = (dist - self.safe_dist) / dt
            target_acc = (target_speed - self.speed)/dt

            # Limit acceleration 
            self.acc = max(min(target_acc, self.max_acc), self.min_acc)
            """

        # Otherwise, accelerate to the maximum
        else:
            self.acc = self.max_acc
        
        # update speed
        self.speed = self.speed + self.acc
        # limit speed
        self.speed = max(min(self.speed, self.max_speed), 0)

        # Update position
        self.pos = self.pos + self.speed
        # Loop back to the beggining
        if (self.pos > length):
            self.pos -= length
        
        return self.pos

