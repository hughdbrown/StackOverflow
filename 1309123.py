import psyco
psyco.full()

from random import randint
import datetime

if __name__ == '__main__':
	upper = 10*1000*1000
	s = datetime.datetime.now()
	d = dict((i, "".join(["1"]*i)) for i in range(1, 10))
	for _ in xrange(upper):
		y = int(d[randint(1,9)])
	e = datetime.datetime.now()
	print upper
	print "Elapsed: ", (e - s)
