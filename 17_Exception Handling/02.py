print("------------------EX 1 ------------------")
try:
    n=int(input("Enter a number:"))

except:
    print("Invalid input")
    n=0

sq=n**2
print(f"Square of {n} is {sq}")



print("------------------EX 2------------------")
try:
  x=int(input('Enter first number '))
  y=int(input('Enter second number '))
  res=x/y
except ValueError:
  res=0
  print('Invalid input')
except ZeroDivisionError:
  res=x
  print('cant divide by zero')

print(f'result of division is {res}')



print("------------------EX 3------------------")
try:
  x=int(input('Enter first number '))
  y=int(input('Enter second number '))
  res=x/y
except:
  res=0
  print('Invalid input or divided by zero')

print(f'result of division is {res}')




print("------------------EX 4------------------")
film={
    "name":"sholay",
    "releaseyear":1975,
    "genre":"action",
    "language":"hindi",
    "actors":["amitabh bachchan","dharmendra","sanjiv kumar"],
    "music":"r d burman",
    "imdbrating":7.9
}
key=input('Enter key : ')
try:
  print(film[key])
except KeyError:
  print(f'information not available for {key}')
finally:
  print('films make our life live')



print("------------------EX 5------------------")
lst=['java','spring','python','data science','machine learning','genai','pandas']
i=int(input('Enter list index : '))
print(lst[i])
try:
  i=int(input('Enter list index : '))
  try:
    print(lst[i])
  except IndexError:
    print('index out of range')
except ValueError:
  print('invalid index...must be a number')


try:
  i=int(input('Enter list index : '))
  try:
    print(lst[i])
  except IndexError:
    print('index out of range')
except ValueError:
  print('invalid index...must be a number')


print("------------------EX 6------------------")
try:
  n=int(input("Enter a number : "))
  if n<0:
    raise ValueError()
except ValueError:
  n=0
  print('Invalid input or a negative number')

sq=n**2
print(f'square of {n} is {sq}')




print("------------------EX 7------------------")
try:
  ps=input('Enter password : ')
  if len(ps)<8:
    raise ValueError()
except ValueError:
  print('invalid password')

print(f"your password is {ps}")
