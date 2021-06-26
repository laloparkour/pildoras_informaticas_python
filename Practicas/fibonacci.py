a = 0
b = 1
f = 0

x = 0
print("0, ", end="")
while x <= 11:
	f = a + b
	b = a
	a = f
	print(f, end=", ")
	x += 1
