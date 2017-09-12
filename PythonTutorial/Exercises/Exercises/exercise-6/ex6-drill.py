# Study drill for exercise 6

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # String is put inside a string

print(x)
print(y)

print(f"I said: {x}") # String is put inside a string
print(f"I also said: '{y}'") # String is put inside a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) 

w = "This is the left side of..."
e = "a string with a right side"

print(w + e) # new string is the combination of string w and string e