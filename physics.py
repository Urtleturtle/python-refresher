import numpy as np
G = 9.81
WATER_DENSITY = 1000

def calculate_buoyancy(V, density_fluid):
    return V*density_fluid*G

def will_it_float(V, mass):
    return mass/V < WATER_DENSITY

def calculate_pressure(depth):
    return depth*G*WATER_DENSITY

def calculate_acceleration(F, m):
    return F/m

def calculate_angular_acceleration(tau, I):
    return tau/I

def calculate_torque(F_magnitude, F_direction, r):
    F_direction = F_direction* (np.pi/180)
    return F_magnitude*r*np.sin(r)

def calculate_moment_of_inertia(m,r):
    return m*(r**2)

def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100, volume = 0.1, thruster_distance = 0.5):
    return F_magnitude/mass

def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia = 1, thruster_distance = 0.5):
    return calculate_torque(F_magnitude,F_angle,thruster_distance)/inertia

def calculate_auv2_acceleration(T, alpha, theta, mass = 100):
    T_dir = np.ndarray([alpha, 2*np.pi - alpha, np.pi + alpha, 180 - alpha])
    hor_components = np.zeros(4)
    ver_components = np.zeros(4)

    for i in range(4):
        hor_components[i] = 

    return np.sqrt((np.sum(hor_components)**2) + (np.sum(ver_components)**2))/mass
