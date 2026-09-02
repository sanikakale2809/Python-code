# Area of rectangle
print("-------------------Area of Rectangle------------------")
def area_of_rectangle(l,b):
    area = l*b
    return area
print(area_of_rectangle(3,4))

# perimeter of rectangle
print("--------------------Perimeter of Rectangle------------------")
def perimeter_of_rectangle(l,b):
    perimeter = 2*(l+b)
    return perimeter
print(perimeter_of_rectangle(3,4))


#Calculate percentage
print("--------------------Calculate percentage--------------------")
def cal(a,b,c,d,e):
    per=(a+b+c+d+e)/100
    return per
print(cal(3,4,5,6,7))


#pass or fail
print("--------------------Check result---------------------")
def check_result(marks):
    if marks > 40 :
        return "pass"
    else:
        return "fail"
print(check_result(37))
print(check_result(67))


#largest of three numbers
print("--------------------Largest of three numbers--------------------")
def largest(a,b,c):
    if a > b and a > c :
        return "a is greater number"
    elif b > a and b > c:
        return "b is greater number"
    else:
        return "c is greater number"

print(largest(2,5,8))


# Calculate simple interest
print("--------------Simple Interest-----------------------")
def si(p,r,t):
    simpleinterest=(p*r*t)/100
    return simpleinterest
print(si(2000,5,2))


#Count characters
print("-----------------Count Characters 1---------------------")
def count_characters(s):
    count=0
    for c in s:
        count=count +1
    return count

print(count_characters("Sanika kale"))
print(count_characters("Sanikakale"))

print("-----------------Count Characters 2---------------------")
def count_characters2(s):
    print(len(s))

print(count_characters2("Sanika kale"))
print(count_characters2("Sanikakale"))

# Convert Celsius to Fahrenheit
print("-----------------Celsius to Fahrenheit----------------")
def conversion(tem):
    feh = (tem * 1.8) + 32
    return feh
print(conversion(37))
print(conversion(67))


# Check vowel
print("-----------------Check Vowel--------------------------")
def vowel(s):
    vowel = 'aeiouAEIOU'
    count = 0

    for ch in s:
        if ch in vowel:
            count = count + 1
    return count
print(vowel("hello"))
print(vowel("aeiouAEIOU"))

# Reverse String
print("-----------------Reverse String 1---------------------")
def reverse(s):
    rev=" "
    for ch in s:
        rev = ch + rev
    return rev
print(reverse("Sanika"))

print("---------------Reverse String 2---------------------")
def reverse2(s):
    print(s[::-1])

reverse("sanika")
reverse2("Python")