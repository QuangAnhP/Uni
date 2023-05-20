# %% Q1:

def q1(n):
    if n > 0:
        q1(n-1)
        print(n)
    else: 
        return 
q1(10)



# %% Q2:

def q2(n):
    while n > 0:
        print(n)
        return q2(n-1)
    
q2(10)

# %% Q3: (not done)

def q3(n):

    if n > 0:
        q3(n-1)

    else:
        return
        
q3(10)

# %% Q4: (not done)

def q4(n):
    while n > 0:
        return q4(n+(n-1))
    
q4(3)
    
    
    
    

# %% Extra: reverse a number with recursion

def rev(old, new):

    if old == 0:
        return new
    
    else:
        return rev(old // 10, new*10 + old%10)

rev(1234, 0)