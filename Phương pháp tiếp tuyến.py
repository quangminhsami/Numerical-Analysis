import math

def func(x):
    return math.log(x) - 1

def func_phay(x):
    return 1 / x

def func_2phay(x):
    return -1 / (x * x)

print("Nhập khoảng cách ly nghiệm a và b:")
print("Nhập a = ")
a = float(input())
print("Nhập b = ")
b = float(input())
print("Nhập sai số epxilon = ")
epxilon = float(input())

m_1 = min(func_phay(a),func_phay(b))

i = 0 # số lần lặp

epxilon_0 = m_1 * epxilon

if func(a) * func_2phay(a) > 0:
    x_0 = a
    while math.fabs(func(x_0)) > epxilon_0:
        x_0 = x_0 - func(x_0) / func_phay(x_0)
        i += 1
        print("Số e gần đúng : " + str(x_0))
    
if func(b) * func_2phay(b) > 0:
    x_0 = b
    while math.fabs(func(x_0)) > epxilon_0:
        x_0 = x_0 - func(x_0) / func_phay(x_0)
        print("Số e gần đúng : " + str(x_0))

print("Số lần lặp: " + str(i))

