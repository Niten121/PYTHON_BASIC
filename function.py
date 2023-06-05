# function are ways to encapsulate code to perform a specific task (sort numbers ,trgger events , do a numerical computation )
# easier to debug because all codes performing a task is gathered at the same pace

#function are reusable
'''
pi = 3.141
def cir_area(r):
    return pi*r*r
print(cir_area(5))
'''


            #arguments and parameteres
import datetime as dt
# # def ad(a,b,c):
# #     return a+b+c
# def add(*numbers):#for n number of inputs
#     total = 0
#     for n in numbers:
#         total += n
#         return total
# print(add(5,5))

'''record time and display time'''
def record_time (message, time = dt.datetime.now()):
    print('{:},time::{:}'.format(message,time))
record_time("good afternoon")