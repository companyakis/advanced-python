# Base class

class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def info(self):
        print("I'm an animal")

# look at the info methods!

class Cat(Animal):
    def __init__(self, name: str, sound: str, greet: str):
        super().__init__(name, sound)
        self.greet = greet
        
    def info(self):
        print("I'm a cat")
    
class Bird(Animal):
    def __init__(self, name: str, sound: str, greet: str):
        super().__init__(name, sound)
        self.greet = greet

    def info(self):
        print("I'm a bird")

# Create instances 

sylvester = Cat("Sylvester", "Sufferin' succotash! I'm pretty awethome!", "Hi there...")

tweety = Bird("Tweety", "I Tawt I Taw a Puddy Tat!", "Hello!")

# Call the methods

sylvester.info()

tweety.info()

# I'm a cat
# I'm a bird
