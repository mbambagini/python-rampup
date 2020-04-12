# catch division-by-0 exception
a = 10
b = 0
try:
    div = a/b
except ZeroDivisionError:
    print("Division by 0");
else:
    print("The result is " + str(div))

# don't do anything when the exception is caught
try:
    div = a/b
except ZeroDivisionError:
    pass
else:
    print("The result is " + str(div))

# catch not-existing-file exception
try:
    with open("NotExistingFile.txt") as fobj:
        cnt = fobj.read()
except EnvironmentError as err:
    print("Error code: " + str(err.errno))
else:
    print("File content: " + cnt)

