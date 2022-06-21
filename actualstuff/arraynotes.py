import numpy as np

#arrays are special variables that hold more than one value; very useful for holding large amounts of data

Numbers = ["1", "2", "3", "4"]

x = Numbers[0]  #finds the value of the specific item in the array
Numbers[0] = "0"  #can modify the elements of an array 

#len() method returns the length of an array 

x = len(Numbers)

#can use a for loop to loop through the items of an array


for x in (Numbers):
    print(x)
else:
    print("The array has been looped through.")


#append() method is used to add items to an array

Numbers.append("5") #the command can only take one argument
Numbers.append("6")

for x in (Numbers):
    print(x)
else: 
    print("The second array has been looped through.")

#pop() method is used to remove items from an array

Numbers.pop(4) #the argument in the function is the position of the item

#remove() method is used to remove items from an array aswell

Numbers.remove("4") #the arguemnt in the function is the name of the specific element 

#to make a 2d array, set the second dimension next to the first

Numbers2 = [["1", "2", "3"],
            ["4", "5", "6"]]
for x in Numbers2:
    for y in Numbers2:
        print(x,y)

#clear() removes all elements from the list
#copy() returns a copy of the list
#count() counts the number of items in the array
#extend() adds the element of a list to the end of a current list
#index() returns the index of the specified element 
#reverse() reverses the order of the list
#sort() sorts the list 

#there are three types of arrays
#first way is to turn any list in an array

#full() fills the array with numbers
#z = np.zero(5, dtype=np.bool)
#t = np.full(5,3) #fills the array with five 3s 

#math in arrays works on each element
a = ["2", "4", "6"]




import pickle
import numpy as np
import matplotlib.pyplot as plt


file = 'orbits_prelim.pkl'

with open(file,'rb') as f:
    data = pickle.load(f)

yay = data['data']

print(data)

time = yay[0]['Time']
mass = yay[0]['mass']

x = time
y = mass

h,xmids,_ = plt.hist(x)
h,xedges = np.histogram(x, bins=20, range=[0,0.35])
xmids=0.5*(xedges[0:-1]+xedges[1:])
#plt.semilogy(time,mass)
plt.bar(xmids,h,width=0.1)
plt.show()






plt.plot(time,mass)
plt.xlabel('time (strange units, TBD)')
plt.yscale("log")
plt.ylabel('mass (Msun)')
plt.savefig("pickle.png")





