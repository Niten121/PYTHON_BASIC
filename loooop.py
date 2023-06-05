# s = "hello world"
# a = [4,5,6]
#
# print(5 in a)
# print(4 in a)
# print('ello' in s)
# for eve in [2,4,8,10]:
#     print(eve)
# odd = [1,3,5,7,9]
# for of in odd:
#     print(of)
#
#
# print(range(len(odd)))
# for index in range(len(odd)):
#     print("index {:d} , odd no :{:d}".format(index, odd[index]))
#
# #while
# index  = 0
# names = ['josh','harry','leah','mitchel']
# while index < len(names):
#     name = names[index]
#     print(name)
#     index = index+1
# total = 0
# v = 1
# while v <=10:
#     total=total+v
#     v = v+1
# print(total)
#
# while True:
#     a, b = int(input("enter a  values: ")), int(input("enter b value: "))
#     if a+b==10:
#         print("congrats u got it")
#         break
#     else:
#         print("please make sure u inserted perfect numbers ")

        #loops and Conditionals

numbers = [1,2,3,4,5,6,7,8,9]
total = 0
for n in numbers:
    if n %2==0:
        total = total+n
print(total)

alpha = "asdfghjklqwertyuiopzxcvbnm"
vowels = 'aeiouAEIOU'
my_str = 'packt punlishing rocks!'

characters = []
for ch in my_str:
    if ch not in vowels and ch in alpha:
        characters.append(ch)
cononants = "->".join(characters)
print(cononants)

