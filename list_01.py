num = [5,6,2,4,6]
names = ['health', 'mitvh','niten',444]

print(num)
print(names[0])
print(names[1])
print(names[2])
print(names[3])


mystr = 'hello'
print(mystr[0])
print(mystr[4])

#listg method
alpha = ["a","b","c","d"]
alpha = alpha + ['s','f']
print(alpha)
d_index = alpha.index(('d'))
print("d_index" + str(d_index))
del alpha[d_index]
print(alpha)
alpha.remove("c")
print(alpha)

'''
append = add ele in the list
extend = exten=nd the liat by appending  all elements 
'''
#advance list methods
alpha1 = ['a','f','b']
alpha2 = ['e','s']
alpha3 = "bdjsgtyaavdyv"

print(alpha1)
alpha1.sort()
print(alpha1)

alpha1.insert(2,'g')
print(alpha1)

'''
to remove [] symbol from the list   '''

alpha1 = ' '.join(alpha1)
print(alpha1)

