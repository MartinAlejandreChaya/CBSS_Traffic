"""
Code to simulate lanes of traffic
"""

from graphics import *
import numpy as np
from matplotlib import pyplot as plt
import time

# Animation and n_accidents and total_flux
def simulate_lane(lane, steps, dt, width, height, frame_rate):

    # Create window
    win = GraphWin(lane.name, width, height)

    if (frame_rate != False):
        frame_time = 1/frame_rate

    width_transform = width / lane.length
    height_mid = height/2

    # Create a circle for each car
    circles = []
    for i in range(lane.total_cars):
        # Create circle at car position
        circ = Circle(Point(lane.cars[i].pos * width_transform, height_mid), 5)
        circ.setFill(color_rgb(*lane.cars[i].get_color()))

        # Draw circle
        circ.draw(win)
        circles.append(circ)

    total_flux = 0
    total_accidents = 0
    for i in range(steps):
        # Get the ammount moved by each car
        positions, speeds, n_accidents, flux = lane.step(dt)
        
        # Redraw all car circles
        for j in range(lane.total_cars):
            dx = positions[j] * width_transform - circles[j].getCenter().getX()
            circles[j].move(dx, 0)

        total_flux += flux
        total_accidents += n_accidents

        if (frame_rate != False):
            time.sleep(frame_time)

    print("\nLane: ", lane.name)
    print("Total flux: ", total_flux)
    print("Total accidents: ", total_accidents)

    print("\nFlux / time: ", total_flux / (steps * dt))
    print("\nAccidents / time: ", total_accidents / (steps * dt))

    win.close()    # Close window when done


# phantom jams y todo eso
def plot_positions(steps, dt, lane, linewidth = 2):

    t = 0
    prev_positions = lane.get_positions()

    for i in range(steps):

        t += dt

        # Get the ammount moved by each car
        positions, speeds, n_accidents, flux = lane.step(dt)

        # Draw a line for consecutive positions of the cars.
        for j in range(lane.total_cars):
            # Skip cars that loop
            if (positions[j] < prev_positions[j]):
                continue
            # Plot line for rest of the cars
            plt.plot([prev_positions[j], positions[j]], [t-dt, t], 'black', linewidth=linewidth)
        
        prev_positions = positions


    plt.show()


# X axis: time, Y axis: all car's average speed
def plot_average_speed(steps, dt, lane):
    
    avg_speeds = np.zeros((steps, ))

    for i in range(steps):
        # Get the ammount moved by each car
        positions, speeds, n_accidents, flux = lane.step(dt)

        # Save average speed
        avg_speeds[i] = np.mean(speeds)
        

    plt.plot(avg_speeds)
    plt.show()

# For one simulation of one lane, the number of accidents and total flux.
def flux_and_accidents(steps, dt, lane):

    total_flux, total_accidents = 0, 0

    for i in range(steps):
        # Get the ammount moved by each car
        positions, speeds, n_accidents, flux = lane.step(dt)

        total_accidents += n_accidents
        total_flux += flux


    return total_flux, total_accidents, total_flux / (steps*dt), total_accidents / (steps * dt)


def noises_flux(steps, dt, lane, noises):

    fluxes = np.zeros((len(noises), ))
    accidents = np.zeros((len(noises), ))

    # For each of the noises
    for n in range(len(noises)):
        lane.noise = noises[n]
        # Run the simulation and compute the flux and accidents.
        total_flux, total_accidents = 0, 0
        for i in range(steps):
            # Get the ammount moved by each car
            positions, speeds, n_accidents, flux = lane.step(dt)

            total_accidents += n_accidents
            total_flux += flux
        
        fluxes[n] = total_flux / (steps * dt)
        accidents[n] = total_accidents / (steps * dt)

    return fluxes, accidents