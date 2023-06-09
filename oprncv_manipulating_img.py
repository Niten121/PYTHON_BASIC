import  cv2
from matplotlib import pyplot as plt

moon = cv2.imread('bw.jpeg')
print(moon.shape)
moon1 = cv2.resize(moon,(250,220))
rect = cv2.imread('black-and-white rect.png')
print(rect.shape)
rect1 = cv2.resize(rect,(250,220))
#
cv2.imshow('moon',moon1)
cv2.waitKey(0)
cv2.imshow('rect',rect1)
cv2.waitKey(0)
image_AND = cv2.bitwise_and(rect1,moon1)
cv2.imshow("and",image_AND)
plt.imshow(cv2.cvtColor(image_AND,cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
image_OR = cv2.bitwise_or(rect1,moon1)
cv2.imshow("or",image_OR)
plt.imshow(cv2.cvtColor(image_OR,cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
image_XOR = cv2.bitwise_xor(rect1,moon1)
cv2.imshow("xor",image_XOR)
plt.imshow(cv2.cvtColor(image_XOR,cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
image_NOT = cv2.bitwise_not(rect1,moon1)
cv2.imshow("not",image_NOT)
plt.imshow(cv2.cvtColor(image_NOT,cv2.COLOR_BGR2RGB))
cv2.waitKey(0)