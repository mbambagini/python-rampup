# define a non-homogeneous list
myList = ['string', 10, 3.4]
print(myList)

# access content
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
myList.append('fifth')
myList.append('seventh')
myList.insert(5, 6)
print(myList)

# modify content
myList[5] = 'sixth'
print(myList)

# delete content
del myList[5]
print(myList)
myList.pop()
print(myList)
a = myList.pop(3)
print(myList)
myList.remove('third')
print(myList)

# sort list
print(sorted(myList))
myList.sort()
print(myList)
myList.reverse()
print(myList)

# iterate over lists
numbers = ['first', 'second', 'third', 'forth']
for number in numbers:
    print(number)

# appent
numbers = []
for i in range(1,10):
    numbers.append(i)
print(numbers)

# operations on lists
even_numbers = list(range(0,10,2))
print(even_numbers)
print("Min: " + str(min(even_numbers)))
print("Max: " + str(max(even_numbers)))
print("Sum: " + str(sum(even_numbers)))

# sub lists
print("First three even numbers: " + str(even_numbers[:3]))

# get length
print(len(myList))

# tuple
size = (100, 200, 300)
print("Size H: " + str(size[0]))
print("Size W: " + str(size[1]))
print("Size L: " + str(size[2]))
sizes = [size, size]
print(sizes)

