# %% Search: Linear Search

def LinearSearch(alist, val):
    for i in range(len(alist)):
        if alist[i] == val:
            return i
    return -1

LinearSearch([1, 2, 3, 4, 5], 5)

# %% Search: Binary Search O(log[2](n) + 1)

def BinarySearch(alist, val): 
    
    # Assign beginning values:
    start = 0
    end = len(alist) - 1

    # Start the loop:
    while start <= end:
        mid = (start + end) // 2
        
        if alist[mid] == val:
            return mid
        
        elif alist[mid] > val:
            end = mid - 1
        
        elif alist[mid] < val:
            start = mid + 1
    
    return -1

BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)

# %% Sort: Bubble Sort O(n^2)

def BubbleSort(alist):
    for i in range(len(alist) - 1):
        
        for j in range(len(alist) - i - 1):
        
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

    return alist

BubbleSort([1, 5, 4, 66, 53, 10])

# %% Sort: Selection Sort O(n^2)

def SelectionSort(alist):
    
    for i in range(len(alist)):
        index = i
    
        for j in range(i+1, len(alist)):
            if alist[j] < alist[index]:
                index = j
    
        temp = alist[index]
        alist[index] = alist[i]
        alist[i] = temp

    return alist

# %% Sort: Insertion Sort O(n^2/2 - n/2)

def InsertionSort(alist):
    
    for i in range(1, len(alist)):
        temp = alist[i]
        index = i - 1
        
        while index >= 0:
            
            if alist[index] > temp:
                alist[index + 1] = alist[index] 
                index -= 1
                print(alist)
                
            else:
                break
            
        alist[index + 1] = temp
        
    return alist

InsertionSort([5, 10, 2, 3, 1, 6])