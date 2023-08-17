# Exam
# Python Basics

# Data Types

# Which of the following is not a mutable data type in Python?
# a) List
# b) Dictionary
# c) Tuple
# d) Set

# Answer - Tuple





# Lists and Loops

# Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.

even_squares = []
for i in range(1, 11):
    if i % 2 == 0:
        even_squares.append(i ** 2) # or (i * i)

print(even_squares)

# Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.

divisible_numbers = []
for num in range(1, 11):
    if num % 2 == 0 and num % 3 == 0:
        divisible_numbers.append(num)

print(divisible_numbers)

# Loop through the provided list of dictionaries and print the names and ages:

student_list = [
    {
        "name": "John",
        "age": 24
    },
    {
        "name": "Anna",
        "age": 22
    },
    {
        "name": "Mike",
        "age": 25
    }
]

for student in student_list:
    print(f"Student name: {student['name']}, Student age: {student['age']}")

# Function Behavior with *args and **kwargs
# Write a function combine_words that accepts any number of positional arguments and key-value arguments. The function should return a single sentence combining all the words provided.

# def combine_words(*args,**kwargs):
#     sentence = ' '.join(args)
#     for value in list(kwargs.values()):
#         sentence += f' {value}'
#     return sentence

# print(combine_words("Hello", "world", second="is", third="great!", first="Python"))

def combine_words(*args,**kwargs):
    sentence = ' '.join(args)
    sorted(kwargs.keys())
    for key,value in sorted(kwargs.items()):
        sentence += f' {value}'
    return sentence

print(combine_words("Hello", "world", second="is", third="great!", first="Python"))


# Object-Oriented Programming (OOP)
# Create a class Vehicle with string attributes type, brand, and integer attribute year. Ensure instances of the vehicle cannot be created if any of these attributes are missing and include a method to display the vehicle’s info. Use dunder method.


class Vehicle:
    def __init__(self, type, brand, year):
        self.type = type
        self.brand = brand
        self.year = year

    def display_info(self):
        return f"{self.type},{self.brand},{self.year}"

    def __str__(self):
        return self.display_info()

vehicle = Vehicle("car", "nissan", 2017)

print(vehicle.display_info())

print(vehicle)

# OOP Inheritance and Decorators

# Create a class Car with string attributes brand, model, and integer attribute mileage. Implement a method to return the car’s details.


# Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity. Override the car’s details method to include the battery capacity.
# Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to modify the battery capacity only if the new value is positive.


# Create a BankAccount class with private float attribute _balance and private string attribute _account_holder. Implement methods to deposit, withdraw, and view the balance. Include a class method to track accounts created and a static method for a bank policy message. Ensure the balance is non-negative.


class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def car_details(self):
        return f"{self.brand},{self.model},{self.mileage}"
    
class ElectricCar(Car):
    def __init__(self,battery_capacity,brand,model,mileage):
        super().__init__(brand,model,mileage)
        self.__battery_capacity = battery_capacity
        
    def car_details(self):
        return f"{Car.brand},{Car.model},{Car.mileage},{self.__battery_capacity}"
    
    @property
    def battery_capacity(self):
        return self.__battery_capacity
    
    @battery_capacity.setter
    def set_battery_capacity(self,new_value):
        if new_value > 0:
            self.__battery_capacity = new_value
    

class BankAccount():
    
    total_accounts = 0
    
    def __init__(self, balance, account_holder):
        self.__balance = balance
        self.__account_holder = account_holder
        BankAccount.total_accounts += account_holder
        
    def deposit(self,new_amount):
        if new_amount > 0:
            self.__balance = new_amount
            
    def withdraw(self, withdraw_amount):
        self.__balance -= withdraw_amount
        
    def view_balance(self):
        return f'Balance: {self.__balance}'
    
    @classmethod
    def total_accounts(cls):
        return cls.total_accounts
    
    @staticmethod
    def policy():
        return f'Our policy is to provide you with exellent service'
    
