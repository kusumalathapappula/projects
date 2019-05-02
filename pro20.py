def factorial(n):
	fact = 1
	while n > 0:
		fact = fact * n
		n = n-1
	return fact
num = factorial(100)
sum = 0
while num > 0:
	rem = num % 10
	sum = sum + rem
	num = num // 10
print(sum)



	

