from numpy import array, zeros, fabs, linalg
import numpy as np
# Nhập ma trận A    
'''A = array([[0,7,-1,3,1],
           [0,3,4,1,7],
           [6,2,0,2,-1],
           [2,1,2,0,2],
           [3,4,1,-2,1]], float)'''

A = np.loadtxt("data1.txt", dtype = float)

# Nhập vector b
b = array([5,7,2,3,4], float)
n = len(b) 
x = zeros(n, float) # vector toàn số 0

# Quy trình thuận : Khử 
for k in range(n-1):
    if fabs(A[k,k]) < 1.0e-12:
        for i in range(k+1, n):
            if fabs(A[i,k]) > fabs(A[k,k]):
                A[[k,i]] = A[[i,k]]
                b[[k,i]] = b[[i,k]]
                break
    for i in range(k+1, n):
        if A[i,k] == 0:
            continue
        for j in range(k,n):
            A[i,j] = A[k,j] - A[i,j] * A[k,k] / A[i,k]
        b[i] = b[k] - b[i] * A[k,k] / A[i,k]

print(A)
print(b)

# Quy trình nghịch : Thế 
x[n-1] = b[n-1] / A[n-1,n-1]
for i in range(n-2, -1,-1):
    sum = 0
    for j in range(i+1,n):
        sum += A[i,j] * x[j]
    x[i] = (b[i] - sum) / A[i,i]

print("The solution of Gauss method ")
print(x)

print("The solution of Numpy: ")
print(linalg.solve(A,b))

