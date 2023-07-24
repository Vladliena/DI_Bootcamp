# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]


# 2. Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.


class Family:
    def __init__(self,last_name):
        self.members = []
        self.last_name = last_name
        
    def add_members(self,name,age,gender,is_child):
        self.members.append({
            'name':name,
            'age':age,
            'gender':gender,
            'is_child':is_child
        })
        
    def born(self,**child):
        self.members.append(child)
        print(f'Congratulations! You have a baby')
        
    def if_18(self,member_name):
        for member in self.members:
            if member['name'] == member_name:
                if member['age'] >= 18:
                    member['is_child'] = False
                else:
                    member['is_child'] = True
                    
    def family_presentation(self):
        first_names = [member['name'] for member in self.members]
        string_names = ','.join(first_names)
        print(f'{self.last_name} members: {string_names}')
                    
                
        
        
milner_family = Family('Milner')
milner_family.add_members('Michael',35,'Male',False)
milner_family.add_members('Sarah',32,'Female',False)
milner_family.born(name='Ken',age=0,gender='Male',is_child=True)
milner_family.if_18('Sarah')
milner_family.family_presentation()


# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.

# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# Add a method called incredible_presentation which :

# Prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method)
# Prints all the members’ incredible name and power.

# Call the incredible_presentation method.


# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


# Call the incredible_presentation method again.

class TheIncredibles(Family):
    def __init__(self,last_name):
       super().__init__(last_name)
       
    def add_powers_and_supernames(self,family_info,power,super_name):
        name = family_info['name']
        age = family_info['age']
        gender = family_info['gender']
        is_child = family_info['is_child']
        super().add_members(name,age,gender,is_child)
        self.members[-1]['power'] = power
        self.members[-1]['incredible_name'] = super_name
        
    def use_power(self):
        for member in self.members:
            if member['age'] > 18:
                print(member['power'])
    
    def incredible_presentation(self):
        super().family_presentation()
        for member in self.members:
         print(f"{member['power']},{member['incredible_name']}")
    
        

super_family = TheIncredibles('Milner')
super_family.add_powers_and_supernames(milner_family.members[0],'fly','MikeFly')
super_family.use_power()
super_family.incredible_presentation()
super_family.born(name='Jack',age=1,gender='Male',is_child=True,power="Unknown Power",incredible_name = 'unknown')
super_family.incredible_presentation()
