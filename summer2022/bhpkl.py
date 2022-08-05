import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

file = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test5stampede/blackholes.pkl'

with open(file,'rb') as f: #loads pickle files 
    data = pickle.load(f)

yay = data['data']

x1 = yay[0]['x']
y1 = yay[0]['y']
z1 = yay[0]['z']
vx1 = yay[0]['vx']
vy1 = yay[0]['vy']
vz1 = yay[0]['vz']
time1 = yay[0]['Time']

x2 = yay[1]['x']
y2 = yay[1]['y']
z2 = yay[1]['z']
vx2 = yay[1]['vx']
vy2 = yay[1]['vy']
vz2 = yay[1]['vz']
time2 = yay[1]['Time']

'''
print(vx1[np.where(time1 == 0.184735)]) #finds the position of element in array
print(vy1[np.where(time1 == 0.184735)])
print(vz1[np.where(time1 == 0.184735)])
'''
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_title("Black Hole Position")
ax.set_xlabel("X (kpc)")
ax.set_ylabel("Y (kpc)")
ax.set_zlabel("Z (kpc)")

N = len(time1) #makes the lines cool colors 
for i in range(N-1):
    p = ax.plot3D(x1[i:i+2], y1[i:i+2], z1[i:i+2], color=plt.cm.jet(i/N))

N2 = len(time2)
for j in range(N2-1):
    p2 = ax.plot3D(x2[j:j+2], y2[j:j+2], z2[j:j+2], color=plt.cm.jet(j/N2))

plt.savefig("inserttitlehere.png") #saves the figure

fig = plt.figure() #conversion to real units from system units
plt.plot(np.multiply(np.subtract(np.multiply(time1, 38.462), 7.09), 1000), vx1, color = 'blue')
plt.plot(np.multiply(np.subtract(np.multiply(time1, 38.462), 7.09), 1000), vy1, color = 'orange')
plt.plot(np.multiply(np.subtract(np.multiply(time1, 38.462), 7.09), 1000), vz1, color = 'green')
plt.xlim([0, 80])
plt.xlabel("Time [Megayears]")
plt.ylabel("Velocity [km/s]")
plt.title("Black Hole 1 Velocity")

fig = plt.figure()
plt.plot(np.multiply(np.subtract(np.multiply(time2, 38.462), 7.09), 1000), vx2, color = 'blue')
plt.plot(np.multiply(np.subtract(np.multiply(time2, 38.462), 7.09), 1000), vy2, color = 'orange')
plt.plot(np.multiply(np.subtract(np.multiply(time2, 38.462), 7.09), 1000), vz2, color = 'green')
plt.xlim([0, 80])
plt.ylim([-70, 10])
plt.xlabel("Time [Megayears]")
plt.ylabel("Velocity [km/s]")
plt.title("Black Hole 2 Velocity")

plt.show()

#grep BHSink output.out