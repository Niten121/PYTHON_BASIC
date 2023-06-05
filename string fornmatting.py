n = 11
f = 1.22
s = "fomputer"

print("my no is {:d}".format(n))
print("my no is {:b}".format(n))
'''
 there r many formatting styles 
 e = exponents
 b = binary
 o = octal
 d = decimal
 x = hexadecimal
 f = float
 s = string
 '''
print("{:f}".format(f))
print("{:.3f}".format(f))
#padding
print("{:11.3f}".format(f))
print("{:011.3f}".format(f))
print("{name} owns {amount} of {objects}".format(name = "niten", amount = 500, objects= "pair of shoes"))