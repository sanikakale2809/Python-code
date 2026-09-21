# Lambda function is a small, single line, anonymous function.
def calcsquare(x):
  sq=x**2
  return sq

print("square is ",calcsquare(15))


# lambda parameters:return value
print("------------Print Square---------------")
sq=lambda x:x**2
print('square is ',sq(5))
print(sq(-9))

print("------------Print cube---------------")

cube=lambda x:x**3
print('cube is ',cube(5))


print("------------Print add---------------")
add=lambda a,b:a+b
print(add(4,8))



print("------------Print discount---------------")
d=lambda amount:amount*10/100
print(d(3400))