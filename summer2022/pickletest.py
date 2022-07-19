import numpy as np
import pynbody

point1 = "/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test3/dennis.000001"
f = pynbody.load(point1)

f.physical_units()
radius = "15 kpc"
center = (0,0,0)
sphere = f[pynbody.filt.Sphere(radius, center)]

mass = sphere['mass'].sum().in_units("Msol")

print(mass)

kpctokm = 3.086E16
Msoltokg = 1.989E30
Msolunits = 1.85E16

R = np.multiply(15, kpctokm) #km
G = 6.6743E-20  #km^3/kg*s^2
M = np.multiply(mass, Msoltokg) #kg

v = np.power(np.divide(np.multiply(G, M), R), 0.5)

print(v)