"""this is practicing.... page practice_0"""

# list comprehension: make a list of squares from 1 to 10
def square_function(x):
    return x**2
square_list = [square_function(x) for x in range(1,11,2)]

# using *args
def sum_of_args(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

# using dict.items: iterating over...
fav_numbers = {'eric': 17, 'ever': 4} 
for name, number in fav_numbers.items(): 
    print(name + ' loves ' + str(number))
    

def func(x):
    return x + 1

