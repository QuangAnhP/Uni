# %% Recursion: factorial

def factorial(n):
    return (n*factorial(n-1)) if (n != 0) else 1

factorial(5)

# %% Recursion: printReverse

def printReverse(n):
    
    if n == 0:
        return
    
    else:
        print(n % 10)
        printReverse(n // 10)

printReverse(123456789)

# %% Recursion: Print

def printNotReverse(n):
    
    if n == 0:
        return
    
    else:
        printNotReverse(n//10)
        print(n%10)


printNotReverse(1234)

# %% Recursion: Fibonacci

def Fib(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

Fib(10)

# %% Recursion: Paper Test

def foo(n):
    if n < 0:
        return
    else:
        foo(n-1)
        print(n)
        foo(n-2)

foo(3)

# %% Recursion: Linear Search

def LinearSearch(alist, val):
    
    if len(alist) <= 0:
        return -1
    
    if alist[0] == val:
        return 0
    
    else:
        LinearSearch(alist.pop(0), val)

LinearSearch([1, 2, 3, 4, 5], 3)

# %% same as above but works

def linearSearch(alist, index, val):
  
    if index == len(alist):
        return -1
  
    else:
  
        if alist[index] == val:
            return index
  
        else:
            return linearSearch(alist, index + 1, val)

linearSearch([0, 1, 2, 3, 4, 5, 6], 0, 10)

# %% Recursion: Tower of Hanoi

def towerofHanoi(n, fromPeg, toPeg, tempPeg):
    
    if n == 0:
        return
    
    else:
        
        # Move n-1 from A to B:
        towerofHanoi(n-1, fromPeg, tempPeg, toPeg)
        
        print(f"Move top disk from {fromPeg} to {toPeg}.")
        
        # Move n-1 from B to C:
        towerofHanoi(n-1, tempPeg, toPeg, fromPeg)

towerofHanoi(3, "A", "C", "B")

# %% Recursion: Bubble Sort

def bubbleSort(alist, n):

    for i in range(n - 1):
        if alist[i] > alist[i+1]:
            alist[i], alist[i+1] = alist[i+1], alist[i]
    
    if n > 1:
        bubbleSort(alist, n-1)


list = [10, 3, 4, 2, 5, 100, 1]

bubbleSort(list, len(list))
print(list)