# %% Q1

def toDict(alist):
    
    d = {}
    for i in alist:
        d[i] = ord(i)
    
    return d

toDict(["a", "b", "c", "?"])

# %% Q2 (Assume only numbers and upper case Englist letters are input)

numpad = {
    "A":2, "B":2, "C":2,
    "D":3, "E":3, "F":3,
    "G":4, "H":4, "I":4,
    "J":5, "K":5, "L":5,
    "M":6, "N":6, "O":6,
    "P":7, "Q":7, "R":7, "S":7,
    "T":8, "U":8, "V":8,
    "W":9, "X":9, "Y":9,
}



def dialer(string):
    
    new_string = ""
    
    for i in string:
    
        if 65 <= ord(i) <= 90:
            new_string += str(numpad[i])

        else:
            new_string += i
    
    return new_string


dialer("604-EXAMPLE")
