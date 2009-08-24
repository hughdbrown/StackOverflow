import collections
import datetime
import random

def simulate_list(n, reps, lower, upper):
	rr = random.random
	a = list(range(n))
	for i in xrange(reps):
		r = rr()
		append = (len(a) < lower or r >= 0.5)
		if append:
			a.append(37)
		else:
			a.pop(0)

def simulate_deque(n, reps, lower, upper):
	rr = random.random
	a = collections.deque(range(n))
	for i in xrange(reps):
		r = rr()
		append = (len(a) < lower or r >= 0.5)
		if append:
			a.append(37)
		else:
			a.popleft()

if __name__ == '__main__':
	init_size, reps = 10000, 1*1000*1000
	lower, upper = int(0.9 * init_size), int(1.1 * init_size)

	s = datetime.datetime.now()
	simulate_list(init_size, reps, lower, upper)
	e = datetime.datetime.now()
	print "List: ", (e - s)

	s = datetime.datetime.now()
	simulate_deque(init_size, reps, lower, upper)
	e = datetime.datetime.now()
	print "Deque: ", (e - s)
