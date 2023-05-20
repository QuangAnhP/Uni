# %% Part a

def isFound(d, val):
    return (val in d.values())


d = {"key1": 10, "key2": 2, "key3": 4}

isFound(d, 10)

# %% Part b                                 (didn't use isFound)


    # main:
    
def removeDupValue(d):
    new = {}
        
    for k,v in d.items():
        
        if count(d.values(), v) < 2:
            new[k] = v
    
    return new


    # aux:

def count(alist, val):
    count = 0
    
    for i in alist:
    
        if i == val:
            count += 1
    
    return count


removeDupValue({"key1": 1, "key2": 4, "key3": 6,
               "key4": 4, "key5": 8, "key6": 1, "key7": 1,})

