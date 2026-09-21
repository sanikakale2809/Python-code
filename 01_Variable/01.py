#Data Type
print("  -------------------Text datatype (str)---------------------")
name="Sanika"
print(name)
print(type(name))

s1="My name is Sanika"
print(s1)
print(type(s1))

grade="A"
print(grade)
print(type(grade))

pwd="abcd@123"
print(pwd)
print(type(pwd))

s2="1234"
print(s2)
print(type(s2))

student = Result("Ethan Hunt", 101)

print("Name:", student.name)
print("Roll No:", student.roll_no)

student.marks(80, 90, 70)
student.calculate_total()
student.calculate_percentage()