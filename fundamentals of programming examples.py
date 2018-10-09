#fundamentals of programming
import math

#comments are used to explain what different parts of code does
"""Longer
          comment
                   use"""

#-----------------------------------------------------------------------------

#Data Types

number = int(12)
word = str("Hello1!%*")
boolean = True
otherN = float(3.567)

#the examples above are examples of explicit casting, i am telling it what
#The values are, if you let the computer choose it is called implicit casting

print("-------")
#-----------------------------------------------------------------------------

#Arithmatic operations, MOD = remainders, DIV = whole times
#adding = 1+2
print(1+2)
#subtract = 2-1
print(10-1)
#multiply = 2*2
print(2*2)
#dividing = 2/2
print(10/2)
#Mod = 2 % 5 or 2 MOD 5
print(10%2)
#div = 2 // 5 or 10 DIV 2
print(10//2)
#power = 2**5
print(2**5)

#rounding numbers to whole number
n = round(otherN)
print(n)

#rounding numbers to specific places
no = round(otherN,2)
print(no)

#truncating
n = math.trunc(otherN)
print(n)

print("-------")
#-----------------------------------------------------------------------------

#string operations
st = str("Hello my name is")

#upper
print(st.upper())

#lower
print(st.lower())

#title
print(st.title())

#find how many letters in it is
print(st.find("my"))

#length
print(len(st))

#find the ASCII number from the letter
print(ord("m"))

#find the ASCII letter from the number
print(chr(109))


#concatenation, putting two or more strings together
print(st+word)
print(st+" "+word)
#dont use ',' if possible, try to use '+' instead
print(st,word)

print("-------")
#-----------------------------------------------------------------------------

#Using operations and if statements to choose options and filter results
new = int(23)
print(new)
if new == 10:
    print("Equal")
elif new > 10:
    print("Greater than 10")
elif new < 10:
    print("less than 10")
else:
    print("-")

#using a not equal to variable
new = int(13)
print(new)
if new != 12:
    print("not equal to 12")
else:
    print("Equal")

#checking if a number is an int and telling the user if it is
if new == int(new):
    print("It is a number")
else:
    print("It is not")

#new = int(input("Enter a number: "))
if new == 12:
    print("it is 12")
elif new > 12:
    if new > 50:
        print("bigger than 50")
    else:
        print("Bigger than 12 smaller than 50")
else:
    print("Smaller than 12")
    
#in boolen operations you have AND,OR,NOT,XOR, XOR will only except a or b where as
#OR will accept a, b or both    

print("-------")
#-----------------------------------------------------------------------------
#itterations are loops

num = int(1)
while num < 11:
    print(num)
    num = num+1

print("Done")

#for loops will work they're way through something
lists = ["a","b","c","d"]
for x in lists:
    print(x)

#Changing the letters in hello to the next letter in ASCII
Nstr= ""
string = "Hello"
for x in string:
    letter = ord(x)+1
    Nstr = Nstr+chr(letter)
print(Nstr)

#Changing the letters in hello to the letter before in ASCII
Nstr= ""
string = "Hello"
for x in string:
    letter = ord(x)-1
    Nstr = Nstr+chr(letter)
print(Nstr)
    
print("-------")
#-----------------------------------------------------------------------------

#arrays are ways of storing multiple bits of data
#usally you can have different data types in arrays/lists

lists = ["a","b","c","d"]
print(lists[0])

#multidimentional arrays
multiple = [["Rhian","Brown"],["Sadie","Brown"],["Ollie","Black"]]
print(multiple[1][0])

newName = ["Conrad","Blonde"]
multiple.append(newName)
print(multiple)

#Experimenting with arrays and making a grid or alternating 1's and 0's

#efficient example of using ranges and arrays to print out a grid with only 0's
array = [[0 for i in range(10)] for i in range(10)]
array2 = [[]]

for x in array:
    line = ""
    for i in x:
        line = line+str(i)+""
    print(line)

print("")

#long method for creating alternating 0 and 1's but it doesnt change each line
block = []
for x in range(10):
    pattern = []
    for i in range(10):
        pattern.append(0)
        pattern.append(1)
    block.append(pattern)


for x in block:
    line = ""
    for i in x:
        line = line+str(i)+""
    print(line)   

print("")

#Making a grid that alternates between 0-1
size = int(10)
block = []
for x in range(int(size/2)):
    pattern = []
    pattern2 = []
    for i in range(size):
        pattern.append(0);pattern.append(1)
    block.append(pattern)
    for i in range(size):
        pattern2.append(1);pattern2.append(0)
    block.append(pattern2)



for x in block:
    line = ""
    for i in x:
        line = line+str(i)+""
    print(line)

#-----------------------------------------------------------------------------
#Array experimenting that currently does not work
'''array3 = [[["01" for i in range(5)]for i in range(5)]["10" for i in range(5)] for i in range(5)]

print(array3)

for x in array3:
    line = ""
    for i in x:
        line = line+str(i)+""
    print(line)'''

print("-------")
#-----------------------------------------------------------------------------

#subroutines (procedures and functions)
Nm = "Rhian"

#This is a procedure not a function
def hello(name):
    print("Hello "+name)
hello(Nm)

x = open("Test File.txt","a")
x.write(Nm)
x.close()

x = open("Test File.txt","r")
print(x.readlines())
print("-------")
#-----------------------------------------------------------------------------

#Dictionaries have keys and values, you can have multiple in each
dictonary = {"Rhian":{"age":16,"Gender":"Female","HairColour":"Brown"},
             "Ollie":{"age":16, "Gender":"Male","HairColour":"Black"}}

print(dictonary["Rhian"]["age"])
