""" Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation. """

class Developer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
    
    def code(self):
        print(f"{self.name} is coding in {self.language}")
    
    def debug(self):
        print(f"{self.name} is debugging")

    def retire(self):
        print(f"{self.name} will retire in {self.age+50} years old.")

developer = Developer("Kalwenzi", 22, "Python")

class WebDeveloper(Developer):
    def __init__(self, name, age, language, framework):
        super().__init__(name, age, language)  # Call the parent's constructor
        self.framework = framework  # Web developers have a framework

    def code(self):  # Override the parent's code() method
        print(f"{self.name} is coding in {self.language} using {self.framework}")

    def deploy(self, website):
        print(f"{self.name} is deploying {website}")

kalwenzi = Developer("Kalwenzi", 22, "Python")
james = WebDeveloper("James", 28, "JavaScript", "React")


""" Activity 2: Polymorphism Challenge! 🎭
Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️). """

class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves in a general way.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  

    def move(self):
        print(f"{self.name} runs on four legs.")

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)  

    def move(self):
        print(f"{self.name} swims in the water.")

animal = Animal("Any Animal")
dog = Dog("Sonic")
fish = Fish("Spoons")

animal.move()
dog.move()
fish.move()