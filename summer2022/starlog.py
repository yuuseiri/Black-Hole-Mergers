import pynbody 
import numpy as np
import matplotlib.pyplot as plt

file = '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.starlog'
sl = pynbody.snapshot.tipsy.StarLog(file)

temperature = np.array(sl['tempform'])
density = np.array(sl['rhoform'])
print(temperature)
print(density)

x = np.log10(temperature)
y = np.log10(density)

plt.hist2d(y,x,bins=200)
plt.colorbar()
plt.xlabel('Density')
plt.ylabel('Temperature')

#plt.gca().invert_yaxis()

plt.show()



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



