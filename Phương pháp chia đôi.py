import math

def func(x): # Ham f(x)
    return math.log(x) - 1

# Kiem tra khoang cach ly nghiem

print("Nhập khoảng cách ly nghiệm a và b:")
print("Nhập a = ")
a = float(input())
print("Nhập b = ")
b = float(input())
print("Nhập sai số epxilon = ")
epxilon = float(input())

if func(a) * func(b) > 0: 
	print("Khoảng cách ly không hợp lệ")
else: # chia doi
	if func(a) - 1 > 0:
		sig = 1
	else:
		sig = -1

	i = 0

	c = (a + b) / 2

	while b - a >= epxilon:
		z = func(c) - 1
		if z == 0:
			print("Số e gần đúng là" + " " + str(c))
		else:
			if z * sig > 0:
				a = (a + b) / 2
			else:
				b = (a + b) / 2
		c = (a + b) / 2
		i += 1
		print("Số e gần đúng là" + " " + str(c))
	print("số lần lặp : " + str(i))





 
