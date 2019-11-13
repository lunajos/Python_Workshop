##############
# Data Types #
##############
# String
# Int
# Float
# Boolean

##############
# Collection #
##############
# Tuple - ()
# Set   - {}
# List  - []


print('#############################################################')
print('                            Data Types                       ')
strings = 'this is a string'
integer = 1
floating = 3.3

string_to_int = '32'
int_to_string = 23

string_to_float = '32.32'
float_to_string = 32.32

booleanFalse = False
booleanTrue = True

tupling = ('test', 'ing', 'tuple')
setting = {
  "name": "Pat",
  "age": 25,
  "height": "68"
}
listing = [1, 2, 3, 4, 5, 6]


print('#############################################################')
print('                            Conversion                       ')

print(type(string_to_float))
print(type(float(string_to_float)))
print(type(int(string_to_int)))

print('#############################################################')
print('                        Input and Output                     ')

# Input
first = input("Enter First name: ")
print('Enter Last name')
last = input()

# Output
print('Your First Name is ' + first)
print('Your Fast Name is ' + last)

print('#############################################################')
print('                            Functions                        ')

def printWords():
    print('Foo Bar');

def printParams(aWord):
    print(aWord);

printWords()
printParams('pneumonoultramicroscopicsilicovolcanoconiosis')

# Statements


print('#############################################################')
print('                    Arithmetic Operators                     ')
# +     Add
# -     Subtract
# /     Divide
# *     Multiply
# %     Modulus
# **    Exponentiation
# //    Floor division

print(3+2)
print(3-2)
print(3/2)
print(3*2)
print(3%2)
print(3**2)
print(3//2)


print('#############################################################')
print('                    Assignment Operators                     ')
# =      Add
# -=     Subtract
# +=     Divide
# *=     Multiply
# %=     Modulus
# **=    Exponentiation
# //=    Floor division

item1 = 10      # 10
item1 -= 1      # 9
item1 += 5.6    # 15
item1 *= 3      # 75
item1 %= 5      #
item1 **= 2     #
# item1 //= 0     #
print(item1)

#################
# Control Flows #
#################

print('#############################################################')
print('                       If Control Flows                      ')
# IF
if (not booleanFalse):
    print('The answer is: ' + str(booleanFalse))
elif(booleanFalse):
    print('The answer is: ' + str(booleanFalse))
else:
    print('This catches everything ')

print('#############################################################')
print('                       Logical Operators                    ')
# and
# or
# not
# is
# is not
if (True and False): print("And")
if (True or False): print("Or")
if (not False): print("Greater than")
if (True is True): print("Less Than")
if (False is not True): print("GE")

print('#############################################################')
print('                      Bitewise Operators                    ')
# &
# |
# ^
# ~
# <<
# >>

if (True & False): print("&")
if (True | False): print("|")
if (~False): print("~")
if (True << True): print("<<")
if (False >> True): print(">>")

print('#############################################################')
print('                    Comparison Operators                   ')
# ==
# !=
# >
# <
# >=
# <=

if (1==2): print("Equal")
if (1!=2): print("Not equal")
if (1>2): print("Greater than")
if (1<2): print("Less Than")
if (1>=2): print("GE")
if (1<=2): print("LE")


print('#############################################################')
print('                          While Loops                        ')
num = 0
while num <= 5:
    print("The number is: " + str(num))
    num += 1

print('#############################################################')
print('                           For Loops                         ')
# For Loop
for x in listing:
    print('for loop: '+ str(x))

print('#############################################################')
print('                 Built in Methods & Functions                ')

print("Does it end in 'ing'?:  " + str(strings.endswith("ing")))
print(listing)

listing.append("test")

print(listing)
print(listing.pop())
print(sum(listing))

print(5 in listing)
print(len("pneumonoultramicroscopicsilicovolcanoconiosis"))
print(len(listing))
