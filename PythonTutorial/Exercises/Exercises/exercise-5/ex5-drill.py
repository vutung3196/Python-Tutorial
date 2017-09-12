# Study drill for exercise 5

name = 'Zed A. Shaw'
age = 35 # not a lie;
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inch = 2.54 #centimetre
lbs = 0.453592 #kg
weightKg = weight * lbs
heightCm = height * inch

print(f"Let's talk about {name}.")
print(f"He's {height} inches or {heightCm} centimetres tall.")
print(f"He's {weight} pounds or {weightKg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right

total = age + height + weight
print(f"If I add {age}, {height}, {weight} I get {total}.")