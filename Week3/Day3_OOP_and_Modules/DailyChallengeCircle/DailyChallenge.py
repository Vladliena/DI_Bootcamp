# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together - use a dunder method
# Be able to compare two circles to see which is bigger - use a dunder method
# Be able to compare two circles and see if there are equal - use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

import math

class Circle:
    
    list_of_circles = []
    
    def __init__(self,radius):
        self.radius = radius
        self.diameter = 0
    
    def diameter_find(self):
        self.diameter += 2 * self.radius
        return self.diameter
    
    def __str__(self):
        return f'circle radius = {self.radius}, circle diameter = {self.diameter}'
    
    def area(self):
        return math.pi * self.radius**2
    
    def __add__(self,other_circle):
        return self.radius + other_circle.radius
    
    def __gt__(self,other_circle):
        if self.radius > other_circle.radius:
            return 'circle 1 is bigger'
        else:
            return "circle 2 is bigger"
        
    def __eq__(self,other_circle):
        if self.radius == other_circle.radius:
            return True
        else:
            return False
    
    @classmethod
    def add_to_list(cls, circle):
        if isinstance(circle, Circle):
            cls.list_of_circles.append(str(circle.radius))
    
    @classmethod        
    def sorted(cls):
        cls.list_of_circles = sorted(cls.list_of_circles)
    
            
    
c1 = Circle(10)
c2 = Circle(6)
c1.diameter_find()
c2.diameter_find()
print('Circle area: ',c1.area())
print('Circle area: ',c2.area())
c3 = c1 + c2
print('Two circles added together: ',c3)
print(c1>c2)
Circle.add_to_list(c1)
Circle.add_to_list(c2)

print(Circle.list_of_circles)
Circle.sorted()
print(Circle.list_of_circles)
