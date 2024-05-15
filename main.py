"""
Code to run some experiments.
"""

from simulator import *

from lanes.OneLane import OneLane
from agents.OneLaneCar import OneLaneCar

import numpy as np

def test_normal():

    # ----
    # For one lane of safe drivers. No noise. Displays phantom jams.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    lane = OneLane(length=1000, n_cars=[50], car_types=["safe"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=1, min_acc=-4, extra_name=" - safe cars")

    simulate_lane(lane, steps=200, dt=0.2, width=900, height=100, frame_rate=60*60)
    # ----

    # ----
    # For one lane of risky drivers. No noise. Displays good traffic flux.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    lane = OneLane(length=1000, n_cars=[50], car_types=["smart"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=1, min_acc=-4, extra_name = " - risky cars")

    simulate_lane(lane, steps=200, dt=0.2, width=900, height=100, frame_rate=60*60)
    # ----

def test_noise():
    # ----
    # For one lane of safe drivers. With no noise. Displays fluid traffic.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    lane = OneLane(length=1000, n_cars=[35], car_types=["safe"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=1, min_acc=-4, 
                extra_name=" - safe cars (no noise)", noise = False)

    simulate_lane(lane, steps=200, dt=0.2, width=900, height=100, frame_rate=60*60)
    # ----

    # ----
    # For one lane of safe drivers. With writting noise. Displays fluid traffic.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    noise = {
        "write": {"prob": 0.05, "brake_prob": 0., "mag": 0.3},
        "read": False
    }
    lane = OneLane(length=1000, n_cars=[35], car_types=["safe"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=1, min_acc=-4, 
                extra_name=" - safe cars (writting noise)", noise = noise)

    simulate_lane(lane, steps=200, dt=0.2, width=900, height=100, frame_rate=60*60)
    # ----

     # ----
    # For one lane of safe drivers. With random brakes. Displays phantom jams.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    noise = {
        "write": {"prob": 0.0, "brake_prob": 0.02, "mag": 0.},
        "read": False
    }
    lane = OneLane(length=1000, n_cars=[35], car_types=["safe"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=1, min_acc=-4, 
                extra_name=" - safe cars (random brakes)", noise = noise)

    simulate_lane(lane, steps=200, dt=0.2, width=900, height=100, frame_rate=60*60)
    # ----

def test_noise_smart():
    # ----
    # For one lane of safe drivers. With no noise. Displays fluid traffic.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    lane = OneLane(length=1000, n_cars=[35], car_types=["smart"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=1, min_acc=-4, 
                extra_name=" - smart cars (no noise)", noise = False)

    simulate_lane(lane, steps=200, dt=0.2, width=900, height=100, frame_rate=60*60)
    # ----

    # ----
    # For one lane of safe drivers. With writting noise. Displays fluid traffic.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    noise = {
        "write": {"prob": 0.05, "brake_prob": 0., "mag": 0.3},
        "read": False
    }
    lane = OneLane(length=1000, n_cars=[35], car_types=["smart"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=1, min_acc=-4, 
                extra_name=" - smart cars (writting noise)", noise = noise)

    simulate_lane(lane, steps=200, dt=0.2, width=900, height=100, frame_rate=60*60)
    # ----

     # ----
    # For one lane of safe drivers. With random brakes. Displays phantom jams that are quickly disperssed but with accidents.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    noise = {
        "write": {"prob": 0.0, "brake_prob": 0.02, "mag": 0.},
        "read": False
    }
    lane = OneLane(length=1000, n_cars=[35], car_types=["smart"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=1, min_acc=-4, 
                extra_name=" - smart cars (random brakes)", noise = noise)

    simulate_lane(lane, steps=200, dt=0.2, width=900, height=100, frame_rate=60*60)
    # ----

def test_risky():
    # ----
    # For one lane of risky drivers. No noise. Displays very good traffic flux.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    lane = OneLane(length=1000, n_cars=[70], car_types=["smart"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 15, max_acc=3, min_acc=-12, extra_name = " - risky cars")

    simulate_lane(lane, steps=200, dt=0.5, width=900, height=100, frame_rate=120)
    # ----

    # ----
    # For one lane of risky drivers. No noise. Displays very good traffic flux.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    lane = OneLane(length=1000, n_cars=[70], car_types=["risky"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 15, max_acc=3, min_acc=-12, extra_name = " - risky cars")

    simulate_lane(lane, steps=200, dt=0.5, width=900, height=100, frame_rate=120)
    # ----

    # ----
    # For one lane of risky drivers. With noise only for distance. Displays some accidents and jams.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    noise = {
        "write": False,
        "read": {"prob": 0.03, "mag": 3, "sp_mag": 0}
    }
    lane = OneLane(length=1000, n_cars=[70], car_types=["risky"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=3, min_acc=-12, 
                extra_name = " - risky cars", noise=noise)

    simulate_lane(lane, steps=200, dt=0.5, width=900, height=100, frame_rate=120)
    # ----

    # ----
    # For one lane of risky drivers. With noise for distance and speed. Displays some accidents and jams.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    noise = {
        "write": False,
        "read": {"prob": 0.03, "mag": 2, "sp_mag": 2}
    }
    lane = OneLane(length=1000, n_cars=[70], car_types=["risky"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=3, min_acc=-12, 
                extra_name = " - risky cars", noise = noise)

    simulate_lane(lane, steps=200, dt=0.5, width=900, height=100, frame_rate=120)
    # ----

def test_mixed():
    # ----
    # For one lane of mixed drivers. No noise.
    # The max speed is a  bit less than the safe_dist, and the accident dist is about 1/3 of safe_dist.
    lane = OneLane(length=1000, n_cars=[20, 25, 25], car_types=["smart", "risky", "safe"], car_constructor=OneLaneCar,
                safe_dist = 10, accident_dist = 3, max_speed = 9, max_acc=3, min_acc=-12, extra_name = " - mixed cars")

    simulate_lane(lane, steps=200, dt=0.5, width=1200, height=100, frame_rate=120)
    # ----

# test_normal()
# test_noise()
# test_noise_smart()
# test_risky()
# test_mixed()

"""
# ----
# One lane of smart cars. This is enough cars so that there will be phantom jams without the need of noise.
lane = OneLane(length=700, n_cars=[50], car_types=["safe"], car_constructor=OneLaneCar,
            safe_dist = 10, accident_dist = 3, max_speed = 6, max_acc=0.5, min_acc=-4, extra_name = " - smart cars")

simulate_lane(lane, steps=200, dt=1, width=900, height=100, frame_rate=120)
# ----

# ----
# One lane of smart cars. This is enough cars so that there will be phantom jams without the need of noise.
lane = OneLane(length=700, n_cars=[50], car_types=["smart"], car_constructor=OneLaneCar,
            safe_dist = 10, accident_dist = 3, max_speed = 6, max_acc=0.5, min_acc=-4, extra_name = " - smart cars")

simulate_lane(lane, steps=200, dt=1, width=900, height=100, frame_rate=120)
# ----

# ----
lane = OneLane(length=700, n_cars=[50], car_types=["risky"], car_constructor=OneLaneCar,
            safe_dist = 10, accident_dist = 3, max_speed = 6, max_acc=0.5, min_acc=-4, extra_name = " - risky cars")

simulate_lane(lane, steps=200, dt=1, width=900, height=100, frame_rate=120)
# ----


lane = OneLane(length=1000, n_cars=[30, 20, 10], car_types=["smart", "risky", "safe"], car_constructor=OneLaneCar,
            safe_dist = 10, accident_dist = 3, max_speed = 6, max_acc=0.5, min_acc=-4, extra_name = " - smart cars")

simulate_lane(lane, steps=200, dt=1, width=900, height=100, frame_rate=120)

# Phantom jams
plot_positions(100, 1, lane)
plot_average_speed(100, 1, lane)

"""
lane = OneLane(length=700, n_cars=[60], car_types=["risky"], car_constructor=OneLaneCar,
            safe_dist = 10, accident_dist = 3, max_speed = 6, max_acc=0.5, min_acc=-4, extra_name = " - risky cars")

max_speeds = [3 + i/20*20 for i in range(20)]
fluxes = np.zeros((len(max_speeds),))
accidents = np.zeros((len(max_speeds),))
for i, sp in enumerate(max_speeds):
    
    # Set all cars max speed to sp
    for car in lane.cars:
        car.max_speed = sp
    
    # Simulate lane
    flux, accs = flux_and_accidents(500, 1, lane)

    print("Flux and accidents for speed: ", sp, flux, accs)
    fluxes[i] = flux
    accidents[i] = accs

plt.plot(max_speeds, fluxes)
plt.title("Flux")
plt.show()
