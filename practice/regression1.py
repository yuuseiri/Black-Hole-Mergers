import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import stats

print("Let x = weight and y = bodylength")

w = [57, 84, 90, 71, 77, 68, 73]
bl= [123, 129, 143, 125, 122, 125, 122]

aw = np.divide(np.sum(w), len(w))
abl = np.divide(np.sum(bl), len(bl))

diffx = []
diffy = []

for i in w:
  diffx.append((np.subtract(i, aw)))

for j in bl:
  diffy.append((np.subtract(j, abl)))

sxx = np.sum(np.power(diffx, 2))
syy = np.sum(np.power(diffy, 2))
sxy = np.sum(np.multiply(diffx, diffy))

print("This is sxx:", sxx)
print("This is syy:", syy)
print("This is sxy:", sxy)

betaone1 = np.divide(sxy, sxx)
betaone2 = np.divide(sxy, syy)
betaknot1 = np.subtract(abl, np.multiply(betaone1, aw))
betaknot2 = np.subtract(abl, np.multiply(betaone2, aw))

print("The regression line 1 is", "y =", betaknot1, "+", betaone1, "x")
print("The regression line 2 is", "y =", betaknot2, "+", betaone2, "x")

rsquared = np.divide(np.power(sxy, 2), np.multiply(sxx, syy))

sigmasxxsquared = np.divide(sxx, np.subtract(len(w), 2))
sigmasyysquared = np.divide(syy, np.subtract(len(bl), 2))

print("The estimation of variance for weight is", sigmasxxsquared)
print("The estimation of variance for body length is", sigmasyysquared)

print("The data set's r squared is ", rsquared)

