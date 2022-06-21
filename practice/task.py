import numpy as np
import matplotlib.pyplot as plt


redshift = np.loadtxt("times.list")[:, 0]
time = np.loadtxt("times.list")[:, 1]

reversed_redshift = redshift[::-1]
reversed_time = time[::-1]


for x in redshift:
    for y in time:
        plt.plot(redshift, time)

        plt.xlabel('time (Gigayears)')
        plt.ylabel('redshift (unitless)')

        #plt.gca().invert_xaxis()
        #plt.gca().invert_yaxis()

        plt.show()



