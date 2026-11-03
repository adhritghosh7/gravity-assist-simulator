# 3-Body Gravity Assist Simulator
## What my code actually is:
My code is a simulator which helps to get a graph and understand the gravity assist concept. It is a 3-body system simulation that checks how a spacecraft's trajectory changes under the influence of the Sun's and the planet's gravity.

## Project Overview
When a spacecraft travels through a solar system, it can use the gravitational fields of planets to change its velocity and trajectory. This technique is called gravity assist. It allows the spacecraft to gain or lose energy without relying on onboard propulsion.

The goal of my project is to build a simplified, 2-Dimensional, three-body simulation that shows the physics behind gravity assists and shows how the spacesraft's path changes due to the effect of gravity. I have taken Jupiter as my primary example, but there are options for other planets in my code as well.

## Objectives

### 1. Modelling gravitational interactions
To simulate the gravitational acceleration acting on the spacecraft due the planet and the sun and understanding how sum of these accelerations would affect the spacecraft's trajectory.

### 2. Simulating spacecraft trajectories
To use the solve_ivp function from the SciPy library to help calculate how the positions and velocities of the simulated bodies change over time.

### 3. Visualising the simulation
To use the matplotlib library, to plot the simulated trajectory of the spacecraft and to analyze its motion and understand the effects of gravity.

## Features
- Planet Selection: Allows the user to select a planet from the Planets dictionary containing data about the planets.
- Gravitational Modelling: Calculates the gravitational acceleration acting on the spacecraft due to the Sun and the selected planet
- Initial Conditions: Defines the initial position and velocity of the celestial bodies and spacecraft for the simulation
- Numerical Integration: Uses SciPy's solve_ivp function to solve the equations of motion and calculate the state (positions and velocities) of the system over a certain period of time
- Trajectory Visualization: Uses Matplotlib to plot the simulated path of the spacecraft and visualize the trajectory with the Sun at the origin of the coordinate system.


## Physics Behind the Simulation

The main physics law that governs my project is Newton's Law of Universal Gravitation. This law describes gravity as a force: any particle attracts any other particle with a force proportional to the product of their masses and inversely proportional to the square of the distance between their centers of mass.

The equation for this law is:

$$
F = \frac{Gm_1m_2}{r^2}
$$

Where:
- $G$ = Universal gravitational constant
- $m_1, m_2$ = Masses of the two bodies
- $r$ = Distance between the centres of mass

## 1. Motion of the Planet

In the simulation, the Sun is kept stationary at the origin of my cartesian plane, while the selected is allowed to move under the gravity of the Sun.

