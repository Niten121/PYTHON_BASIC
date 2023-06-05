import numpy as np
# a = [ 1, 2, 3, 4 ]
# a.append(3)
# print("after append ",a)
# print("from 0 to 2:", a[0:2])
# ar = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(ar)
# print("dimention of ar",np.ndim(ar))
# print(ar[1, 1])
#
# arr= np.array([1,2,3,4,5,6,7,8,9])
# arr1 = np.array([1,2,5,6,10])
# print("dimention of arr",np.ndim(arr))
# print(arr[-2])
# i = np.intersect1d(arr, arr1)
# print("intersection of the 2 arrays :", i)
#
ar = np.array([[[[[[[[[[[[[[[1,2,3],[4,5,6],[7,8,9]]]]]]]]]]]]]]])
au = np.array([[[[[[[[[[[[[[6,2,3],[4,5,6],[7,8,9]]]]]]]]]]]]]])
sum=np.dot(au,ar)
summ=au*ar
print(summ)
print(sum)
#print(ar)
print(np.ndim(ar))

#l = []
#print(type(l))
#for i in range (5):
#   print(i**i)