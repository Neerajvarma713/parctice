import numpy as np
arr = np.arange(1,10,2)
arr1 = np.array([1,3,2,5,8])
arr2 = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

'''
print(arr1.shape)
print(arr1.dtype)
print(arr2.shape)
print(arr2.size)
print(arr2.ndim)
print(arr2.dtype)
print(arr2.itemsize)
print(arr2.nbytes)
'''

'''
print(arr2)
print(arr2[0])
print(arr2[0][2])
print(arr2[0,0])
print(arr2[0:3,0:3:2])
print(arr2[1]) #2nd row
print(arr2[:,1]) #2nd column
'''

'''
print(arr2+arr3)
print(arr2-arr3)
print(arr2*arr3)
print(arr2/arr3)
print(arr2**arr3)
'''

'''
print(arr1 + 10)
print(arr1 * 2)
'''
'''
print(np.sum(arr2))
print(np.sum(arr1))
print(np.mean(arr1))
print(np.median(arr1))
print(np.std(arr1))
print(np.var(arr1))
print(np.min(arr1))
print(np.max(arr1))
print(np.sqrt(arr1))
print(np.exp(arr1))
'''

'''
print(np.reshape(arr1,(2,3)))
print(np.transpose(arr2))

#ravel and flatten are used to convert a multi-dimensional array into a 1D array. 
# The difference is that ravel returns a flattened array and is a view of the original array whenever possible,
# while flatten always returns a copy of the original array.  
r = np.ravel(arr2)
r[0] = 100
print(arr2)
print(r)

f = arr2.flatten()
f[0] = 200
print(arr2)
print(f)

print(arr2.flatten())
print(np.sort(arr1))
'''

'''
print("arr1: ",arr1)
print("arr: ",arr)
print(arr+arr1)
print(np.concatenate((a,b), axis=0)) #concatenate along rows
print(np.concatenate((a,b), axis=1)) #concatenate along columns 
'''

'''
print(np.hstack((a,b))) #horizontal stack
print(np.vstack((a,b))) #vertical stack
print(np.dstack((a,b))) #depth stack1
print(np.split(arr1,3))
print(np.split(arr1,3)[0]) #splits it into 3 equal parts selects the first split
print(np.split(arr1,[2,5])) #splits arr1 into 3 parts at index 2 and 5
'''

'''
print(arr1>5)
print(arr1[arr1>5])
print(arr1[(arr1 % 2 == 0 )])
print(arr1[(arr1 > 3 ) & (arr1 < 10 )])

# bbelow 2 methods are used to replace the values in an array based on a condition
arr1[arr1 > 5] = 0 #if the condition is true, then replace the value with 0
print(arr1)
print(np.where(arr1>5, 0, arr1)) #if the condition is true, then replace the value with 0 else keep the value as it is
'''

'''
print("hello")
print(np.random.rand())
print(np.random.rand(2,3))
print(np.random.randint(1,10))
print(np.random.randint(2,20, size=(2,3)))
print("original arr:" ,arr1)
print(np.random.permutation(arr1)) #it doesnot suffle the original array
np.random.shuffle(arr1) #it suffles the original array
print(arr1)
'''

'''
#a = np.array([[1,2],[3,4]])
#b = np.array([[5,6],[7,8]])
print(np.dot(arr,arr1)) #dot product of 2 arrays
print(np.matmul(a,b)) #matrix multiplication of 2 arrays
print(np.linalg.inv(a)) #inverse of a matrix
print(np.linalg.det(b)) #determinant of a matrix
print(np.linalg.eig(a)) #eigenvalues and eigenvectors of a matrix
'''

'''
a @ b #matrix multiplication using @ operator
x = np.linalg.inv(a) #multiplying a matrix with its inverse gives identity matrix
print(x)
print(np.eye(3)) #identity matrix of size 3x3
'''

A = np.array([[2,1],[1,3]])
B = np.array([5,6])
print(np.linalg.solve(A, B)) #solves the linear equation Ax = B for x
