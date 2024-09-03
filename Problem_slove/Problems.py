# Here I try to solve some easy  and basic problems with python ###############

# 1. Variable Swap: Write a Python program to swap the values of two variables without using a temporary variable.
var1 = 23
var2 = 12
var1, var2 = var2, var1  # tuple unpacking
print(var1, var2)

# 2. Even or Odd: Write a Python program that takes an integer as input and prints whether it is even or odd.
randomNumber = int(input("give a random number: "))  # input function always returns the user input as a string
print(type(randomNumber))
print("even number") if randomNumber % 2 == 0 else print("odd number")

# 3. String Reverse: Write a Python function to reverse a given string and return the reversed string.
# method-1------------------------------------------------


def rev_func(s):
    return s[::-1]


string = input('enter a string value: ')
revString = rev_func(string)
print(revString)


# method-2------------------------------------------------
def rev_function(s):
    rev_string = " "
    for char in s:
        rev_string = char + rev_string

    return rev_string


revString2 = 'hello python'
print(rev_function(revString2))

# 4. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit.
#    Take the Celsius temperature as input from the user.

celsius = int(input("enter temp in celsius:"))
fahrenheit = ((celsius * 9)/5)+32
print(fahrenheit)

