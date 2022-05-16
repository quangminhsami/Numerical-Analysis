# toang quá 
import numpy as np

eps = float(input()) # nhập sai số 

# nhập ma trận A là ma trận chéo trội hàng
A = np.array([[-19,7,5,4],
              [0,10,2,-3],
              [1,-5,16,5],
              [-6,1,2,14]])

# Nhập vector b
b = np.array([1,2,3,4])

# ma trận đơn vị của A
I = np.zeros_like(A)

# ma trận đường chéo của A
T = np.linalg.inv((np.diag(A)))
# print(T)

B = I - np.dot(T, A)

norm_B = np.linalg.norm(B, np.inf) # chuẩn 1 của ma trận B

x0 = np.zeros_like(b) # khởi tạo x(0)

i = 0 # số lần lặp

eps0 = ((1 - norm_B) * eps) / norm_B

x1 = np.dot(B, x0) + np.dot(T, b)

'''while np.linalg.norm((x1 - x0), np.inf) > eps0 :
    x0 = x1
    x1 = np.dot(B, x0) + np.dot(T, b)
    i += 1
    print(x1)

# nghiệm : [0.150985, 0.259998, 0.162880, 0.3085823]'''