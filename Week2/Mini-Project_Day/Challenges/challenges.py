# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.


def add_item(some_list,index,item):
    some_list.insert(index,item)
    return some_list
    
my_list = ['orange','mellon','lemon']
add_item(my_list,0,'peach')
print(my_list)

# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.

def spaces(some_sentence):
    counter = 0
    for x in some_sentence:
        if x == ' ':
            counter += 1
    return counter

sapces_number = spaces('Hello my name is Vlada')
print('Number of spaces:',sapces_number)

# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.

def words(sentence2):
    lower_case = 0
    upper_case = 0
    for x in sentence2:
        if x.isupper():
            upper_case+=1
        elif x.islower():
            lower_case+=1
        else:
            continue
    return upper_case,lower_case,

words2 = words('This Is a SentenCe')
print(words2)


# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:

#     >>>my_sum([1,5,4,2])
#     >>>12

def sum(numbers):
    sum_of_numbers = 0
    for x in numbers:
        sum_of_numbers += x
    
    return sum_of_numbers
        
        
main_sum = sum([1,5,4,2])
print(main_sum)