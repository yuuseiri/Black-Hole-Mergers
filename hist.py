import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('findBH.txt')
BH,distance = np.loadtxt('findBH.txt',unpack=True,usecols=[1,3])

file = 'findBH.txt'

with open(file,'rb') as f:
    data = np.loadtxt(f)

#BH = data[:,1]
distance = data[:,3]

y = distance[0:3]
print(y)
x = [1,2,3]
#plt.xlabel("Primary", "Secondary", "Merged")

plt.bar(x,height=y,width=0.75)

plt.show()