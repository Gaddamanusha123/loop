#BY Using the While Loop
#Task 1 : Find the second prime of the given number ?

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

num = int(input("Enter a number: "))
n = num + 1
count = 0
while True:
    if is_prime(n):
        count += 1
        if count == 2:
            print("The second prime number after", num, "is:", n)
            break
    n += 1



#By using break control statement
#Task 2 : Break the loop if  Condition matches with the given number?
for i in range(1,21,1):
    if i==15:
        break
    print(i)
    
    
  #By using the continue control statement
 #Task 3 : print the numbers from 1 to 100, but it should not print multiples of 3

for i in range(1,101,1):
    if i%3==0:
        continue
    print(i)