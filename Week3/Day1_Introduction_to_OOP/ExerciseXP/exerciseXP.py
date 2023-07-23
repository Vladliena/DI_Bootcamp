# 🌟 Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self,cat_name,cat_age):
        self.name = cat_name
        self.age = cat_age

cat3 = Cat('Tom',3)
cat1 = Cat('Hugo',22)
cat2 = Cat('Felix',10)


def oldest_cat(cat_list: list[Cat]):
    if len(cat_list) == 0:
        return None

    oldest_cat = cat_list[0]

    for cat in cat_list:
        if cat.age > oldest_cat.age:
            oldest_cat = cat

    return oldest_cat


oldest = oldest_cat([cat1,cat2,cat3])
print(oldest.name)

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


def bigger_dog(dog_list: list[Dog]):
    if len(dog_list) == 0:
        return 0

    bigger_dog = dog_list[0]

    for dog in dog_list:
        if dog.height > bigger_dog.height:
            bigger_dog = dog
    return bigger_dog.name


davids_dogs = Dog(name="Rex", height=50)
davids_dogs.jump()
davids_dogs.bark()
sarahs_dog = Dog(name="Teacup", height=20)
sarahs_dog.jump()
sarahs_dog.bark()
print(bigger_dog([davids_dogs, sarahs_dog]))


# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven


class Song:
    def __init__(self, lyrics=[]):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in range(0, len(self.lyrics)):
            print(self.lyrics[i])


stairway = Song(
    [
        "Theres a lady who's sure",
        "all that glitters is gold",
        "and shes buying a stairway to heaven",
    ]
)
stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, *new_animal):
        for animal in new_animal:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, *animal_sold):
        for animal in animal_sold:
            if animal in self.animals:
                self.animals.remove(animal)

    def sorted_animals(self, animals_list):
        animals_sorted = sorted(animals_list)
        animal_groups = {}
        group = 1
        animal_groups[group] = [animals_sorted[0]]
        for animal in animals_sorted[1:]:
            if animal[0] == animal_groups[group][0][0]:
                animal_groups[group].append(animal)
            else:
                group += 1
                animal_groups[group] = [animal]
        return animal_groups
    def get_groups(self,sorted_animals):
        for key,value in sorted_animals.items():
            print(key,value)
            
        


ramat_gan_safari = Zoo('Ramat Gan Zoo')
ramat_gan_safari.add_animal("Elephant", "Cat", "Panda", "Pantera", "Emo","Rat","Raccon")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Cat")
ramat_gan_safari.get_animals()
sorted_list = ramat_gan_safari.sorted_animals(ramat_gan_safari.animals)
print(sorted_list)
ramat_gan_safari.get_groups(sorted_list)