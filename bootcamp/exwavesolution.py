from numpy import empty 
from pylab import imshow,gray,show
import numpy as np

wavelength = 5.0
k = 2*np.pi/wavelength 
xi0 = 1.0
separation = 20.0
side = 100.0
points = 500 
spacing = side/points 
x1 = side/2 + separation/2 
y1 = side/2 
x2 = side/2 - separation/2 
y2 = side/2 
xi = empty([points,points],float)

for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        r1 = (((x - x1)**2) + ((y - y1)**2))**0.5
        r2 = (((x - x2)**2) + ((y - y2)**2))**0.5
        xi[i,j] = xi0*np.sin(k*r1) + xi0*np.sin(k*r2)

imshow(xi,origin = 'lower', extent = [0, side, 0, side])
gray()
show()

#loop runs until it reaches the integer value