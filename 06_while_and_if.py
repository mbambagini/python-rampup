from random import randrange

# example with while loop and if statement

print("-> Search for a random number")
upper = 1000
lower = 0
var = randrange(lower, upper)
current_val = (upper-lower)/2
step = 1

while True:
    if current_val == var:
        break
    elif current_val < var:
        lower = current_val
        current_val = int((upper-current_val)/2+current_val)
    else: # current_val > var
        upper = current_val
        current_val = int((current_val-lower)/2+lower)
    step += 1

print("The value was " + str(current_val) + " in " + str(step) + " steps")

# multi conditions
print("-> Multi condition")
boolVal = True;
myList = range(1,10)
if myList and 3 in myList and boolVal:
    print("The condition is true")
else:
    print("The condition is false")

