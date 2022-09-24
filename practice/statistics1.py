import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import stats 

data1 = np.loadtxt('data1.txt') #data set 1 is definitely not normal, skewed right
data2 = np.loadtxt('data2.txt')
data3 = np.loadtxt('data3.txt')

#manually
np.sort(data1)
print(np.divide(np.sum(data1), len(data1)))
print(data1[int(np.subtract(np.divide(len(data1), 2), 0.5))])

#actual 
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

#t = np.divide((np.subtract(np.average(data2), np.average(data3))), np.power(np.divide)

plt.hist(data1,bins=15)
plt.show()
plt.hist(data2,bins=10)
plt.show()
plt.hist(data3,bins=10)
plt.show()
