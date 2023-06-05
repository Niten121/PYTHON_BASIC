age = 18
if age<20:
    print("not ele")
else:
    print("ele")

    #comparision
"""
    == != < >  <=
"""

# elif

name = "sara"
if name == "john":
    print("john")
elif name == 'mike':
    print("mike'")
else:
    print("sara")

#and or not

t = True
f = False
st = 3>4
if st:
    print(f)
else:
    print(t)
#test

a = int(input("a="))
b = int(input("b="))
# if(a%b==0):
#     print("divisible")
# else:
#     print("not divisible")

# if (b != 0):
#     c = a / b
# else:
#     exit(1)


n1 = str(input("name1:"))
n2 = str(input("name2:"))
n3 = str(input("name3:"))
if n1.lower()== n2.lower()== n3.lower():
    print("equal")
else:
    exit(500)