import pynbody
import numpy as np
import struct
from pytipsy import wtipsy #writes
from pytipsy import rtipsy  #reads  

file = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/DMOnlyCollapse_5e11_8388608_Physical_0.01.000480'
file2 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/DMOnlyCollapse_5e11_8388608_Physical_0.01_BH2.000480'
file3 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/DMOnlyCollapse_5e11_8388608_Physical_0.01_BH3.000480'

h, g, d, s = rtipsy(file)

munit = 1.84793E16
mass = [((1E7)/munit), ((1E7)/munit)]
x = ['0.0', '3.11226E-06']
y = ['0.0', '0.0']
z = ['0.0', '0.0']
vx = ['0.0', '0.0']
vy = ['0.0', '0.0']
vz = ['0.0', '0.0']
phi = ['0.0', '0.0']
eps = ['3.11226E-06', '3.11226E-06']
tform = ['-1.0', '-1.0']
metals = ['0.0', '0.0']

s = {'mass':mass, 'pos':[x,y,z], 'vel':[vx,vy,vz], 'metals':metals, 'tform':tform, 'eps':eps, 'phi':phi}
header = {'time':h['time'], 'n':h['n'] + 2, 'ndim':h['ndim'], 'ngas':h['ngas'], 'ndark':h['ndark'], 'nstar':h['nstar'] + 2} #edit h + n
print("writing file")
#wtipsy(file2, h, g, d, s)
wtipsy(file3, h, g, d, s)





'''
f = pynbody.load(file2) #loads the file 
f.properties
 
f.loadable_keys()  #size of each array is 8388608 (1-8388609)
f['vel'][8388608]  
f['eps'][8388608]
f['phi'][8388608]
f['mass'][8388608]
f['pos'][8388608]
'''