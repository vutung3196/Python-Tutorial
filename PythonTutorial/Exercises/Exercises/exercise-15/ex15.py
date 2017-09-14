# Exercise 15: Reading Files

from sys import argv

script, fileName = argv

# Open a file
txt = open(fileName)

print("Here's your file %r:" % fileName)
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

# Open a file
txt_again = open(file_again)

print(txt_again.read())

# Close opened file
txt_again.close()