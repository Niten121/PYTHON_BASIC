#
# def double(n):
#     if n == 0:
#         return 0
#     return double(n-1)+3
#
# n = int(input("enter number "))
# print(double(n))
#
'''power'''
# def expo(b,e):
#     if(e==0):
#         return 1
#     else :
#         return expo(b,e-1)*b
# b = int(input('enter base'))
# e = int(input('enter power'))
# print(expo(b,e))

#examples
'''count vowels'''
# def count_vowels(s,i=0):
#     if (i==len(s)):
#         return 0
#     c= s[i]
#     if c in 'aeiou':
#         return count_vowels(s,i+1)+1
#     return count_vowels(s,i+1)+0
# s=str(input('enter string: '))
# print(count_vowels(s))

'''sum of digits'''
# def digit_sum(n):
#     if n ==0 :
#         return 0
#     return digit_sum(n//10)+n%10
# n = int(input("enter didit to be sumed :"))
# print(digit_sum(n))
'''fibbonacci'''


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("enter upto ehat u want fibbo series: "))
for i in range(n):
    print(fibonacci(i))