import numpy as np

eps = float(input()) # nhập sai số 

# nhập ma trận A là ma trận chéo trội cot
'''A = np.array([[-19,2,5,1],
                 [0,10,2,-3],
                 [1,-5,16,5],
                 [-6,1,2,14]])'''

# Nhap ma tran A tu file
A = np.loadtxt("data6.txt", dtype= float)

# Nhập vector b
b = np.array([1,2,3,4])

# kich thuoc theo hang cua ma tran A
n,_ = np.shape(A)

# ma trận đơn vị của A
I = np.identity(n) 

# ma trận đường chéo của A
T = np.linalg.inv(np.diag(np.diag(A)))

B = I - np.dot(T, A)

norm_B = np.linalg.norm(B, 1) # chuẩn 1 của ma trận B

x0 = np.zeros_like(b) # khởi tạo x0 ( ma tran khong)

i = 0 # số lần lặp

lst = np.diag(A)
# print(lst)

lamda = max(abs(lst)) / min(abs(lst))
# print(lamda) 

eps0 = ((1 - norm_B) * eps) / ( lamda * norm_B)

d = np.dot(T, b)

x1 = np.dot(B, x0) + d

while np.linalg.norm((x1 - x0), 1) > eps0 :
    x0 = x1
    x1 = np.dot(B, x0) + d
    i += 1
    print(x1)

print("so lan lap:" + str(i))

# nghiệm : [0.03374486 0.24108553 0.18035814 0.25719052]

# Nghiem dung numpy
# print(np.linalg.solve(A, b))