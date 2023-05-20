# %% Import File: Read lines and find average of first column:

file = open("mydata.txt", "r")
sum = 0
count = 0

for line in file:
    value = line.split()
    sum += int(value[0]) 
    count += 1
    
print(sum / count)


file.close()

# %% split()

message1 = "Hello     world          bye"
a = message1.split()
print(a)

message2 = "Hello,world,bye"
b = message2.split(",")
print(b)

# %% Method: read()

file = open("mydata.txt", "r")

filestring = file.read()
print(type(filestring))
print(filestring)

file.close()
# %% Method: readline()

    # readline()
file = open("mydata.txt",)

test = file.readline()
test = file.readline()
print(test)

while test:
    print(test)
    test = file.readline()

    # readlines()
test = file.readlines()
print(test)


file.close()

# %% Practice1: Turn into 2D list

file = open("mydata.txt",)
data = []

for line in file:
    temp = line.split()
    data.append(temp)

print(data)

file.close()

# %% Practice 2:

file = open("mydata.txt",)
value = 0

for i in range(3):
    temp = data[i][2].split("E")
    value += float(temp[0])

power = temp[1]
if value > 10:
    value /= 10
    power = str(int(power) + 1)    
print(f"{value}E{power}")

file.close()

# %% Extract info from downloaded article:


    # Count words

file = open("article.txt", "r")
article = file.read()
k = 0
wordcount = 0

for i in article:
    if i == " ":
        k += 1
    elif (i != " ") and (k != 0):
        wordcount += 1
        k = 0








# %% Practice: compare number from a column from file
file = open("mydata.txt",)
data = []
line = file.readline()

for line in file:
    temp = line.split()
    data.append(float(temp[1]))

for i in range(len(data) - 1):
    if data[i] > data[i-1]:
        print("Increasted")
    elif data[i] < data[i-1]:
        print("Decreased")

file.close()

# %% "w"

file = open("mydata.txt", "r")
new_file = open("newdata.txt", "w")
line = file.readline()

while line:
    values = line.split()
    dataline = values[1] + "\t" + values[2]
    new_file.write(dataline + "\n")
    line = file.readline()

file.close()
new_file.close()

# %% swap data in new file

file = open("mydata.txt", "r")
swapped = open("swapped.txt", "w")
line = file.readline()

while line:
    values = line.split()
    dataline = values[1] + "\t" + values[0] + "\t" + values[2]
    swapped.write(dataline + "\n")
    line = file.readline()
    
# %% Extra: Linear Regression

def linearRegression(xlist, ylist):
    
    n = len(xlist)
    x_ave = sum(xlist) / n
    y_ave = sum(ylist) / n
    
    total_xy = 0
    for i in range(n):
        total_xy += xlist[i] * ylist[i]
    
    total_x2 = 0
    for i in range(n):
        total_x2 += xlist[i]**2
    
    a = (total_xy - (n * x_ave * y_ave)) / (total_x2 - n * x_ave**2)
    b = y_ave - a*x_ave
    
    return (a, b)


infile = open("mydata.txt", "r")
data = []

for line in infile:
    temp = line.split()
    data.append(temp)

year = [float(data[i][0]) for i in range(len(data))]
temp = [float(data[i][1]) for i in range(len(data))]

linearRegression(year, temp)