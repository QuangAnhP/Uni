# %% Morse Code encrypter:

morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}

def encryp(s):
    s = s.upper()
    e = ""
    for i in s:
        if i == " ":
            e = e + " "
        elif (i != " ") and i != s[len(s) - 1]:
            e = e + morse_code[i] + " "
        else: 
            e = e + morse_code[i]
    return e

# %% Morse Code Decrypter: (NOT DONE!)

def decryp(e):
    keys_list = list(morse_code.keys())
    values_list = list(morse_code.values())
    s = ""
    c = 0
    for i in range(len(e)):
        if e[i] != " ":
            c += 1
        if (e[i] == " ") and (c != 0):
            temp = values_list.index(e[i-c : i])
            print(temp)
            s = s + keys_list[temp]
            c = 0
    return s
decryp("...  ---  ... ")














# %% Extra: Remove desired pairs

d = {
    2: "prime",
    3: "prime",
    4: "not prime",
    5: "primte",
    6: "not prime",
}
copy = d.copy()
for k in copy:
    if d[k] == "prime":
        del d[k]
print(d)

# %% Lab 1:

def ASCII():
    d = {}
    for i in range(1, 257):
        d[i] = chr(i)
    
    return d

ASCII()

# %% Lab 2:
