import numpy as np

# A = LU ( L : ma trận tam giác dưới, U : ma trận tam giác trên)

def cholesky(A):    # Hàm tìm ma trận tam giác dưới của A
    A = np.array(A, float)
    L = np.zeros_like(A)    # khởi tạo ma trận "không"  với kích thước giống A => là ma trận tam giác dưới
    n,_ = np.shape(A)       # kích cỡ ma trận A ( lấy theo hàng, cột vì A là ma trận vuông nên số hàng = số cột)
    for j in range(n):
        for i in range(j,n):
            if i == j:
                sum_k = 0
                for k in range(j):
                    sum_k += L[i,k] ** 2
                L[i,j] = np.sqrt(A[i,j] - sum_k)
            else:
                sum_k = 0
                for k in range(j):
                    sum_k += L[i,k] * L[j,k]
                L[i,j] = (A[i,j] - sum_k) / L[j,j]   
    return L

def solveLU(L, U, b):
    L = np.array(L, float)
    U = np.array(U, float)
    b = np.array(b, float)
    n,_ = np.shape(L)
    y = np.zeros(n)
    x = np.zeros(n)

    for i in range(n):
        sum_j = 0
        for j in range(i):
            sum_j += L[i,j] * y[j]
        y[i] = (b[i] - sum_j) / L[i,i]
    
    for i in range(n-1, -1, -1):
        sum_j = 0
        for j in range(i+1, n):
            sum_j += U[i,j] * x[j]
        x[i] = (y[i] - sum_j) / U[i,i]
    return x

# A đối xứng 

A = [[8.00, 3.22, 0.8, 0.00, 4.10],
     [3.22, 7.76, 2.33, 1.91, -1.03],
     [0.8, 2.33, 5.25, 1.00, 3.02],
     [0.00, 1.91, 1.00, 7.50, 1.03],
     [4.10, -1.03, 3.02, 1.03, 6.44]]
    
print(np.linalg.eigvals(A))     # kiểm tra ma trận xác định dương

print(cholesky(A))          # in ra ma trận tam giác dưới L của A


# print(np.zeros_like(A))

# print(np.shape(A)) 

# n,_ = np.shape(A) 
# print(n)

b = [9.45, -12.20, 7.78, -8.1, 10.0]

L = cholesky(A)

X = solveLU(L, np.transpose(L), b) # U là chuyển vị của L
print("The solution of Cholesky: ")
print(X)

print("The solution of Numpy: ")
print(np.linalg.solve(A,b))   # Hàm có sẵn tìm nghiệm AX = b

