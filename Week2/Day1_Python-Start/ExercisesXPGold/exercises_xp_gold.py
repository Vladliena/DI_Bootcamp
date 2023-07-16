# Exercise 1 : Hello World-I Love Python
# Instructions
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python


print(('Hello World\n')*4 + ('I love Python\n')*4)

# Exercise 2 : What Is The Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)



month = int(input("Tell me the number of the month"))

if 3 <= month <= 5:
    print('It is spring')
elif 6 <= month <= 8:
    print('It is Summer')
elif 9 <= month <= 11:
    print('It is Autumn')
else:
    print('Its Winter')


