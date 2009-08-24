#!/usr/bin/env python

import psyco
psyco.full()

import multiprocessing
import threading
from time import time

def print_timing(func):
    def wrapper(*arg):
        t1 = time()
        res = func(*arg)
        t2 = time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper


def counter():
    reps = 1000 * 1000
    for i in xrange(reps):
        pass

@print_timing
def serialrun(x):
    for _ in xrange(x):
        counter()

@print_timing
def parallelpoolrun(reps):
    pool = multiprocessing.Pool()
    results = [pool.apply_async(counter) for rep in range(reps)]
    [result.get() for result in results]


@print_timing
def parallelrun(x):
    proclist = [multiprocessing.Process(target=counter) for _ in xrange(x)]
    [p.start() for p in proclist]
    [p.join() for p in proclist]
        

@print_timing
def threadedrun(x):
    threadlist = [threading.Thread(target=counter) for _ in xrange(x)]
    for t in threadlist: t.start()
    for t in threadlist: t.join()

def main(reps):
    multiprocessing.freeze_support()
    serialrun(reps)
    parallelrun(reps)
    parallelpoolrun(reps)
    threadedrun(reps)

if __name__ == '__main__':
    main(100)
