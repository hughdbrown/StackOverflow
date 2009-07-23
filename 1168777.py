#!/usr/bin/env python
import re

paragraph = "I eat bananas and a banana " * 1000
targets = [x for _ in range(100) for x in ['banana', 'loganberry', 'passion fruit'] ]

def map_test_re():
    global targets, paragraph
    def tester(x):
        return len(re.findall(x,paragraph))
    return map(tester, targets)

def map_test_count():
    global targets, paragraph
    #def tester(x):
    #    return paragraph.count(x)
    #return map(tester, targets)
    return map(paragraph.count, targets)

def lc_test_count():
    global targets, paragraph
    #def tester(x):
    #    return paragraph.count(x)
    #return [tester(target) for target in targets]
    return [paragraph.count(target) for target in targets]

def map_test_closure():
    global targets, paragraph
    def tester(s): 
        def f(x):
            return len(re.findall(x,s))
        return f
    return map(tester(paragraph), targets)


def lc_test_re():
    global targets, paragraph
    def tester(x):
        return len(re.findall(x,paragraph))
    return [tester(target) for target in targets]

if __name__ == '__main__':
    from timeit import Timer
    fns = ['lc_test_count()', 'lc_test_re()', 'map_test_count()', 'map_test_re()', 'map_test_closure()']
    for fn in fns:
        t = Timer(fn, "from __main__ import lc_test_count, lc_test_re, map_test_count, map_test_re, map_test_closure")
        print fn, 1000 * t.timeit(3)

