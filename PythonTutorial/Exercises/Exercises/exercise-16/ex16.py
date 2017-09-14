# Exercise 16: Reading and Writing Files

from sys import argv

script, fileName = argv

# Print a line
print("We're going to erase %r." %fileName)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("? ")

# Open the file
print("Opening the file...")
target = open(fileName, 'w')

print("Truncating the file. Goodbye!")
# truncate method helps shorten the file's size
target.truncate()

print("Now I'm going to ask you for three lines.")
# Here're three inputs
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# write method helps you put these inputs into file.
target.write("%r\n%r\n%r" % (line1, line2, line3))

print("And finally, we close it.")
# close the file
target.close()