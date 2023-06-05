#                     # Python code to read image
# # import cv2
# # import matplotlib.pyplot as plt
# # img = cv2.imread("demo.jpg")
# # cv2.imshow("image", img)
# # cv2.waitKey(10)
# # cv2.destroyAllWindows()
#
# # #                     #capture video from web-cam
# # import cv2
# # vid = cv2.VideoCapture(0)
# # while (True):
# #     ret, frame = vid.read()
# #     cv2.imshow("frame",frame)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# # vid.release()
# # cv2.destroyAllWindows()
#
#                   resize image
# import cv2
# img1 = cv2.imread("img1.png")
# cv2.imshow('img', img1)
# cv2.waitKey(0)
# shape = img1.shape
# print(shape)
# img = cv2.resize(img1,(300,300))
# i_shape = img.shape
# print("shape after resize", i_shape)
# cv2.imshow("reduced sizee", img)
# cv2.waitKey(0)
# #
#                  #addition of 2 images
# import cv2
# img1 = cv2.imread("img1.png")
# cv2.resize(img1,(250,250))
# cv2.imshow("img1",img1)
# img2 = cv2.imread("img2.png")
# cv2.imshow("img2",img2)
# cv2.waitKey(0)
# add = cv2.add(img1,img2)
# cv2.imshow("added",add)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#               #addition of 2 image  by giving weighted values
# import cv2
# img1 = cv2.imread("img1.png")
# cv2.resize(img1,(300,300))
# cv2.imshow("img1",img1)
# img2 = cv2.imread("img2.png")
# cv2.resize(img2,(300,300))
# cv2.imshow("img2",img2)
# cv2.waitKey(0)
# add = cv2.addWeighted(img1,0.7,img2,0.3,-1)
# cv2.imshow("added",add)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#                    # detect cornor
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("cornors.png")
cv2.imshow("image ",img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image ", gray)
cv2.waitKey(0)
cornors= cv2.goodFeaturesToTrack(gray,27,0.01,10)
cornors = np.int0(cornors)

for i in cornors:
    
    x,y = i.ravel()
    cv2.circle(img, (x,y),3,225,-1)

plt.imshow(img)
plt.show()
cv2.destroyAllWindows()

