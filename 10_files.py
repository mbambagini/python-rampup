filename = 'temp.txt'

# write messages to a file
with open(filename, 'w') as fobj:
    for i in range(1,5):
        fobj.write("Hello world!\n")

# append messages to a file
with open(filename, 'a') as fobj:
    for i in range(1,3):
        fobj.write("More greetings!\n")

# read the whole file content
with open(filename) as fobj:
    full_content = fobj.read()
    print(full_content)

# read lines from a file
with open(filename) as fobj:
    for line in fobj:
        print(line.rstrip())

