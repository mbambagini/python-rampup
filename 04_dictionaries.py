# dictionary definition
print("-> Dictionary definition")

dictionary = {'key1' : 'value1', 'key2' : 2, 3 : 'value3'}

print(dictionary['key1'])
print(dictionary[3])

print(dictionary)

# add elements
print("-> Add to a dictionary")
dictionary = {}
dictionary['key1'] = 'value1';
dictionary['key2'] = 2;
print(dictionary)

# modify element
print("-> Modify a dictionary")
dictionary['key2'] = 'value2';
print(dictionary)

# delete element
print("-> Delete from a dictionary")
del dictionary['key2']
print(dictionary)

# loop over elements
print("-> Loop over a dictionary")
dictionary = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
for key,value in dictionary.items():
    print("key (" +str(key)+ ") value (" +str(value)+ ")")

for name in dictionary.keys(): #key is the default element
    print("key (" +str(name)+ ") value (" +str(dictionary[name])+ ")")


for name in dictionary.values(): #key is the default element
    print("value (" +str(name)+ ")")

# lists and dictionaries can be combined

