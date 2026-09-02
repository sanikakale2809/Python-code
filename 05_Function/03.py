# Factorial
print("--------------------Factorial-----------------------")
def factorial(N):
    fac = 1
    for i in range(1, N + 1):
        fac = fac * i
    print("factorial =", fac)

factorial(5)

# Sum from 1 to n
print("------------------Sum from 1 to n--------------------")
def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


result = sum_n(5)
print(result)


# Sum of even numbers
print("------------------Sum of even numbers--------------------")
def sum_even(n):
    total = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            total = total + i

    return total


result = sum_even(10)
print(result)



# Prime number
print("------------------Check Prime number-----------------")
