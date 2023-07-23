# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.

class Farm:
    def __init__(self,farm_name):
        self.name = farm_name
        self.animals = {}
    
    def add_animal(self,animal,number=1):
        if animal in self.animals:
            self.animals[animal] += number
        else:    
            self.animals[animal] = number
        return(self.animals)
    
    def get_info(self):
        print (f'{self.name}s farm\n')
        for animal,number in self.animals.items():
            print (f'{animal}:{number}')
        print() #I added this ptint() to create an empty line (space between list of animals and 'E-I-E-I-0!')
        print('E-I-E-I-0!')
            
    def get_animal_type(self):
        sorted_list = sorted(self.animals)
        return sorted_list
    
    def get_short_info(self,animals):
        animals_txt = ' '.join(animals)
        return print(f'McDonalds farm has {animals_txt}.')
        
        
new_animal = Farm('McDonald')
new_animal.add_animal('cow',5)
new_animal.add_animal('sheep')
new_animal.add_animal('sheep')
new_animal.add_animal('goat',12)
new_animal.get_info()
sorted_list = new_animal.get_animal_type()
print(sorted_list)
new_animal.get_short_info(sorted_list)



        
        