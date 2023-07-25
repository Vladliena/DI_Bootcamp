# 🌟 Exercise 1: Currencies
# Instructions


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    # Your code starts here

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.amount + other
        if self.currency == other.currency:
            return self.amount + other.amount
        # else:
        #     raise TypeError ('You cant add to different currencies')

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
            return self
        if self.currency == other.currency:
            self.amount += other.amount
            return self
        else:
            print("You cant add it")


c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)

print(c1)

c1 += 5
print(c1)

c1 += c2
print(c1)

c1 + c3
print(c1)


# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>


# 🌟 Exercise 3: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

import random


def random_num(some_number):
    integer1 = random.randint(1, 10)
    if some_number == integer1:
        print("Its the same number")
    else:
        print("Not the same number")


random_num(8)

# 🌟 Exercise 4: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import string


def string_generator(size=5, chars=string.ascii_uppercase + string.ascii_lowercase):
    return "".join(random.choice(chars) for ch in range(size))


string_new = string_generator()
print(string_new)

# 🌟 Exercise 5 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

import datetime

current_time = datetime.datetime.now()
print(
    f"Year: {current_time.year}, Month: {current_time.month}, Day: {current_time.day}"
)

# Exercise 6 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).


def until_1st(until_date):
    result = until_date - datetime.date.today()
    print(f"1st of January is in {result}")


until_1st(datetime.date(2024, 1, 1))

# Exercise 7 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

from datetime import datetime


def calculate_lived_minutes(birthdate):
    birthdate_datetime = datetime.strptime(birthdate, "%Y-%m-%d")

    current_datetime = datetime.now()

    time_difference = current_datetime - birthdate_datetime

    lived_minutes = time_difference.total_seconds() / 60

    print(int(lived_minutes))


calculate_lived_minutes("1993-07-14")

# Exercise 8 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

from faker import Faker
fake = Faker()

users = []

def fake_list():
    for i in range(0,3):
     user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
     users.append(user)

fake_list()
print(users)

    

