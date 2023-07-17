import random


# Exercise
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.


some_words = input('Tell me something')
if len(some_words) < 10:
    print('string not long enough')
elif len(some_words) > 10:
    print('string is too long')
elif len(some_words) == 10:
    print('perfect string')

# Then, print the first and last characters of the given text.

print (some_words[0])
print (some_words[-1])

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

for i in range(len(some_words)):
    print(some_words[:i+1])

# Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method).

shuffled_list = ''.join(random.sample(some_words,len(some_words)))
print(shuffled_list)






