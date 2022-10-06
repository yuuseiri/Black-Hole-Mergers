import numpy as np
import random
import matplotlib.pyplot as plt
import scipy as sc
from scipy import stats 
from sklearn.utils import shuffle 

data1 = np.loadtxt('data1.txt') #data set 1 is definitely not normal, skewed right
data2 = np.loadtxt('data2.txt') #data 2 is NOT normal
data3 = np.loadtxt('data3.txt') #data 3 looks normal enough

#manually
print("This is the manual method.")
np.sort(data1)
print(np.divide(np.sum(data1), len(data1))) #mean is just sum of numbers over number of numbers
print(data1[int(np.subtract(np.divide(len(data1), 2), 0.5))]) #median is center number

#actual 
print("This is the fast method.")
print("The average temperature in spring is", np.average(data1), "degrees Celsius.")
print("The average height of a 5-year-old child in Syria is", np.average(data2), "centimeters.")
print("The average height of a 5-year-old child in the United States is", np.average(data3), "centimeters.")

print("The median temperature in spring is ", np.median(data1), "degrees Celsius.")
print("The median height of a 5-year-old child in Syria is", np.median(data2), "centimeters.")
print("The median height of a 5-year-old child in the United States is", np.median(data3), "centimeters.")

print("The kurtosis of data set 1 is", sc.stats.kurtosis(data1))
print("The kurtosis of data set 2 is", sc.stats.kurtosis(data2))
print("The kurtosis of data set 3 is", sc.stats.kurtosis(data3))

print("The skew of data set 1 is", sc.stats.skew(data1))
print("The skew of data set 2 is", sc.stats.skew(data2))
print("The skew of data set 3 is", sc.stats.skew(data3))

''' #this doesn't work help 
d2 = []
d3 = []

d2.append(data2)
d3.append(data3)

s2 = []
s3 = []

s2.append(np.power(np.divide(np.sum(np.subtract(d2, np.average(d2), len(d2)))), 0.5)) #this shit don't work
s3.append(np.power(np.divide(np.sum(np.subtract(data3, np.average(data3), len(data3)))), 0.5))

t = np.divide((np.subtract(np.average(data2), np.average(data3))), np.power(np.add(np.divide(s2, len(data2)), np.divide(s3, len(data3))), 0.5))

print(t)
'''
plt.figure()
counts, edges, plot = plt.hist(data1, bins = 10) #edges are the edges of the bins, counts are the quantity per bin
plt.title("Average Spring Temperature (Celcius)")
data1_ind = np.unravel_index(np.argmax(counts), counts.shape)
print("The mode of data1 set is", edges[data1_ind]) #mode is calculated by intervals represented by bins


plt.figure()
counts, edges, plot = plt.hist(data2, bins = 10)
plt.title("Heights of 5-year-old children in Syria")
data2_ind = np.unravel_index(np.argmax(counts), counts.shape)
print("The mode of data2 set is", edges[data2_ind])

plt.figure()
counts, edges, plot = plt.hist(data3, bins = 10)
plt.title("Heights of 5-year-old children in the U.S.")
data3_ind = np.unravel_index(np.argmax(counts), counts.shape)
print("The mode of data3 set is", edges[data3_ind])

#normalizing data1
means = []

for i in range(0, 10000): #larger range = more normal distribution due to larger sample size 
    random.shuffle(data1) #randomly shuffles the data set per i in the loop
    x = data1[0:40] #takes the first 40 elements of the now shuffled data set (n = 40 here)
    q = np.average(x) #takes the average of the now 40 elements of a new array
    means.append(q) 

array = np.array(means)
    
plt.figure()
plt.hist(array, bins = 30)

#normalizing data2
means2 = []

for j in range(0, 10000):
    random.shuffle(data2) 
    y = data2[0:40]
    h = np.average(y)
    means2.append(h)

array2 = np.array(means2)
    
plt.figure()
plt.hist(array2, bins = 30)

plt.show()
