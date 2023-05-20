


# %% Multiplication table:
n = int(input("Enter a positive number: "))
while n <= 0:
    n = int(input("Enter a POSITIVE number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i>j:
            print("" * i, end = "\t")
        else:
            print(j * i, end = "\t")
    print()
        