# 🌟 Exercise 1 : Pets
# Instructions
# Using this code:

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self,sounds):
        return f'{sounds}'
        
        
bengal = Bengal('Tom',4,)
print(bengal.sing('Meaaw'))
chartreux = Chartreux('Hugo',8)
print(chartreux.sing('Meaaaaaaaaaaw'))
siamese = Siamese('Lola',3)
print(siamese.sing('Mew'))

all_cats = [bengal,chartreux,siamese]

sara_pets = Pets(all_cats)
sara_pets.walk()

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.


class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark (self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        return self.weight / self.age*10
    
    def fight(self,other_dog):
        self_run_speed_weight = self.run_speed() * self.weight
        other_run_speed_weight = other_dog.run_speed() * other_dog.weight
        if self_run_speed_weight > other_run_speed_weight:
            print(f'{self.name} win')
        elif other_run_speed_weight > self_run_speed_weight:
            print(f'{other_dog.name} win')
        else:
            print('No one win')
            
dog1 = Dog('Sam',5,4)
dog2 = Dog('Rex',5,6)
dog3 = Dog('Lola',8,10)

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(f'{dog1.name} speed:',dog1.run_speed())
print(f'{dog2.name} speed:',dog2.run_speed())
print(f'{dog3.name} speed:',dog3.run_speed())



dog1.fight(dog2)
dog2.fight(dog1)
dog3.fight(dog2)


# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.

