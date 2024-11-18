"""
A class for representing a circle

radius => property

methods => circle_area and circle_circumference

"""
import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        
    def circle_area(self):
        return self.radius * self.radius * math.pi
    
    def circle_circumference(self):
         print(f"Circumference = {2 * math.pi * self.radius}")
    
# a circle instance

a_circle = Circle(5.6)

print("Area = ", a_circle.circle_area())

a_circle.circle_circumference()

# Area =  98.5203456165759
# Circumference = 35.18583772020568
