#prime no checker
n = int(input("enterer number:: "))

divisor=[]

if n >= 2:

    for divisor in range(2,n):
        if n % divisor == 0:
                print('{:d} is not prime because {:} divide {:d}'.format(n, str(divisor), n))
                break
        else:
                print('{:d} is prime'.format(n))
                break
else:
    print("kindly enter +ve number and try again")

