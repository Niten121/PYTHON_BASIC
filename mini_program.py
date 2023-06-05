import sys
l = input()
split = line.split()

left = split[0]
op =split[1]
right = int (split[2])

val = 0
if op == '+':
    val = left+right
elif op =='-':
    val = left-right
elif op =='*':
    val = left*right
elif op =='/':
    if right==0:
        print('dib by 0')
        sys.exit(1)
else :
    print("retry")
