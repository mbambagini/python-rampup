# define a non-homogeneous list
print("-> List definition")
myList = ['string', 10, 3.4]
print(myList)

# access content
print("-> List access")
myList = ['first', 'second', 'third', 'forth']
print("At 0:\t" + myList[0])
print("At 1:\t" + myList[1])
print("At 2:\t" + myList[2])
print("At 3:\t" + myList[3])
print("At -1:\t" + myList[-1])
print("At -2:\t" + myList[-2])
print("At -3:\t" + myList[-3])
print("At -4:\t" + myList[-4])

# add content
print("-> Add to a list")
myList.append('fifth')
myList.append('seventh')
myList.insert(5, 6)
print(myList)

# modify content
print("-> Modify a list")
myList[5] = 'sixth'
print(myList)

# delete content
print("-> Delete from a list")
del myList[5]
print(myList)
myList.pop()
print(myList)
a = myList.pop(3)
print(myList)
myList.remove('third')
print(myList)

# sort list
print("-> Sort to a list")
print(sorted(myList))
myList.sort()
print(myList)
myList.reverse()
print(myList)

# iterate over lists
print("-> Loop over a list")
numbers = ['first', 'second', 'third', 'forth']
for number in numbers:
    print(number)

# operations on lists
print("-> List methods")
even_numbers = list(range(0,10,2))
print(even_numbers)
print("Min: " + str(min(even_numbers)))
print("Max: " + str(max(even_numbers)))
print("Sum: " + str(sum(even_numbers)))
print("Num elements: " + str(len(myList)))

# sub lists
print("-> Sub list")
print("First three even numbers: " + str(even_numbers[:3]))

# tuple
print("-> Tuples")
size = (100, 200, 300)
print("Size H: " + str(size[0]))
print("Size W: " + str(size[1]))
print("Size L: " + str(size[2]))
sizes = [size, size]
print(sizes)

