my_list = [1,2,3,4,5,6]
my_tup = (2,4,8,6,5)
my_str = "hello world!"

print(dir(my_list))
#lets check if iter is there in list tup and str
print('__iter__' in dir(my_list))
print('__iter__' in dir(my_str))
print('__iter__' in dir(my_tup))
            #Ways of itteration
    #1st way
for elem in my_list:
    print(elem)
    # 2nd way
list_iterator = iter(my_list)
while True:
    try:

        next_ele = next(list_iterator)
        print(next_ele)
    except StopIteration:
        break