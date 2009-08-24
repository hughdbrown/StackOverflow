#!/usr/bin/env python

try:
    import psyco
    psyco.full()
except ImportError:
    pass

def encode(s):
    def calc_count(count, c):
        return count * (-1 if c == '0' else 1)
    result = []
    c = s[0]
    count = 1
    for i in range(1, len(s)):
        d = s[i]
        if d == c:
            count += 1
        else:
            result.append(calc_count(count, c))
            count = 1
            c = d
    result.append(calc_count(count, c))
    return result

def search(encoded_source, targets):
    def match(encoded_source, t, max_search_len, len_source):
        x = len(t)-1
        # Get the indexes of the longest segments and search them first
        most_restrictive = [bb[0] for bb in sorted(((i, abs(t[i])) for i in range(1,x)), key=lambda x: x[1], reverse=True)]
        # Align the signs of the source and target
        index = (0 if encoded_source[0] * t[0] > 0 else 1)
        unencoded_pos = sum(abs(c) for c in encoded_source[:index])
        start_t, end_t = abs(t[0]), abs(t[x])
        for i in range(index, len(encoded_source)-x, 2):
            if all(t[j] == encoded_source[j+i] for j in most_restrictive):
                encoded_start, encoded_end = abs(encoded_source[i]), abs(encoded_source[i+x])
                if start_t <= encoded_start and end_t <= encoded_end:
                    return unencoded_pos + (abs(encoded_source[i]) - start_t)
            unencoded_pos += abs(encoded_source[i]) + abs(encoded_source[i+1])
            if unencoded_pos > max_search_len:
                return len_source
        return len_source
    len_source = sum(abs(c) for c in encoded_source)
    i, found, target_index = len_source, None, -1
    for j, t in enumerate(targets):
        x = match(encoded_source, t, i, len_source)
        print "Match at: ", x
        if x < i:
            i, found, target_index = x, t, j
    return (i, found, target_index)

if __name__ == "__main__":
    import datetime
    def make_source_text(len):
        from random import randint
        item_len = 8
        item_count = 2**item_len
        table = ["".join("1" if (j & (1 << i)) else "0" for i in reversed(range(item_len))) for j in range(item_count)]
        return "".join(table[randint(0,item_count-1)] for _ in range(len//item_len))
    targets = ['0001101101'*2, '01010100100'*2, '10100100010'*2]
    encoded_targets = [encode(t) for t in targets]
    data_len = 10*1000*1000
    s = datetime.datetime.now()
    source_text = make_source_text(data_len)
    e = datetime.datetime.now()
    print "Make source text(length %d): " % data_len,  (e - s)
    s = datetime.datetime.now()
    encoded_source = encode(source_text)
    e = datetime.datetime.now()
    print "Encode source text: ", (e - s)
    
    s = datetime.datetime.now()
    (i, found, target_index) = search(encoded_source, encoded_targets)
    print (i, found, target_index)
    print "Target      : ", targets[target_index]
    print "Source match: ", source_text[i:i+len(targets[target_index])]
    e = datetime.datetime.now()
    print "Search time: ", (e - s)

