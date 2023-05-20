




# %% bottom right corner triagle with sides of n:
n = int(input("Enter a positive number: "))
while n <= 0:
    n = int(input("Enter a POSITIVE number: "))


for i in range(1, n + 1):
    for j in range(1, n + 1):
            if j <= n - i:
                print(" ", end = " ")
            else:
                print("*", end = " ")
    print()