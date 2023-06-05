import numpy as np
# a= np.array([1,2,5,6,3,7])
# print("the array is ", a)
# print("the max is ",a.max())
# print("the min is ",a.min())
# print("the sum is ",a.sum())

# x= np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# print(x)
# print("the sum of the the axis 0", x.sum(axis=0))  #0 is for col and 1 is for rows
# e = x.min(axis=0)
# print("the minimun of the matrics axix 0 ", x.min(axis=0))
# print(e.sum())

                #array comcatenation
# a = np.array([[1,2,30],[10,15,4]])
# b  = np.array([[1,2,3],[12,15,16]])
# print("vertically concatenation" , np.vstack((a,b,a,a,a)))
# print("horizontally concatenated", np.hstack((a,b)))

                    #where: for seleting elements based on condition
a = np.arange(12)
# b = np.where(a*2)

b = np.where([[True,False], [True,True]],[[1,2],[3,2]],[[4,5],[6,7]])
print(b)


