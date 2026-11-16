# 3-Body Gravity Assist Simulator
## What my code actually is:
My code is a simulator which helps to get a graph and understand the gravity assist concept. It is a 3-body system simulation that checks how a spacecraft's trajectory changes under the influence of the Sun's and the planet's gravity.

## Project Overview
When a spacecraft travels through a solar system, it can use the gravitational fields of planets to change its velocity and trajectory. This technique is called gravity assist. It allows the spacecraft to gain or lose energy without relying on onboard propulsion.

The goal of my project is to build a simplified, 2-Dimensional, three-body simulation that shows the physics behind gravity assists and  how the spacecraft's path changes due to the effect of gravity. I have taken Jupiter as my primary example, but there are options for other planets in my code as well.

## Objectives

### 1. Modelling gravitational interactions
To simulate the gravitational acceleration acting on the spacecraft due to the planet and the sun and understand how the sum of these accelerations would affect the spacecraft's trajectory.

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

The acceleration of the planet is calculated using:

$$
\vec{a}p = -\frac{GM_{\text{sun}}\vec{r}_p}{|\vec{r}_p|^3}
$$

Where:
- $G$ = Universal gravitational constant
- $M_{\text{sun}}$ = Mass of the Sun
- $\vec{r}_p$ = Position vector of the planet relative to the sun
- $\vec{a}_p$ = Acceleration of the planet

## 2. Motion of the Spacecraft

The spacecraft experiences gravitational acceleration due to both the Sun and the selected planet.

The total acceleration is calculated by adding both the accelerations:

$$
\vec{a}{\text{total}} = \vec{a}{\text{sun}} + \vec{a}{\text{planet}}
$$

These gravitational interactions determine the change in the spacecraft's velocity throughout the simulation.

## Assumptions and Limitations

To make the simulation manageable, I made a few assumptions to simplify my code:

- The Sun is assumed to remain stationary at the origin.
- The simulation is 2 - dimensional only.
- The planet is influenced only by the Sun's gravity while the spacecraft in influenced by only the Sun's gravity and the planet's gravity.
- There are no other forces acting on the spacecraft other than the above mentioned forces.
- The initial positions and velocities are simplified approximations of planetary motion.

## Technologies Used

- Python: My main programming language
- NumPy: I used this module for mathematical operations and handling data efficiently
- SciPy: I used this module for numerical integration using solve_ivp()
- Matplotlib: I used this module to plot the trajectories of the planet and the spacecraft

## Requirements and Setup

Thbe project requires Python 3.x and the following libraries:
- NumPy
- SciPy
- Matplotlib

## Example Usage and Sample Output

My program asks the user to choose one of the available planets and enter the nicoming spacecraft's velocity. It then caslculates the initial conditions, simulates the motion of the planet and spacecraft. and displays a graph showing their trajectories.

### Sample Output


## What I Learnt
Working on this code helped me integrate core concepts from Physics and Maths with Computer Science. I understood how gravitational ineractions work, about position and velocity vectors in Python, how differential equations help us plot the motion of celstial bodies and how to use different modules such as SciPy, NumPy and Matplotlib. Most importantly, this project gave me an opportunity to explore how a real spacecraft technique can be represented through a simplified mathematical model.