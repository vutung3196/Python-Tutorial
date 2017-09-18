# Study drill for exercise 19

def sayHello(name):
    print("Hello %r" % name)
    print("Goodbye.\n")

# Use this function to print one string
sayHello('Tung')

# We can use variable from our script
a = 'Ha'
sayHello(a)

# We can combine variable, and math
sayHello(a + ' and Tung')

# Or you can combine two arguments 
sayHello('Tung' + ' Nhat')

# Call one function in a function
def intro_person(name_first, name_second):
    print("Hi, I'm %r" %name_first)
    sayHello(name_second)

# Remember that this function accepts two arguments 
intro_person('Tung', 'Nhat')

# We can use variables from our script
name_person_1 = 'Tung'
name_person_2 = 'Son'

intro_person('Tung', 'Son')