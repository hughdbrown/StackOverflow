#!/usr/bin/env python

def is_sublist2(cand, lists):
    s = set(cand)
    for target in lists:
        if len(cand) <= len(target):
            # quick test to see if any match is possible
            if s <= set(target):
                # perform ordered test
                for c in cand:
                    i = target.index(c)
                    if i >= 0:
                        target = target[i+1:]
                    else:
                        break
                else:
                    return True
    return False

def is_sublist_of_any_list(cand, lists):
    def is_sublist_of_list(cand, target):
        try:
            i = 0
            for c in cand:
                i = 1 + target.index(c, i)
            return True
        except ValueError:
            return False
    return any(is_sublist_of_list(cand, target) for target in lists if len(cand) <= len(target))

# Compare candidates to all other lists
def super_lists(lists):
    return [cand for i, cand in enumerate(lists) if not is_sublist_of_any_list(cand, lists[:i] + lists[i+1:])]

if __name__ == '__main__':
    lists = [[1, 2, 4, 8], [1, 2, 4, 5, 6], [1, 2, 3], [2, 3, 21], [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7]]
    superlists = super_lists(lists)
    print superlists


