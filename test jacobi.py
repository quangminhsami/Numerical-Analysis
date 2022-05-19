# 4x1 - x2 - x3 = 3
# -2x1 + 6x2 + x3 = 9
# -x1 + x2 + 7x3 = -6

# initial estimate = [0,0,0]

# x(k+1) = inv(D)[(-L-U)x(k) + b]

from numpy import array, diag, diagflat, dot
import numpy as np 
from numpy.linalg import inv

# number of iteration
'''A = array([[4.0, -1.0, -1.0],
          [-2.0, 6.0, 1.0],
          [-1.0, 1.0, 7.0]])'''

A = np.loadtxt("data5.txt", dtype = float)

b = array([3.0, 9.0, -6.0])

guess = array([0.0, 0.0, 0.0]) # khởi tạo x(0)

U = np.triu(A,1) # ma trận tam giác trên của A
L = np.tril(A,-1)    # ma trận tam giác dưới của A

# print(U)
# print(L)

minus_L_minus_U = -L - U

D = diagflat(diag(A))  # ma trận đường chéo của A
# print(D)

inv_of_D = inv(D) # ma trận nghịch đảo của D
# print(inv_of_D)

# x(k+1) = inv(D)[(-L-U)x(k) + b]

N = 15 # số lần lặp
for i in range(N):
    minus_L_minus_U_dot_x_plus_b = dot(minus_L_minus_U, guess) + b
    guess = dot(inv_of_D, minus_L_minus_U_dot_x_plus_b)
    print(i+1, np.round(guess, 5))