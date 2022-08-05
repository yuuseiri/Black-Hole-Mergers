import pynbody
import numpy as np
import struct
from pytipsy import wtipsy 
from pytipsy import rtipsy  

file = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/DMOnlyCollapse_5e11_8388608_Physical_0.01.000480'
file3 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/DMOnlyCollapse_5e11_8388608_Physical_0.01_BH3.000480'

h, g, d, s = rtipsy(file)

softening = 3.11226E-06

munit = 1.84793E16
mass = [((1E7)/munit), ((1E7)/munit)]
x = [softening, softening] 
y = [0.0, 0.0]
z = [0.0, 0.0]
vx = [0.0, 0.0] 
vy = [0.0, 0.0]
vz = [0.0, 0.0]
phi = [0.0, 0.0]
eps = [softening, softening]
tform = [-1.0, -1.0]
metals = [0.0, 0.0]

s = {'mass':mass, 'x':x, 'y':y, 'z':z, 'vx':vx, 'vy':vy, 'vz':vz, 'metals':metals, 'tform':tform, 'eps':eps, 'phi':phi}
header = {'time':h['time'], 'n':h['n'] + 2, 'ndim':h['ndim'], 'ngas':h['ngas'], 'ndark':h['ndark'], 'nstar':h['nstar'] + 2} 
print("writing file")
wtipsy(file3, header, g, d, s)