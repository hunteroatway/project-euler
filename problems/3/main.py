n = 600851475143

def lpf(n):
	p = 2
	while n > p:
		if n % p  == 0:
			n = n / p
			p = 2
		else:
			p += 1
	return p

print(lpf(n))
