'''
a function which produces output and use the return keyword returns an assignable value to a variable

example of the function ahiech returs assignablevales are:
max_value = max([3,4,8,1])
'''

def is_even(number):
    if number%2==0:
        return True
    return False
n = int(input("enter number"))
print(is_even(n))

"""
a void function doesnot return a value it performs an action . void function do not use the return keyword in their implementation

example of the coid funcion incldes
print('i return nothing')

[4,8,5,9,4].sort
"""
def iss_even(num):
    if num %2 ==0:
        print("'{:d}' is even".format(num))
    else:
        print('"{:d}" is odd'.format(num))

n = int(input("enter number"))
print(iss_even(n))
