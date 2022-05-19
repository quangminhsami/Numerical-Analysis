import numpy as np

def gauss_jordan(a,b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)

    for k in range(n):
        if np.fabs(a[k,k]) < 1.0e-12:
            for i in range(k+1, n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    for j in range(k,n):
                        a[k,j],a[i,j] = a[i,j],a[k,j]
                    b[k],b[i] = b[i],b[k]
                    break

        for j in range(k,n):
            a[k,j] /= a[k,k]
        b[k] /= a[k,k]

        for i in range(n):
            if i == k or a[i,k] == 0 :
                continue
            for j in range(k,n):
                a[i,j] -= a[i,k] * a[k,j]
            b[i] -= a[i,k] * b[k]

    return b,a

'''a = [[0,2,0,1],
    [2,2,3,2],
    [4,-3,0,1],
    [6,1,-6,-5]]'''

a = np.loadtxt("data2.txt", dtype = float)

b = [0,-2,-7,6]

x,A = gauss_jordan(a,b)

print("The transformed [A]:")
print(A)

print("The solution of Gauss-Jordan method:")
print(x)

# print("The solution of Numpy: ")
# print(np.linalg.solve(a,b))

