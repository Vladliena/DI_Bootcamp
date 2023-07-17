# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]


user_input = input("Tell me a number and a lenght separated by coma - ")
user_input = user_input.split(",")
i = 0
multiply_list = []

while i < int(user_input[-1]):
    multiply_list.append(int(user_input[0]) * (i + 1))
    i += 1

print(multiply_list)

# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).


user_word = input("Tell me a word")
final_string = ""

for i in user_word:
    if final_string == "" or i not in final_string[-1]:
        final_string += i

print(final_string)
