#Single Inheritance
# Create a class Animal with a method eat() that prints "Animal is eating".
# Create a class Dog that inherits from Animal and has a method bark() that prints "Dog is barking".
# Create a Dog object and call both methods.

# Create a class
#Parent clss
class Animal:
    # Create a method
    def eat(self):
        print("Animal is eating")
#child class
class dog(Animal):
    def bark(self):
        print("Dog is barking")


d1=dog()
d1.eat()
d1.bark()



#Create a class Person with a variable:
# name = "Rahul"
# Create a class Student that inherits from Person.
# Print the name variable using the Student object.

# Create the Person class with the name variable
class Person:
    name = "Rahul"

# Create the Student class that inherits from Person
class Student(Person):
    pass

# Create an object of the Student class
student_obj = Student()

# Print the name variable using the Student object
print(student_obj.name)
