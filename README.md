# 3-Body Gravity Assist Simulator
## What the code actually is:
It is a Python-based physics simulation that explores how gravitational interactions between heavenly bodies and a spacecraft can change the spacecraft's trajectory and velocity using a gravity assist manoeuvre


## Project Overview
When a spacecraft travels through a solar system, it can use the gravitational fields of planets to change its velocity and trajectory. This technique is called gravity assist or gravitational slingshot. It allows the spacecraft to gain or lose energy without relying on onboard propulsion.

The goal of my project is to build a simplified, 2-Dimensional, three-body simulation that shows the physics behind gravity assists. I have taken Jupiter as my primary example, but there are options for other planets in my code as well.

## Objectives

### 1. Modelling gravitational interactions
To simulate the gravitational acceleration acting on the spacecraft due the planet and the sun and understanding how sum of these accelerations would affect the spacecraft's trajectory. 

### 2. Simulating spacecraft trajectories
To use the solve_ivp function from the SciPy library to calculate how the positions and velocities of the simulated bodies change over time.

### 3. Visualising the simulation
To use the matplotlib library, to plot the simulated trajecoty of the spacecraft and to analyze its motion and understand the effects of gravity.