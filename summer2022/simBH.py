import pickle
import numpy as np
import pynbody

#loaded with pickle or pynbody

'''
point1 = "/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test7/dennis.000005"
f = pynbody.load(point1)

g = f.stars['pos'][0] #loadable_keys
h = f.stars['vel'][0]

x = [] #makes empty array 
y = []
z = []
vx = []
vy = []
vz = []

x.append(g[0]) #append data into empty array 
y.append(g[1])
z.append(g[2])
vx.append(h[0])
vy.append(h[1])
vz.append(h[2])
'''

file = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test7/blackholes.pkl'

with open(file,'rb') as f:
    data = pickle.load(f)

yay = data['data']

#finds the details at the time of recoil

time1 = yay[0]['Time']
x = yay[0]['x'][np.where(time1 == 0.184735)]
y = yay[0]['y'][np.where(time1 == 0.184735)]
z = yay[0]['z'][np.where(time1 == 0.184735)]
vx = yay[0]['vx'][np.where(time1 == 0.184735)]
vy = yay[0]['vy'][np.where(time1 == 0.184735)]
vz = yay[0]['vz'][np.where(time1 == 0.184735)]

#spherical coordinates equations 

mag1 = np.power((np.power(vx, 2) + np.power(vy, 2) + np.power(vz, 2)), 0.5)

rho =  np.power((np.power(x, 2) + np.power(y, 2) + np.power(z, 2)), 0.5)
theta = np.arctan(np.divide(y, x))
phi = np.arccos(np.divide(z, np.power((np.power(x, 2) + np.power(y, 2) + np.power(z, 2)), 0.5)))

rho2 =  np.power((np.power(vx, 2) + np.power(vy, 2) + np.power(vz, 2)), 0.5)
theta2 = np.arctan(np.divide(vy, vx))
phi2 = np.arccos(np.divide(vz, np.power((np.power(vx, 2) + np.power(vy, 2) + np.power(vz, 2)), 0.5)))

print("Recoil Position:", rho[0], np.degrees(theta[0]), np.degrees(phi[0]))
print("Recoil Velocity Magnitude:", mag1)
print("Recoil Velocity Direction:", np.degrees(theta2[0]), np.degrees(phi2[0]))