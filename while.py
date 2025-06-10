# Python Program: Print Factors using while loop

num = int(input("Enter a number: "))
i = 1

print(f"Factors of {num} are:")
while i <= num:
    if num % i == 0:
        print(i, end=' ')
    i += 1

print("Multiplication tables from 1 to 5 (only even multipliers):")

for i in range(1, 6):  # Tables from 1 to 5
    print(f"\nTable of {i}:")
    for j in range(2, 21, 2):  # Even numbers from 2 to 20
        print(f"{i} x {j} = {i * j}")




