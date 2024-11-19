# Base class

class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says '{self.sound}'")

# Subclasses: Cat and Bird

class Cat(Animal):
    def __init__(self, name: str, sound: str, greet: str):
        super().__init__(name, sound)
        self.greet = greet
        
    def cat_says(self):
        print(f"{self.name} says '{self.greet}'")
    
class Bird(Animal):
    def __init__(self, name: str, sound: str, greet: str):
        super().__init__(name, sound)
        self.greet = greet

    def bird_says(self):
        print(f"{self.name} says '{self.greet}'")
