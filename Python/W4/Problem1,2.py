# %% Problem 1:
from random import randint
n1 = randint(50, 100)
n2 = randint(200, 300)

for num in range(n1, n2 + 1):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    if isPrime == True:
        print(num, end = " ")

            
# %% Problem 2:

n1 = randint(50, 100)
n2 = randint(200, 300)

for num in range(n1, n2 + 1):
    Composite = False
    for i in range(2, num):
        if num % i == 0:
            Composite = True
            break
    if Composite:
        print(num, end = " ")
