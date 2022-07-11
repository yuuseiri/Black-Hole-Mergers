import pynbody 
import os
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d

directory = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/'
directory2 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test2/'

x = []
y = []
z = [] 
vx = []
vy = []
vz = []

x2 = []
y2 = []
z2 = [] 
vx2 = []
vy2 = []
vz2 = []

for filename in sorted(os.listdir(directory)):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and (filename.endswith(".param") == False) and (filename.endswith(".list") == False) and (filename.endswith(".txt") == False):
        i = pynbody.load(f)
        print(i.stars['pos'])
        print(i.stars['vel'])
        x.append(i.stars['pos'][:,0])
        y.append(i.stars['pos'][:,1])
        z.append(i.stars['pos'][:,2])
        vx.append(i.stars['vel'][:,0])
        vy.append(i.stars['vel'][:,1])
        vz.append(i.stars['vel'][:,2])
    else: 
        print("There was a non data file")

for filename in sorted(os.listdir(directory2)):
    f = os.path.join(directory2, filename)
    if os.path.isfile(f) and (filename.endswith(".BHmergers") == False) and (filename.endswith(".BlackHoles") == False) and (filename.endswith(".txt~") == False) and (filename.endswith(".txt") == False) and (filename.endswith("608") == False) and (filename.endswith("609") == False) and (filename.endswith(".py") == False) and (filename.endswith(".list") == False) and (filename.endswith(".pkl") == False) and (filename.endswith(".iords") == False) and (filename.endswith(".param") == False):
        k = pynbody.load(f)
        print(k.stars['pos'])
        print(k.stars['vel'])
        x2.append(k.stars['pos'][:,0])
        y2.append(k.stars['pos'][:,1])
        z2.append(k.stars['pos'][:,2])
        vx2.append(k.stars['vel'][:,0])
        vy2.append(k.stars['vel'][:,1])
        vz2.append(k.stars['vel'][:,2])
    else: 
        print("There was a non data file.")

x = np.array(x).flatten() 
y = np.array(y).flatten()
z = np.array(z).flatten()

x2 = np.array(x2).flatten() 
y2 = np.array(y2).flatten()
z2 = np.array(z2).flatten()

rho =  np.power((np.power(x, 2) + np.power(y, 2) + np.power(z, 2)), 0.5)
theta = np.arctan(np.divide(y, x))
phi = np.arccos(np.divide(z, np.power((np.power(x, 2) + np.power(y, 2) + np.power(z, 2)), 0.5)))

rho2 = np.power((np.power(x2, 2) + np.power(y2, 2) + np.power(z2, 2)), 0.5)
theta2 = np.arctan(np.divide(y2, x2))
phi2 = np.arccos(np.divide(z2, np.power((np.power(x2, 2) + np.power(y2, 2) + np.power(z2, 2)), 0.5)))

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_title("Black Hole Position")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.plot3D(x, y, z, 'green')

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_title("Black Hole Velocity")
ax.set_xlabel("VX")
ax.set_ylabel("VY")
ax.set_zlabel("VZ")
ax.scatter3D(vx, vy, vz, 'blue')

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_title("Black Hole Position 2")
ax.set_xlabel("X2")
ax.set_ylabel("Y2")
ax.set_zlabel("Z2")
ax.plot3D(x2, y2, z2, 'green')

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_title("Black Hole Velocity 2")
ax.set_xlabel("VX2")
ax.set_ylabel("VY2")
ax.set_zlabel("VZ2")
ax.scatter3D(vx2, vy2, vz2, 'blue')

fig = plt.figure()
ax.set_title("Spherical 1")
ax.set_xlabel("VX2")
ax.set_ylabel("VY2")
ax.set_zlabel("VZ2")
ax = fig.add_subplot(1,1,1, projection='3d')
plot = ax.plot_trisurf(
    rho, theta, phi, cmap=plt.get_cmap('jet'),
    linewidth=0, antialiased=False, alpha=0.5)

fig = plt.figure()
ax.set_title("Spherical 2")
ax.set_xlabel("VX2")
ax.set_ylabel("VY2")
ax.set_zlabel("VZ2")
ax = fig.add_subplot(1,1,1, projection='3d')
plot = ax.plot_trisurf(
    rho2, theta2, phi2, cmap=plt.get_cmap('jet'),
    linewidth=0, antialiased=False, alpha=0.5)

plt.show()    


    
'''
files = np.loadtxt("files.list", dtype = 'str')
for x in files:  #filename > file 
    i = pynbody.load(x)
    print(i.stars['pos'])
    print(i.stars['vel'])
'''
