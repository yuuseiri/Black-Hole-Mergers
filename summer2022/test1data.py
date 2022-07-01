import pynbody 
import os
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d

directory = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/'

x = []
y = []
z = [] 
vx = []
vy = []
vz = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and (filename.endswith(".param") == False) and (filename.endswith(".txt") == False):
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
        print("There was a .param or .txt file")


fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.scatter3D(x, y, z, cmap='Greens')
ax.scatter3D(vx, vy, vz, cmap='Blues')

plt.show()    

    

