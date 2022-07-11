import pickle
import numpy as np
import matplotlib.pyplot as plt

file = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test2/blackholes.pkl'

with open(file,'rb') as f:
    data = pickle.load(f)

yay = data['data']
yay[0].keys()

x1 = yay[0]['x']
y1 = yay[0]['y']
z1 = yay[0]['z']
time1 = yay[0]['Time']

x2 = yay[1]['x']
y2 = yay[1]['y']
z2 = yay[1]['z']
time2 = yay[0]['Time']

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_title("Black Hole Position")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.plot3D(x1, y1, z1, 'green')

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_title("Black Hole Position 2")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.plot3D(x2, y2, z2, 'green')

plt.show()


