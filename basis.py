#string
science = "SCIENCE"
apple = "apple"

print(apple)
apple = apple.upper()
print(apple)


print(science.lower())
print(science.title())


apple = "           apple                  "
print(apple)
apple = apple.strip().upper()
print(apple)

#advance string method
pre = "python os awsom"
suf = "lang "
astr = pre + suf

astr = astr.replace('lang', ' snake')
print(astr)

astr = astr *2
print(astr)

astr = astr.replace('lang', 'snake ',1)
print("last is count ",astr)
astr = astr.count('snake')
print(astr)

