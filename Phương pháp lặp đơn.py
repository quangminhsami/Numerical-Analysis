import math

def func(x):
    return 1 / (1 + math.exp(-x))

def func_phay(x):
    return math.exp(x) / ((1 + math.exp(x)) * (1 + math.exp(x)))

def func_2phay(x):
    return - math.exp(-x) * (math.exp(x) - 1) / math.pow((math.exp(x) + 1),3)

print("Nhập khoảng cách ly nghiệm a và b:")
print("Nhập a = ")
a = float(input())
print("Nhập b = ")
b = float(input())
print("Nhập xấp xỉ đầu x_0 = ")
x_0 = float(input())
print("Nhập sai số epxilon = ")
epxilon = float(input())

q = max(math.fabs(func_phay(a)), math.fabs(func_phay(b))) 

epxilon_0 = epxilon * (1 - q) / q

x_1 = func(x_0)

i = 0   # số lần lặp

while math.fabs(x_1 - x_0) > epxilon_0:
    x_0 = x_1
    x_1 = func(x_0)
    i += 1
    print("Nghiệm của phương trình là " + str(x_1))
print("Số lần lặp: " + str(i))
    
# Nghiem pt x = 1/(1 + e^(-x)) la x = 0.659046



