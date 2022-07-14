import pickle
import numpy as np
import pynbody

point1 = "/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test3/dennis.000001"
f = pynbody.load(point1)

g = f['pos'][0]
h = f['vel'][0]

x = []
y = []
z = []
vx = []
vy = []
vz = []

x.append(g[0])
y.append(g[1])
z.append(g[2])
vx.append(h[0])
vy.append(h[1])
vz.append(h[2])

mag1 = np.power((np.power(vx, 2) + np.power(vy, 2) + np.power(vz, 2)), 0.5)

rho =  np.power((np.power(x, 2) + np.power(y, 2) + np.power(z, 2)), 0.5)
theta = np.arctan(np.divide(y, x))
phi = np.arccos(np.divide(z, np.power((np.power(x, 2) + np.power(y, 2) + np.power(z, 2)), 0.5)))

rho2 =  np.power((np.power(vx, 2) + np.power(vy, 2) + np.power(vz, 2)), 0.5)
theta2 = np.arctan(np.divide(vy, vx))
phi2 = np.arccos(np.divide(vz, np.power((np.power(vx, 2) + np.power(vy, 2) + np.power(vz, 2)), 0.5)))

print("000001 Position:", rho[0]*50000, np.degrees(theta[0]), np.degrees(phi[0]))
print("000001 Velocity Magnitude:", mag1*1260)
print("000001 Velocity Direction:", np.degrees(theta2[0]), np.degrees(phi2[0]))