"""
Solve the provided ordinary differential equation (ODE) with the Euler method
https://en.wikipedia.org/wiki/Euler_method

I you don't know how to do the Euler method, you can try solve it another way.

Solve for times 0 to 100 using the initial conditions provided.
Plot the result using matplotlib and save it to a file called part_5.png

The equation to be solved is defined by the function `get_derivatives`.
"""
import numpy as np
import matplotlib.pyplot as plt

# Initial conditions for [S, I, R]
INITIAL_CONDITIONS = np.array([1e4, 200, 0])
MAX_TIME = 100
STEP_SIZE = 0.1
NUM_STEPS = int(MAX_TIME / STEP_SIZE)

def get_derivatives(values, time):
    """
    Returns the derivative of the ODE as an array: [dS/dt, dI/dt, dR/dt]
    Use these derivatives to find the future values of [S, I, R]
    """
    total_population = values.sum()
    susceptible, infected = values[0], values[1]
    contact_rate = 0.3 if time < 20 else 0.05
    infection_rate = contact_rate * susceptible * infected / total_population
    recovery_rate = 0.1 * infected
    return np.array([
        -infection_rate,
        infection_rate - recovery_rate,
        recovery_rate,
    ])


times = np.linspace(start=0, stop=MAX_TIME, num=NUM_STEPS)
results = np.zeros((NUM_STEPS, 3))
results[0] = INITIAL_CONDITIONS

for t_idx, t in enumerate(times):
    if t_idx == 0:
        continue

    # Solve the equation here, filling out `results`

# Plot the results as a function of time for S, I, R respectively
