# Study drill for exercise 16
# Remember enter the name of file correctly

from sys import argv
script, fileName = argv

# Open a file
txt = open(fileName)

# Read a file
print("Here is %r." %fileName)
print(txt.read())