# Exercise 29: What If

people = 20
cats = 30
dogs = 15
birds = 10

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry")


dogs += 5

if people >= dogs:
    print("People are greate than or equal to dogs.")

if people <= dogs:
    print("People are less then or equal to dogs.")

if people == dogs:
    print("People are dogs.")

# Add other boolean expression
if people != birds:
    print("The number of people is different from the number of birds")
