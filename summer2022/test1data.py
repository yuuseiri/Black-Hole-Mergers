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
        print("There was a .param or .txt file")

x = np.array(x).flatten() 
y = np.array(y).flatten()
z = np.array(z).flatten()

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(x, y, z)
ax.scatter3D(vx, vy, vz, cmap='Blues')

plt.show()    


    
'''
files = np.loadtxt("files.list", dtype = 'str')
for x in files:  #filename > file 
    i = pynbody.load(x)
    print(i.stars['pos'])
    print(i.stars['vel'])
'''
