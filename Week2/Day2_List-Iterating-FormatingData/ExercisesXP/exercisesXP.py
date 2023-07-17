# Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {3, 6, 9, 14}
my_fav_numbers.add(8)
my_fav_numbers.add(13)
# my_fav_numbers.remove(14)
# friend_fav_numbers = {2, 4, 12, 10}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# or option 2
my_fav_numbers = list(my_fav_numbers)[:-1]
friend_fav_numbers = {2, 4, 12, 10}
our_fav_numbers = set(my_fav_numbers).union(friend_fav_numbers)
print(our_fav_numbers)


# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

my_tuple = (4, 6, 8)  # no because tuple is immutable collection of items


# Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.pop()
basket.append("Kiwi")
basket.insert(0, "Apples")
number_of_apples = basket.count("Apples")
print(basket)
print("Number of apples in basket:", number_of_apples)
basket.clear()
print(basket)


# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence)

start = 1.5
step = 0.5
end = 5

list = []

while start <= end:
    list.append(start)
    start += step
    if start % 1 == 0:
        start = int(start)

print(list)


# Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

number_list = range(1, 21)

for i in number_list:
    print(i)
    if number_list.index(i) % 2 == 0:
        print(f"this {i} index is even")


# Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

active = True

while active:
    user_input = input("Tell me your name")
    if user_input == "Vladlena":
        active = False


# Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

user_fruits = input("Tell me your favorite fruits, separate in with space")
fruits_list = user_fruits.split(" ")
name_a_fruit = input("Tell me a name of a fruit")
if name_a_fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")


# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).


topping_price = 2.5
toppings = []
pizza_price = 10

while True:
    user_input = input("Tell me your favorite topping")
    if user_input == "quit":
        print(f"Your pizza with {' '.join(toppings)} costs: ${pizza_price}")
        break
    else:
        print("I will add this topping to your pizza")
        pizza_price += topping_price
        toppings.append(user_input)


# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.


total = 0
while True:
    user_input = int(
        input("What is your age?\n P.S.If you dont need a ticket write 0 - ")
    )
    if user_input == 0:
        print(f"Your total price: ${total}")
        break
    else:
        if user_input < 3:
            total += 0
        if 3 <= user_input <= 12:
            total += 10
        if user_input > 12:
            total += 15

teenagers = ["Alex", "Sam", "Glen"]

for i in teenagers.copy():
    age = int(input(f"{i} tell me your age - "))
    if 16 <= age <= 21:
        teenagers.remove(i)

print(teenagers)

# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

finished_sandwiches = []

sandwich_orders = [
    "Tuna sandwich",
    "Pastrami sandwich",
    "Avocado sandwich",
    "Pastrami sandwich",
    "Egg sandwich",
    "Chicken sandwich",
    "Pastrami sandwich",
]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich}")
