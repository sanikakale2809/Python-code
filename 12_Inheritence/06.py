# Child Class Method
# Create a parent class Vehicle with method start().
# Create a child class Car with method drive().
# Create a Car object and call both methods.

class Vehicle:
    def start(self):
        print("vehicle is start")


class Car(Vehicle):
    def drive(self):
        print("car is drive")



c1=Car()
c1.drive()
c1.start()



#Constructor Inheritance
# Create a parent class Person with a constructor that accepts name.
# Create a child class Student that inherits from Person.
# Create a student object with the name "Amit" and print the name.

#Parent class
class Person:
    def __init__(self,name):
        self.name = name


# child class
class Student(Person):
    pass


#creat a object
s=Student("Amit")

# print name
print(s.name)



# Multiple Child Classes
# Create a parent class Animal with method eat().
# Create two child classes:
# Dog
# Cat
# Both should inherit from Animal.
# Call eat() using objects of both classes


class Animal:
    def eat(self):
        print("animal is eating")


class Dog(Animal):
    pass

class Cat(Animal):
    pass


# --- Calling eat() using objects of both classes ---

# Create objects
my_dog = Dog()
my_cat = Cat()

# Call the inherited method
my_dog.eat()  # Output: This animal is eating food.
my_cat.eat()  # Output: This animal is eating food.



