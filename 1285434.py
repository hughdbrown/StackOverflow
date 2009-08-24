def _concat(a, b):
    la = len(a)
    for i in range(la):
        if a[i:] == b[:la-i]:
            return a + b[la-i:]
    return a + b

def concat(*args):
    result = ''
    for arg in args:
        result = _concat(result, arg)
    return result


if __name__ == '__main__':
    assert concat('a', 'b', 'c') == 'abc'
    assert concat('abcde', 'defgh', 'ghlmn') == 'abcdefghlmn'
    assert concat('abcdede', 'dedefgh', '') == 'abcdedefgh'
    assert concat('abcde', 'd', 'ghlmn') == 'abcdedghlmn'
    assert concat('abcdef', '', 'defghl') == 'abcdefghl'

