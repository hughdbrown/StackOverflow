#!/usr/bin/env python
import psyco
psyco.full()
import math
import random

def find_duplicate2(arr, gap):
    cost, reps = 0, 0
    while True:
        indexes = sorted((random.randint(0,len(arr)-i-1) for i in xrange(gap)), reverse=True)
        selection = [arr.pop(i) for i in indexes]
        selection_set = set(selection)
        cost += len(selection)
        reps += 1
        if len(selection) > len(selection_set):
            return cost, reps

def find_duplicate(total, half, gap):
    cost = 0
    reps = 0
    while True:
        indexes = [random.randint(0,total-i-1) for i in range(gap)]
        cost += gap
        reps += 1
        above_half = [i for i in indexes if i >= half]
        if len(above_half) >= 2:
            return cost, reps
        else:
            total -= len(indexes)
            half -= (len(indexes) - len(above_half))

#if __name__ == '__main__':
#    import sys
#    import copy
#    import collections
#    orig = list(range(500*1000)) + [600*1000] * 500*1000
#    gap = 1 + int(math.log10(len(orig)) / math.log10(2))
#    total_cost = 0
#    d = collections.defaultdict(int)
#    #print len(orig), gap
#    #mod = 100
#    for i in range(1000*100):
#        arr = copy.copy(orig)
#        cost, reps = find_duplicate(arr, gap)
#        d[reps] += 1
#        total_cost += cost
#        #if i % mod == (mod-1):
#        #    print >> sys.stderr, i, total_cost, "           \r",
#    #print
#    print total_cost
#    for k in sorted(d.keys()):
#        print k, d[k]


if __name__ == '__main__':
    import sys
    import collections
    import datetime
    results = {}
    for total in [2**i for i in range(5, 21)]:
        half = total // 2
        log = int(math.ceil(math.log10(total) / math.log10(2)))
        #gap = log
        gap = 3
        d = collections.defaultdict(int)
        total_cost, total_reps = 0, 1000*1000*10
        s = datetime.datetime.now()
        for _ in xrange(total_reps):
            cost, reps = find_duplicate(total, half, gap)
            d[reps] += 1
            total_cost += cost
        e = datetime.datetime.now()
        print "Elapsed: ", (e - s)
        print "%d elements" % total
        print "block size %d (typically log of # elements)" % gap
        for k in sorted(d.keys()):
            print k, d[k]
        average_cost = float(total_cost) / float(total_reps)
        average_logs = average_cost / log
        print "Total cost: ", total_cost
        print "Average cost in accesses: %f" % average_cost
        print "Average cost in logs: %f" % average_logs
        print
        results[total] = average_logs
    for r in sorted(results.keys()):
        print r, result[r]


