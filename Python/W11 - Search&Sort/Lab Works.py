# %% 1  
from random import randint

def SequentialSearch(alist, val):
    for i in range(len(alist)):
        if alist[i] == val:
            return f"Value found at {i}"  
    return "Value not found"


def main1():
    alist = [randint(1, 10) for i in range(10)]
    print(alist)
    print(SequentialSearch(alist, 1))

main1()

# %% 2


def BinarySearch(alist, val):

    start = 0
    end = len(alist) - 1

    while start <= end:
        mid = (start + end) // 2

        if alist[mid] == val:
            return f"Value found at {mid}"

        elif alist[mid] > val:
            end = mid - 1

        elif alist[mid] < val:
            start = mid + 1

    return "Value not found"

def main2():
    alist = [randint(1, 10) for i in range(10)]
    print(alist)
    print(BinarySearch(alist, 1))


main2()

# %% Extra: return elements sorted in order of their freq in original list

alist = [randint(1, 20) for i in range(10)]

def freq(alist, ele):
    count = 0
    for i in range(len(alist)):
        if alist[i] == ele:
            count += 1
    return count

def sorted(alist, ele):
    print(alist)
    d = {}

    for i in alist:
        d[i] = freq(alist, i)
        
    # swapping keys and values
    new_dict = {}    
    for k in d:
        if d[k] not in new_dict:
            new_dict[d[k]] = [k]
        else:
            new_dict[d[k]].append(k)
    
'''
not done
'''