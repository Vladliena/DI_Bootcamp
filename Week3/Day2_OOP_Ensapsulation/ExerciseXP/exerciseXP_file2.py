from exerciseXP import Dog
import random

# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

class PetDog(Dog):
    def __int__(self,name,age,weight):
        super().__init__(name,age,weight)
        self.trained = False
        
    def train(self):
        print(self.bark())
        self.trained = True
        
    def play(self,*dog_names):
        dog_names = ','.join(dog_names)
        print(f'{self.name},{dog_names} all play together')
        
    def do_a_trick(self):
        if self.trained:
         tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
        print(random.choice(tricks))
        
        
dog4 = PetDog('Lili',4,8)
dog4.train()
dog4.play('Ken','Boby','Tesha')
dog4.do_a_trick()