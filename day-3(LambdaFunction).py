
x = lambda a, b: a-b
print(x(34, 22))
# The power of lambda is better shown when
# you use them as an anonymous function inside another function.

def myFunc(n):
    return lambda a: a*n


lambdaFunc = myFunc(3)
print(lambdaFunc(12))
print(lambdaFunc(33))

string = "hellopython"

upper = lambda upr: upr.upper()
print(upper(string))

Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)
