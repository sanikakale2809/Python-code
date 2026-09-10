# Create:
# Father
# Mother
#    ↓
# Child
# Father should have method father_skill().
# Mother should have method mother_skill().
# Child should inherit from both and have child_skill().
# Call all three methods.



class Father :
    def father_skill(self):
        print("father_skill")

class Mother:
    def mother_skill(self):
        print("mother_skill")

class Child(Father,Mother):
    def child_skill(self):
        print("child_skill")



c=Child()
c.mother_skill()
c.father_skill()
c.mother_skill()



# Multiple Inheritance + Same Method
# Create two classes:
# class A:
#     def show():
#         print("A")
# and
# class B:
#     def show():
#         print("B")
# Create class C(A, B).
# Call show() using the C object

class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")


class C(A,B):
    pass



XYZ=C()
XYZ.show()

