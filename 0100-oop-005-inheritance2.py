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

# Create instances 

sylvester = Cat("Sylvester", "Sufferin' succotash! I'm pretty awethome!", "Hi there...")

tweety = Bird("Tweety", "I Tawt I Taw a Puddy Tat!", "Hello!")

# Call the methods

sylvester.cat_says()

sylvester.make_sound()

tweety.bird_says()

tweety.make_sound()

# Sylvester says 'Hi there...'
# Sylvester says 'Sufferin' succotash! I'm pretty awethome!'
# Tweety says 'Hello!'
# Tweety says 'I Tawt I Taw a Puddy Tat!'
