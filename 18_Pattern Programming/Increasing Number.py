# 1
# 12
# 123
# 1234



for i in range(1, 5):               # Outer loop controls the rows
    for j in range(1, i + 1):       # Inner loop prints numbers from 1 to i
        print(j, end="")
    print()                         # Move to the next line
    