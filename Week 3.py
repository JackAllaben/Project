#Programmer: Jack Allaben
#Date: 9/22

#Week 3 Programming Project

#Program 2

infant = 1
Child = 13
Teenager = 20

age = int(input("How Old Are You? "))

if age > Teenager:
    print('Adult')
elif age > Child:
    print('Teenager')
elif age > infant:
    print('Child')
elif age >= 0:
    print('Infant')
else:
    print('Invalid Entry')


print(' ')
#Program 3
import random

# Generate a random weight between 0.10 and 50.00 pounds
weight = (random.uniform(0.10, 50.00))

# Define shipping rates
rate1 = 1.50
rate2 = 3.00
rate3 = 4.00
rate4 = 4.75

# Calculate shipping cost based on weight
if weight <= 2.0:
    shipping_cost = (weight * rate1)
elif weight <= 6.0:
    shipping_cost = (weight * rate2)
elif weight <= 10.0:
    shipping_cost = (weight * rate3)
else:
    shipping_cost = (weight * rate4)

print(f"The weight of the item is {weight} pounds.")
print(f"The shipping cost is ${shipping_cost:.2f}")

print(' ')
#Program 5
hot_dog_preference = input('Do You Want a Hot Dog or Chili Dog? ')
if hot_dog_preference == 'Hot Dog':
    hot_dog_price = 3.5
elif hot_dog_preference == 'Chili Dog':
    hot_dog_price = 4.5
else:
    print('Invalid Entry')

cheese = input('Do You Want Cheese? ')
if cheese == 'Yes':
    cheese_price = .5
else:
    cheese_price = 0

peppers = input('Do You Want Peppers? ')
if peppers == 'Yes':
    peppers_price = .75
else:
    peppers_price = 0

onions = input('Do You Want Grilled Onions? ')
if onions == 'Yes':
    onions_price = 1
else:
    onions_price = 0

Subtotal = hot_dog_price + cheese_price + peppers_price + onions_price
print(f'The subtotal is: ${Subtotal:.2f}')

Tax = Subtotal*.07
print(f'Tax: ${Tax:.2f}')

Total = Subtotal + Tax
print(f'Total Price: ${Total:.2f}')


