# Ex.4 - Variables and Names
# - Write a comment above each line explaining to yourself in English what it doesç
# - Read the .py file backwardç
# - Read the .py file out loud, saying even the characters
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are",cars,"cars avaiable.")
print("There are only",drivers,"drivers avaiable.")
print("There will be",cars_not_driven,"Empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,
    "in each car.")
