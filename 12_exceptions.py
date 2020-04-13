# catch division-by-0 exception
print("-> ZeroDivisionError exception")
a = 10
b = 0
try:
    div = a/b
except ZeroDivisionError:
    print("Division by 0");
else:
    print("The result is " + str(div))

# don't do anything when the exception is caught
# pass is needed because Python need at least an instruction in that code block
print("-> ZeroDivisionError exception")
try:
    div = a/b
except ZeroDivisionError:
    pass
else:
    print("The result is " + str(div))

# catch exception due to non-existing file 
print("-> NotExistingFile exception")
try:
    with open("NotExistingFile.txt") as fobj:
        cnt = fobj.read()
except EnvironmentError as err:
    print("Error code: " + str(err.errno))
else:
    print("File content: " + cnt)

