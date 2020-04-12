import json

animals = ['dog', 'cat', 'horse', 'rabbit']
filename = 'animal.txt'

# serialize data to a json file
with open(filename, 'w') as fobj:
    """dump a variable for each file"""
    json.dump(animals, fobj)

# deserialize data from a json file
with open(filename) as fobj:
    animals2 = json.load(fobj)
    print(animals2)

