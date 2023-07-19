import random

# # Exercise 1 : What Are You Learning ?
# # Instructions
# # Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# # Call the function, and make sure the message displays correctly.


# def display_message():
#     return print("Im learning Python in Developers Institute")


# display_message()

# # 🌟 Exercise 2: What’s Your Favorite Book ?
# # Instructions
# # Write a function called favorite_book() that accepts one parameter called title.
# # The function should print a message, such as "One of my favorite books is <title>".
# # For example: “One of my favorite books is Alice in Wonderland”
# # Call the function, make sure to include a book title as an argument when calling the function.


# def favorite_book(title):
#     return print(f"One of my favorite books is {title}")


# favorite_book("Harry Potter")

# # Exercise 3 : Some Geography
# # Instructions
# # Write a function called describe_city() that accepts the name of a city and its country as parameters.
# # The function should print a simple sentence, such as "<city> is in <country>".
# # For example “Reykjavik is in Iceland”
# # Give the country parameter a default value.
# # Call your function.


# def describe_city(city, country="Ukraine"):
#     return print(f"{city} is a capital of {country}")


# describe_city("Kyiv")

# # Exercise 4 : Random
# # Instructions
# # Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# # Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.


# def randomizer(n):
#     randon_number = random.randint(1, 100)
#     if n == randon_number:
#         return print("Its the same number!")
#     else:
#         return print(f"{n} and {randon_number} are not the same!")


# randomizer(55)

# # 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# # Instructions
# # Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# # The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# # Call the function make_shirt().

# # Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# # Make a large shirt with the default message
# # Make medium shirt with the default message
# # Make a shirt of any size with a different message.

# # Bonus: Call the function make_shirt() using keyword arguments.


# def make_shirt(size="L", message="I love Python"):
#     return print(f"The size of the shirt is {size} and the text is {message}")


# make_shirt("M", "I love codding")
# make_shirt()
# make_shirt("M")
# make_shirt("S", "I love cats")
# make_shirt(size="XL", message="I love dogs")

# # 🌟 Exercise 6 : Magicians …
# # Instructions
# # Using this list of magician’s names

# # magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# # Create a function called show_magicians(), which prints the name of each magician in the list.
# # Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# # Call the function make_great().
# # Call the function show_magicians() to see that the list has actually been modified.


# magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]


# def show_magicians():
#     for i in magician_names:
#         print(i)


# show_magicians()


# def make_great(some_list):
#     for i in range(len(some_list)):
#         some_list[i] = f"the Great {some_list[i]}"
#     return some_list


# make_great(magician_names)
# show_magicians()


# # Exercise 7 : Temperature Advice
# # Instructions
# # Create a function called get_random_temp().
# # This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# # Test your function to make sure it generates expected results.

# # Create a function called main().
# # Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# # Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# # Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# # below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# # between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# # between 16 and 23
# # between 24 and 32
# # between 32 and 40

# # Change the get_random_temp() function:
# # Add a parameter to the function, named ‘season’.
# # Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# # Now that we’ve changed get_random_temp(), let’s change the main() function:
# # Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# # Use the season as an argument when calling get_random_temp().

# # Bonus: Give the temperature as a floating-point number instead of an integer.
# # Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.


# def get_random_temp(season):
#     if 9 <= season <= 12 or 1 <= season <= 2:
#         degree = round(random.uniform(-10, 16), 1)
#         return degree
#     elif 3 <= season <= 8:
#         degree = round(random.uniform(16, 40), 1)
#         return degree


# def main():
#     main_degree = get_random_temp(int(input("Write me the number of the month: ")))
#     print(f"The temperature right now is {main_degree} degrees Celsius.")
#     if main_degree <= 0:
#         print(f"Brrr, thats freezing! Wear some extra layers today")
#     elif 0 <= main_degree <= 16:
#         print(f"Quite chilly! Don’t forget your coat")
#     elif 16 <= main_degree <= 23:
#         print(f"Such a good weather!")
#     elif 24 <= main_degree <= 32:
#         print(f"Ok...its quite hot outside")
#     else:
#         print(f"We are in hell D:")


# main()

# Exercise 5 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"},
]


def score(a,b,c):
    return print(
        f"List of is your wrong answers: {c}\n Number of incorect unswers: {a}\n Number of correct answers {b}"
    )


def game(some_data):
    incorrect_answers = 0
    correct_answers = 0
    wrong_answers = []
    for i in range(len(some_data)):
        answer = input(some_data[i]["question"])
        if answer != some_data[i]["answer"]:
            print("You are wrong")
            wrong_answers.append(answer)
            incorrect_answers += 1
        else:
            print("You are right!")
            correct_answers += 1
    return score(incorrect_answers,correct_answers,wrong_answers)


game(data)
