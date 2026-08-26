# Salary bonus and calculate it
salary=float(input("Enter your salary="))
if salary < 20000:
    bonus_rate=0.10
    print("10% bonus")
elif salary > 20000 and salary < 50000:
    bonus_rate=0.7
    print("7% bonus")
elif salary > 50000:
    bonus_rate=0.5
    print("7% bonus")

    bonus=salary*bonus_rate
    final_salary=salary+bonus
    print(f"Bonus: {bonus:2f}")
    print(f"Total Salary: {final_salary:2f}")
