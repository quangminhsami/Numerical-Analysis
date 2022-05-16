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

i = 0 # số lần lặp

if func(a) * func(b) < 0  and func_phay(a) * func_phay(b) > 0 and func_2phay(a) * func_2phay(b) > 0:
    if (func(a) * func_2phay(a) > 0):
        d = a 
        x_0 = b
    else:
        d = b 
        x_0 = a

    F_d = func(d)

    M1 = max(math.fabs(func_phay(a)), math.fabs(func_phay(b)))
    m1 = min(math.fabs(func_phay(a)), math.fabs(func_phay(b)))

    epxilon_0 = (epxilon * m1) / (M1 - m1) 
    F_0 = func(x_0)
    x_1 = (x_0 - F_0 * (x_0 - d)) / (F_0 - F_d)

    while math.fabs(x_1 - x_0) >= epxilon_0:
        x_0 = x_1
        F_0 = func(x_0)
        x_1 = x_0 - ((F_0 * (x_0 - d)) / (F_0 - F_d))
        i += 1
        print("Số e gần đúng là: " + str(x_1))
else:
    print("Ko hợp lệ")

print("Số lần lặp là: " + str(i))


