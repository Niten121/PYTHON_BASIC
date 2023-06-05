'''
Shift cipher
'''

alpha = "mnbvcxzlkjhgfdsaqwertyuiop"
def encrypt(s,shift = 1):
    encrypted_str=''
    for ch in s:
        index = alpha.index(ch)
        shifted_index = (index+shift)% len(alpha)
        encrypted_str += alpha[shifted_index]
    return encrypted_str

def decrypt(e,shift = 3):
    decrypted_str = ''
    for ch in e:
        index = alpha.index(ch)
        shifted_index = (index-shift)%len(alpha)
        decrypted_str += alpha[shifted_index]
    return decrypted_str


print(encrypt("sadanand"))
print(decrypt("weqececq"))