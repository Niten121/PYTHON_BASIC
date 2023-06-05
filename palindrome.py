'''palindrome'''
def is_palaindrome(p):
    for i in range (len(p)//2):
        if p[i]!=p[len(p)-i-1]:
            print("{:s} not a palindrome".format(p))
            return

        print("{:s} yes palaindrome".format(p))
        break

print(is_palaindrome("151"))
print(is_palaindrome('123641'))