# %% Sort: Merge Sort

def mergeSort(alist):
    print("Splitting ", alist)
    
    if len(alist) > 1:
    
    # Splitting the list:
        mid = len(alist) // 2
        lefthalf = alist[:mid]  #can use parameters to avoid slicing
        righthalf = alist[mid:] 
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
    
    # Sorting and Merging:
        i = j = k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

    # In case one of the half-list has more elements than the other:
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
        
        return alist
                    
mergeSort([1, 3, 4, 2, 10, 214, 55, 30, 99])


'''
Time Complexity:
f(n): call(half-list) + call(half-list) + merge

<=> f(n) = 2f(n/2) + n
    f(n/2) = 2f(n/4) + n/2
=>  f(n) = 4f(n/4) + 2n

    f(n/4) = 2f(n/8) + n/4
=>  f(n) = 8f(n/8) + 3n

    f(n) = 2^i . f(n/(2^i)) + i.n ---
    f(1) = 1                        |
    n/(2^i) = 1 -> 2^i = n          |
    |                               |
=>  f(n) = n + n.log2(n)         <---
=> O(nlogn)
'''

# %% Time Complexity:

def foo(n):
    d, i, r, b = 50, 1, 0.5, 10
    
    while i <= n:
    
        b = d + b + b*r
        i = i + 1
    
    return b

'''
4 assingment -> O(1)

in n loop:
    1 compare
    2 assingment
    3 addition
    1 multiplication
-> 4 + 7n
=> O(n)
'''

"""
Horner's Method:
f(x) = a(n).x^n + a(n-1).x^(n-1) + ... + a(1)x + a(0)
= a(0) + x{a(1) + x[a(2) + x...]}           (turn O(n^2) - > O(n))
"""

# %% (a,n) -> a^n | O(n)

def power1(a, n):
    product = 1
    i = 0
    while i < n:
        product = product * a
        i += 1
    return product

power1(2, 3)

# %% better | O(logn)

def better_power1(a, n):
    if n == 0:
        return 1
    
    elif n % 2 == 0:
        return better_power1(a*a, n/2)  
    
    else:
        return a * better_power1(a*a, (n-1)//2)

better_power1(2, 3)

# %% also better | O(logn)

def also_better_power1(a, n):
    res = 1
    i = n
    
    while i > 0:
        
        if not(i == i//2*2):
            res = res * a
        
        i //= 2
        if i > 0:
            a = a * a
        
    return res

also_better_power1(2, 3)