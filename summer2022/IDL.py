import pynbody
import numpy as np

file = "DMOnlyCollapse_5e11_8388608_Physical_0.01.000480"
file2 = 'DMOnlyCollapse_5e11_8388608_Physical_0.01_BH.000480'

f = pynbody.load(file2) #loads the file 
f.properties
 
f.loadable_keys()  #size of each array is 8388608 (1-8388609)
f['vel'][8388608]  
f['eps'][8388608]
f['phi'][8388608]
f['mass'][8388608]
f['pos'][8388608]

'''

array = pynbody.array.SimArray(np.array(file2[0]))
array.sim = f
array



#h = f.header
d = f.dark
#g = f.gas
s = f.star

'''


munit = 1.84793E16
mass = (1E7)/munit
x = 0.0
y = 0.0
z = 0.0
vx = 0.0
vy = 0.0
vz = 0.0
phi = 0.0
eps = 3.11226E-06
tform = -1.0
metals = 0.0

rtipsy('DMOnlyCollapse_5e11_8388608_Physical_0.01.000480')



s = {mass:mass, x:x, y:y, z:z, vx:vx, vy:vy, vz:vz, metals:metals, tform:tform, eps:eps, phi:phi}
h.nstar = 1L #???????????????
h.n = h.n + 1L

print("writing file")
wtipsy('DMOnlyCollapse_5e11_8388608_Physical_0.01_BH.000480')