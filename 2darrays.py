from pprint import  pprint as pretty_print
from copy import  copy,deepcopy

import numpy as np

num_2d = [
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13],
    [14,15,16,17]
]
print(num_2d)
pretty_print(num_2d)# is used to represst in a more better way

num_2d[2][2] =-6
pretty_print(num_2d)
letters = ['A','B','C']
letters_2d = [letters,letters,letters] #to change in multiple list
letters_2d[0][0]='a'
print(letters_2d)
letters_2d = [copy(letters),copy(letters),copy(letters)]# to change in one list
letters_2d[0][0]='b'
pretty_print(letters_2d)