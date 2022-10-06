#for loops can execute a set of statements for each item in a list

'''
fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits:
    print(x)
'''

#strings of text contain a sequence of characters, which can also be iterated with a for loop

'''
for x in "banana": 
    print(x)
'''

#the break statement stops the for loop from going through the entire list if the loop runs into the breaking item

'''
fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits:
    print(x)
    if x == "cherry":
        break
'''

#the loop will execute the command on the item that it is breaking on 

#to not execute the command on the breaking item, 

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "cherry":
    break
  print(x)
'''

#the continue statement skip the command on the item 

'''
fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits:
  if x == "cherry":
    continue
  print(x)
'''

#the range() function controls the number of times we loop through a list

'''
for x in range(6):
    print(x)
'''

#to limit the range, add a parameter 

'''
for x in range(2, 6):
    print(x)
'''

#to add an increment to the loop, add a third parameter after the range of items

'''
for x in range(2, 50, 6):  #the format is (lower bound range parameter, upper bound, increment)
    print(x)
'''

#the else keyword executes something when the loop has finished

'''
for x in range(3, 50, 8):
    print(x)
else: 
    print("The loop has finished")
'''

#nested loops are loops within loops

#the inner loop will be executed one time for each iteration of the outer loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in adj:
  

#if for some reason the loop has no content, use the pass statement to skip over the loop to avoid any errors