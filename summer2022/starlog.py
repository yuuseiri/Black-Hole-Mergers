import pynbody 
import numpy as np
import matplotlib.pyplot as plt

file = '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.starlog'
sl = pynbody.snapshot.tipsy.StarLog(file)

N = 100000000

temperature = np.array(sl['tempform'])(size = N)
density = np.array(sl['rhoform'])(size = N)
print(temperature)
print(density)

x = np.log10(temperature)
y = np.log10(density)

hist,xedges,yedges=np.histogram2d(x,y,bins = 100)


print(hist.shape)

plt.imshow(hist)

plt.colorbar()
plt.xlabel('Temperature')
plt.ylabel('Density')

plt.show()



#range[[40000000,180000000],[100,2000]]


'''

star = np.where(sl['tform'] > 0.0)
blackhole = np.where(sl['tform'] < 0.0)

new = sl[blackhole[0]]['tform']

#plt.xlim(-0.020,-0.005)
#plt.ylim(0,30)

plt.hist(new)
plt.xlabel("formation time (units?)")
plt.ylabel("Number of black holes")
plt.show()

'''



