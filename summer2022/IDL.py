import pynbody
import numpy as np
import struct
from pytipsy import wtipsy #writes
from pytipsy import rtipsy  #reads  

file = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/DMOnlyCollapse_5e11_8388608_Physical_0.01.000480'
file2 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/DMOnlyCollapse_5e11_8388608_Physical_0.01_BH2.000480'
file3 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/DMOnlyCollapse_5e11_8388608_Physical_0.01_BH3.000480'
file4 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/DMOnlyCollapse_5e11_8388608_Physical_0.01_BH4.000480'
file5 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/DMOnlyCollapse_5e11_8388608_Physical_0.01_BH5.000480'

h, g, d, s = rtipsy(file)

softening = 3.11226E-06

munit = 1.84793E16
mass = [((1E7)/munit), ((1E7)/munit)]
x = [0.0, (15/50000)] #divide by 50000
y = [0.0, 0.0]
z = [0.0, 0.0]
vx = [0.0, 0.0] #conversion factor is 1260
vy = [0.0, (6.82/1260)]
vz = [0.0, 0.0]
phi = [0.0, 0.0]
eps = [softening, softening]
tform = [-1.0, -1.0]
metals = [0.0, 0.0]

s = {'mass':mass, 'x':x, 'y':y, 'z':z, 'vx':vx, 'vy':vy, 'vz':vz, 'metals':metals, 'tform':tform, 'eps':eps, 'phi':phi}
header = {'time':h['time'], 'n':h['n'] + 2, 'ndim':h['ndim'], 'ngas':h['ngas'], 'ndark':h['ndark'], 'nstar':h['nstar'] + 2} #edit h + n
print("writing file")
wtipsy(file5, header, g, d, s)