import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

"""
x = np.linspace(0,2*np.pi,100) 
y = np.sin(x)
plt.plot(x,y,color='green',linestyle='dashed') 

#plt.show()

y2=np.cos(x)
y3=np.tan(x)
plt.plot(x,y2,label='cos') #labels can be used to make a legend
plt.plot(x,y3,label='tan')
plt.legend()
plt.xlabel('degrees')
plt.title('Trig Functions')
plt.ylim([-2,2])

plt.show()
"""

"""
x = np.random.random(30)
y = 0.5*x +0.1*np.random.random(30)

#scatter is better for a set of points rathr than plot  

plt.scatter(x,y,marker='v',c='red') #can plot every point a different color
#plt.show()
"""

z = 0.1*x + 0.25+0.05*np.random.random(30)
plt.scatter(x,y,marker='+',c='green',label='y',s=50)
plt.scatter(x,z,marker='o',c='blue',label='z')
plt.legend()
#plt.show()


p1 = np.polyfit(x,y,1) #1 is the degree of the polynomial so a line (x^1)
p2 = np.polyfit(x,z,2)
xvals=np.linspace(0,1,10)
plt.plot(xvals,p1[1]+p1[0]*xvals,color='green',linestyle='dashed')
plt.plot(xvals,p2[2]+p2[1]*xvals+p2[0]*xvals**2,color='blue',linestyle='dotted')
plt.scatter(x,y,marker='+',c='green',label='y',s=50)
plt.scatter(x,z,marker='o',c='blue',label='z')
plt.legend()
plt.show()



