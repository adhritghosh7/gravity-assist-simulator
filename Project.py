import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#Gravitational constant (Nm^2/kg^2)
G = 6.67430e-11

#Mass of the sun in kgs
M_sun = 1.989e30

#Astronomical unit in meters
AU = 1.496e11

#No of seconds in a day
Day_sec = 86400

#Planets Database -> [Mass (kg), Semi-major axis (m), Orbital speed (m/s)]
Planets = {
    'Earth':{'mass':5.972e24, 'a':1 * AU, 'v':29780},
    'Mars':{'mass':6.416e23, 'a':1.523 * AU, 'v':24070},
    'Jupiter':{'mass':1.898e27, 'a':5.2 * AU, 'v':13060}
}

print("Welcome to the Gravity Assist Simulation!")
print("The planets available are: ")
for i in Planets.keys():
    print(i)

#Configuring the simulation and displaying the properties of the chosen planet
t_planet = input("Enter the name of the planet you want to choose: ")

print("The mass of", t_planet, "is", Planets[t_planet]['mass'], "kg")
print("The semi-major axis of", t_planet, "is", Planets[t_planet]['a'], "m")
print("The orbital speed of", t_planet, "is", Planets[t_planet]['v'], "m/s")

#Defining the arrays for the position and the velocity vectors of the planet

#The sun is at the origin of the coordinate system (0,0)
#Initial position vector of planet
r_0 = np.array([Planets[t_planet]['a'],0.0])

#Initial velocity vector of planet
v_0 = np.array([0.0, Planets[t_planet]['v']])