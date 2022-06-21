import numpy as np
import matplotlib.pyplot as plt
from astropy.table import QTable 
import astropy.units as u
from numpy import *
import pickle as pkl
import pylab as pl
import pandas as pd


data = np.loadtxt('findBH.txt')
BH,distance = np.loadtxt('findBH.txt',unpack=True,usecols=[1,3])

#file = 'findBH.txt'

#ith open(file,'rb') as f:
    #data = np.loadtxt(f)

#yes = data[:,0]
BH = data[:,1]
distance = data[:,3]

BH1 = BH[np.mod(np.arange(BH.size),3)!=2]
distance1 = distance[np.mod(np.arange(distance.size),3)!=2]

x = np.log10(distance1)
h,xmids,_ = plt.hist(x)

plt.xlabel('Distance from center [Units] ')
plt.ylabel('Frequency [Units]')
plt.show()



'''
data = np.random.normal(size=10000)
pl.hist(data, bins=np.logspace(np.log10(0.1),np.log10(1.0), 50))
pl.gca().set_xscale("log")
'''

'''

t = QTable([BH1, distance1], names=['BH1', 'distance1'])
t['BH1'].unit = 'Black hole Name'
t['distance1'].unit = 'distance unit'

print(t)
'''


'''

data = np,arange(63).reshape((3,21))
print(data[0:2:1,0:21:3])

data = range(63)
print(data[[[0],[1]],[1,3]])


t = QTable([BH, distance], names=['BH', 'distance'])
#t['BH'].unit = 'Black hole Name'
#t['distance'].unit = 'distance unit'

print(t[1][2])

x = BH
y = distance


for index, element in enumerate(yes):
    if index % 3 == 0 or index % 2 == 0 or index == 1:
        print(element)
    else: 
        print('Merger')

for index, in enumerate(data):
    distance = data[:,j]

'''
#hist, bins, _ = plt.hist(distance1, bins=10)
#logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))

#plt.xlabel("Primary", "Secondary", "Merged")
#plt.bar(x,height=y,width=0.75)

