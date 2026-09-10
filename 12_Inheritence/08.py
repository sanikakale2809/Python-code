# Method Overriding
# Create a parent class Animal with:
# sound()
# that prints "Animal makes sound".
# Create a child class Dog that overrides sound() and prints "Dog barks".
# Call sound() using a Dog object.


class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


d=Dog()
d.sound()
d.sound()


#Constructor + super()
# Create a parent class Person with a constructor accepting name.
# Create a child class Student with a constructor accepting name and roll_no.
# Use super() to call the parent constructor.
# Print both values.


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        # Use super() to call the parent class constructor
        super().__init__(name)
        self.roll_no = roll_no

    def display_info(self):
        print(self.name)
        print(self.roll_no)

# Create a Student object and print values
student = Student("Sanika Kale", 52)
student.display_info()
