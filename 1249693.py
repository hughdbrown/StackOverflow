#!/usr/bin/env python

import collections

cache = None

def dice_count(dice_left, die_pips, count_so_far, count_req):
    global cache
    needed = count_req - count_so_far
    if dice_left == 0:
        yield (1 if (needed==0) else 0)
    elif dice_left == 1:
        yield (1 if (1 <= needed <= die_pips) else 0)
    else:
        lower = 1
        upper = min(die_pips+1, count_req - count_so_far)
        s = 0
        for i in range(lower, upper):
            t = (dice_left-1, count_so_far + i)
            if not (t in cache):
                cache[t] = sum(dice_count(dice_left-1, die_pips, count_so_far+i, count_req) )
            s += cache[t]
        yield s

def all_dice_count(dice_left, die_pips, count_req):
    global cache
    cache = collections.defaultdict(int)
    return sum(dice_count(dice_left, die_pips, 0, count_req))

x = all_dice_count(dice_left=100, die_pips=6, count_req=100)
print "Rolling 100 with 100 6-sided dice: ", x, " ways"

x = all_dice_count(dice_left=100, die_pips=6, count_req=101)
print "Rolling 101 with 100 6-sided dice: ", x, " ways"

x = all_dice_count(dice_left=100, die_pips=6, count_req=102)
print "Rolling 102 with 100 6-sided dice: ", x, " ways"
