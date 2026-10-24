import numpy as np
import scipy as sp
from scipy.integrate import sove_ivp
import matplotlib.pyplot as plt

#Gravitational constant (Nm^2/kg^2)
G = 6.67430e-11

#Mass of the sun in kgs
M_sun = 1.989e30

#Astronomical unit in meters
AU = 1.496e11

#No of seconds in a day
Day_sec = 86400

#Planets Database -> [Mass (kg), Semi-major axis (m), Orbital speed (m/s), Radius (m)]
Planets = {
    'Earth':{'mass':5.972e24, 'a':1 * AU, 'v':29780,'r':6371000},
    'Mars':{'mass':6.416e23, 'a':1.523 * AU, 'v':24070,'r':3390000},
    'Jupiter':{'mass':1.898e27, 'a':5.2 * AU, 'v':13060,'r':69911000}
}

print("Welcome to the Gravity Assist Simulation!")
print("The planets available are: ")

k = list(Planets.keys())
for j in range(len(k)):
    print(j+1,". ", k[j], sep='')
    

#Configuring the simulation and displaying the properties of the chosen planet
t_planet = input("Enter the name of the planet you want to choose: ")

if t_planet not in Planets:
    print("Invalid planet name. Please choose from the available planets.")


else:
    print("The mass of", t_planet, "is", Planets[t_planet]['mass'], "kg")
    print("The semi-major axis of", t_planet, "is", Planets[t_planet]['a'], "m")
    print("The orbital speed of", t_planet, "is", Planets[t_planet]['v'], "m/s")
    print()

    #Defining the arrays for the position and the velocity vectors of the planet

    #The sun is at the origin of the coordinate system (0,0)
    #Initial position vector of planet
    r_0 = np.array([Planets[t_planet]['a'],0.0])

    #Initial velocity vector of planet
    v_0 = np.array([0.0, Planets[t_planet]['v']])

    #Joined the two initial arrays together
    state_0 = np.hstack((r_0, v_0))
    print("The initial position and velocity vectors of",t_planet,"are: ")
    print(state_0)
    print()


    #Defining the sun's position and velocity vectors in our cartesian coordinate system
    #The sun is at the origin of the coordinate system (0,0)
    #In my code I will assume that the sun is stationary at the origin of the coordinate system, and its initial position and velocity vectors are both zero.

    #Initial position vector of the sun
    r_sun = np.array([0.0, 0.0])

    #Initial velocity vector of the sun
    v_sun = np.array([0.0, 0.0])

    #Joined the two initial arrays together
    state_sun = np.hstack((r_sun, v_sun))
    print("The initial position and velocity vectors of the sun are: ")
    print(state_sun)
    print()


    #Defining the initial conditions of the spacecraft

    #Here, I will take the radii of the planets as mean approximations of their actual radii
    r_planet = Planets[t_planet]['r']

    #Setting up the incoming spacecraft

    #Initial distance of the target planet (m)
    D = 50e9

    #Sideways offset from the target planet
    b = 20 * r_planet

    #Initial position vector of the spacecraft
    r_sc = r_0 + np.array([-D, b])

    #Assumed incoming speed of the spacecraft (m/s)
    v_relative = float(input("Please enter the incoming velocity of the spacecraft (m/s): "))
    print()

    #Initial velocity vector of the spacecraft
    v_sc = v_0 + np.array([v_relative, 0.0])

    #Joined the two initial arrays together
    state_sc = np.hstack((r_sc, v_sc))
    print("The initial position and velocity vectors of the spacecraft are: ")
    print(state_sc)
    print()

    #My code assumes that all of the planets, the sun and the spacecraft are on the positive x-axis
    #This isn't a realistic assumption, but it simplifies calculations and allows the code to simulate the gravity assist manoeuvre better. 

    #Defining the accelearion function for the spacecraft
    def acceleration(t, state):
        #Extracting the planet's position and velocity
        state_planet = state[0:4]
        r_planet_current = state_planet[0:2]
        v_planet_current = state_planet[2:4]

        #Extracting the spacecraft's position and velocity
        state_sc = state[4:8]
        r_spacecraft = state_sc[0:2]
        v_spacecraft = state_sc[2:4]

        #Calculating distance from the sun
        d_planet_sun = np.linalg.norm(r_planet_current)
        d_sc_sun = np.linalg.norm(r_spacecraft)

        #Calculating distance between planet and spacecraft
        r_relative = r_spacecraft - r_planet_current
        d_relative = np.linalg.norm(r_relative)

        #Acceleration of planet due to Sun
        a_planet = -G * M_sun * r_planet_current / d_planet_sun**3

        #Acceleration of spacecraft due to Sun
        a_sun_sc = -G * M_sun * r_spacecraft / d_sc_sun**3

        #Acceleration of spacecraft due to planet
        a_planet_sc = -G * Planets[t_planet]['mass'] * r_relative / d_relative**3

        #We know that the total acceleration will be the vecotr sum of the 2 accelerations acting on it
        #Hence, the total acceleration can be written as:
        a_spacecraft = a_sun_sc + a_planet_sc

        #Returning the state variables
        return np.hstack((
            v_planet_current,
            a_planet,
            v_spacecraft,
            a_spacecraft
        ))

    #Joining the initial states of the planet and the spacecraft
    state_initial = np.hstack((state_0, state_sc))

    #Setting up the simulation duration

    if v_relative <= 0:
        raise ValueError("Incoming velocity must be positive please try again!")

    #Here we give the spacecraft roughly enough time to travel
    #Therefore, we take the distance as 2 * D
    #The fomula used is time = distance / velocity
    t_end = 2 * D / v_relative

    #Time interval in seconds
    t_span = (0,t_end)
