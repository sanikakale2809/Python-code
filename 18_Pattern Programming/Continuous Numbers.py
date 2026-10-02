# 1
# 23
# 456
# 78910


# Outer loop controls the rows
for i in range(1, 5):

    # Inner loop controls numbers in each row
    for j in range(i):
        print(i, end="")

        # Increase number after printing
        i= i + 1

    # Move to the next line
    print()