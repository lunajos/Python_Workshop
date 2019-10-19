#! path/to/runtime

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
# Array - ?!


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
setting = {}
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

print('#############################################################')
print('                    Assignment Operators                     ')
# =      Add
# -=     Subtract
# +=     Divide
# *=     Multiply
# %=     Modulus
# **=    Exponentiation
# //=    Floor division

print('#############################################################')
print('                    Comparison Operators                   ')
# ==
# !=
# >
# <
# >=
# <=


print('#############################################################')
print('                       Logical Operators                    ')
# and
# or
# not
# is
# is not

print('#############################################################')
print('                      Bitewise Operators                    ')
# &
# |
# ^
# ~
# <<
# >>


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