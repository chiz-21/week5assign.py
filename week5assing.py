# Activity 1

# Base class: Smartphone
class Smartphone:
    brand = "Samsung"  # Class variable for the brand of the smartphone
    model = "Galaxy S21"  # Class variable for the model of the smartphone
    storage = "128GB"  # Class variable for the storage capacity of the smartphone

    # Constructor method to initialize instance variables
    def __init__(self, brand, model, storage):
        self.brand = brand  # Brand of the smartphone
        self.model = model  # Model of the smartphone
        self.storage = storage  # Storage capacity of the smartphone

    # Method to display the smartphone's details
    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}")

# Creating an instance of the Smartphone class
my_smartphone = Smartphone("Samsung", "Galaxy S21", "128GB")
my_smartphone.display_details()  # Calling the display_details method to show the smartphone's details

# Subclass: TecnoSmartphone (inherits from Smartphone)
class TecnoSmartphone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)  # Call the parent constructor
        self.cooling_system = cooling_system  # Assign cooling system from argument

    # Overriding a method to showcase polymorphism
    def display_details(self):
        super().display_details()  # Call the parent method
        print(f"Cooling System: {self.cooling_system}")  # Display additional attribute

# Creating instances
phone1 = Smartphone("Samsung", "Galaxy S21", "128GB")
phone2 = TecnoSmartphone("Tecno", "Camon", "64GB", "Liquid cooling")

# Displaying details of the smartphones
print("\nSmartphone Details:")
phone1.display_details()

print("\nTecno Smartphone Details:")
phone2.display_details()

# Activity 2
# Base class: Animal
class Animal:
    def move(self):
        pass  # A generic move method
class Cat(Animal):
    def move(self):
        print("The cat is walking gracefully. 🐈")
class Dog(Animal):
    def move(self):
        print("The dog is running excitedly. 🐕")
class Snake(Animal):
    def move(self):
        print("The snake is slithering smoothly. 🐍")

# Creating instances
animals = [Cat(), Dog(), Snake()]

# Demonstrating polymorphism
for animal in animals:
    animal.move()  # Calling the move method of each animal object



