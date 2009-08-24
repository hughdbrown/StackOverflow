#!/usr/bin/env python
from __future__ import with_statement

def reformat(s):
    return s.replace('\n', r'\n').replace('\t', r'\t')

def reformat_file(filename):
    with open(filename) as f:
        return reformat(f.read())

if __name__ == '__main__':
    import sys
    s = ".replace(r'\\\\n', r'\\n').replace(r'\\\\t', r'\\t')"
    for arg in sys.argv[1:]:
        print r'print "' + reformat_file(arg) + r'"' + s
