#!/usr/bin/env python
from __future__ import with_statement

import re
import collections

def get_values(file):
    d = collections.defaultdict(list)
    dir = ""
    dir_regex = re.compile(r'^Directory: (.+?)\\$')
    file_regex = re.compile(r'^-> (.+?)$', 128)
    with open(file) as f:
        for line in f:
            line = line.strip()
            match = dir_regex.search(line)
            if match:
                dir = match.group(1)
            else:
                match = file_regex.search(line)
                if match:
                    d[dir].append(match.group(1))
    return d

if __name__ == '__main__':
    d = get_values('test_file')
    for k, v in d.items():
        print k, v

