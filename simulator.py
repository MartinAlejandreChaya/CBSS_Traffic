"""
Code to simulate lanes of traffic
"""

from graphics import *
import time

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

    total_flux = 0
    total_accidents = 0
    input("Press enter to start animation")
    for i in range(steps):
        # Get the ammount moved by each car
        positions, n_accidents, flux = lane.step(dt + width_transform)
        
        # Redraw all car circles
        for j in range(lane.total_cars):
            dx = positions[j] * width_transform - circles[j].getCenter().getX()
            circles[j].move(dx, 0)

        total_flux += flux
        total_accidents += n_accidents

        time.sleep(frame_time)

    print("\nLane: ", lane.name)
    print("Total flux: ", total_flux)
    print("Total accidents: ", total_accidents)

    input("\nPress enter to close the window")
    win.close()    # Close window when done

