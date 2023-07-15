# Exercise 1

print(("Hello world\n") * 4)

# Exercise 2

print((99**3) * 8)

# Exercise 3

5 < 3 #false
3 == 3 #true
3 == "3" #false
"3" > 3 #error
"Hello" == "hello" #false

# Exercise 4

computer_brand = "acer nitro 5"
print("I have a {} computer".format(computer_brand))

# Exercise 5

name = "Vladlena"
age = 30
shoe_size = 38.5

info = "My name is {}, 2 days ago I turned {} and my feet size is {} which is not very common and hard to find".format(
    name, age, shoe_size
)
print(info)

info_option2 = f"My name is {name}, 2 days ago I turned {age} and my shoe size is {shoe_size} which is not very common and hard to find"
print(info_option2)

# Exercise 6

a = 10
b = 5

if a > b:
    print("Hello World")

# Exercise 7

number = int(input("write any number"))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")

# Exercise 8

name = input('Tell me your name')

if name == 'Vladlena':
    print ('wow! we have the same name')
else:
    print('my name is prettier')

# Exercise 9

height = int(input("tell me your height in inches"))
if height > 145:
    print('you are tall enough to ride')
else:
    print('you need to grow more to ride')