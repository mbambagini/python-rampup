def print_hello_world():
    """Comment"""
    print("Hello world!\n")

def f_with_inputs_output(arg1, arg2, arg3, arg4=100):
    """Comment"""
    print("first argument: " + arg1)
    print("second argument: " + arg2)
    print("third argument: " + arg3)
    arg3 = "++++" + arg3 + "++++"
    print("forth argument: " + str(arg4))
    return arg1+" and "+arg2

def f_with_lists(strings):
   for s in strings:
       print("List element: " + s);
   strings[1] = 'horse'

def f_with_ellipse(*animals):
   for animal in animals:
       print("Type of animal: " + animal);

# call function with no input no output
print("-> Basic function")
print_hello_world()

# call function with three inputs and output
# arguments passed by value
print("-> Function with inputs and output")
var_by_value = "third"
ret = f_with_inputs_output("first", "second", var_by_value)
print("third variable value is still the same: " + var_by_value)
print("return value: " + ret.title())
print("")

# call function with one input and no output
# the list is passed by reference
# classes as passed by reference
print("-> Function with list passed by reference")
animals = ['duck', 'dog', 'cat']
f_with_lists(animals)
print(animals) #the second element has changed
print("")

# call function with n inputs and no output
# the list is passed by valued
print("-> Function with list passed by value")
animals = ['duck', 'dog', 'cat']
f_with_lists(animals[:])
print(animals) #the second element hasn't changed
print("")

print("-> Function with ellipse")
# call function with n inputs and no output using ellipse
f_with_ellipse('duck', 'dog', 'cat')

