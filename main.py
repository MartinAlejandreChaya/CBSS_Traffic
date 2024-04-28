from graphics import *
import time

from lanes.OneLane import OneLane
from agents.DumbOneLane import DumbOneLane

import numpy as np

def simulate_lane(lane, steps, dt, width, height, frame_rate):

    # Create window
    win = GraphWin(lane.name, width, height)

    frame_time = 60/frame_rate

    width_transform = width / lane.length
    height_mid = height/2

    # Create a circle for each car
    circles = []
    for i in range(lane.total_cars):
        # Create circle at car position
        circ = Circle(Point(lane.cars[i].pos * width_transform, height_mid), 5)
        circ.setFill(color_rgb(51, 51, 51))

        # Draw circle
        circ.draw(win)
        circles.append(circ)

    input("Press enter to start animation")
    for i in range(steps):
        # Get the ammount moved by each car
        positions = lane.step(dt + width_transform)
        
        # Redraw all car circles
        for j in range(lane.total_cars):
            dx = positions[j] * width_transform - circles[j].getCenter().getX()
            circles[j].move(dx, 0)

        time.sleep(frame_time)

    input("Press enter to close the window")
    win.close()    # Close window when done




lane = OneLane(length=900, n_cars=[30], car_types=[DumbOneLane], 
               safe_dist = 5, max_speed = 8, max_acc=1, min_acc=-3)

simulate_lane(lane, steps=100, dt=1, width=900, height=100, frame_rate=60*10)

lane = OneLane(length=900, n_cars=[40], car_types=[DumbOneLane], 
               safe_dist = 5, max_speed = 10, max_acc=1, min_acc=-3)

simulate_lane(lane, steps=100, dt=1, width=900, height=100, frame_rate=60*10)