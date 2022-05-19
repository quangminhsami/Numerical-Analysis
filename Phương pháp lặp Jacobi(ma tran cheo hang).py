import numpy as np

eps = float(input()) # nhập sai số 

# nhập ma trận A là ma trận chéo trội hàng
'''A = np.array([[-19,7,5,4],
              [0,10,2,-3],
              [1,-5,16,5],
              [-6,1,2,14]])'''

# Nhap ma tran A tu file
A = np.loadtxt("data4.txt", dtype= float)

# Nhập vector b
b = np.array([1,2,3,4])

# kich thuoc theo hang cua ma tran A
n,_ = np.shape(A)

# ma trận đơn vị của A
I = np.identity(n) 

# ma trận đường chéo của A
T = np.linalg.inv(np.diag(np.diag(A)))

B = I - np.dot(T, A)

norm_B = np.linalg.norm(B, np.inf) # chuẩn vo cung của ma trận B

x0 = np.zeros_like(b) # khởi tạo x0 ( ma tran khong)

i = 0 # số lần lặp

eps0 = ((1 - norm_B) * eps) / norm_B

d = np.dot(T, b)

x1 = np.dot(B, x0) + d

while np.linalg.norm((x1 - x0), np.inf) > eps0 :
    x0 = x1
    x1 = np.dot(B, x0) + d
    i += 1
    print(x1)

print("so lan lap:" + str(i))

# nghiệm : [0.150985, 0.259998, 0.162880, 0.3085823]

# Nghiem dung numpy
# print(np.linalg.solve(A, b))