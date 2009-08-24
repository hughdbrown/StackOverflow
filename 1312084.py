import psyco
psyco.full()

def is_prime(n):
	a = list(range(n+1))
	a[2] = 0
	for mark in range(4, n, 2):
		a[mark] = 2
	upper = 1+int(n ** 0.5)
	for i in range(3, len(a), 2):
		if a[i] == i:
			a[i] = 0
			for mark in range(i*i, len(a), i):
				a[mark] = i
	return a[n] == 0

if __name__ == '__main__':
	for i in range(2, 40):
		print i, is_prime(i)
	print 12163781, is_prime(12163781)
	print 640199, is_prime(640199)
	print 91457, is_prime(91457)
