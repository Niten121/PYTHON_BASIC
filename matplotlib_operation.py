# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:17:35 2022

@author: sethy
"""

'''

MATPLOTLIB:
    matplotlib.pyplot is a collection of the command style function that make matplotlib works like MATLABA
types of plots
bar:
make a bar
barh:
    make a horizontal bar plot
boxplot:
    make a box and whisker plot
hist:
    plpot a histogram
pie:
    plot a pie chat
plot:
    plot lines and or  markers to the axes
polar:
    make a polar plot
scatter:
    make a scter plot of x and y
stackplot:
    DRAWS A STACK ARE A PLOT
stem:
    create a stem plot

'''
import numpy as np

'''import matplotlib.pyplot as plt
xs = [1,2,3,4,5]
ys = [x**2 for x in xs]
x = np.linspace(1,0,100)
y = [i*7 for i in x]
print(x)
plt.plot(x, y)
plt.show()
#plt.scatter(xs, ys)

'''  # inline: to display op inside the notbook itself ( and not in the seerate vieweer).
# enter  %matplotlib'''
# install qt5 to use % matplotlib
''' '''
import matplotlib.pyplot as plt
from pylab import *

x = np.linspace(-3, 3, 30)
y = x ** 2
plt.plot(x, y)
plt.show()
