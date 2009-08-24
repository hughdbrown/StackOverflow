import itertools
import pprint
import operator

alpha, charlie, norway, england = range(4)

a = [{"value1": 1234, "value2": 23423423421, "value3": norway, "value4": charlie},
     {"value1": 1398, "value2": 23423412221, "value3": england, "value4": alpha}, 
     {"value1": 1234, "value2": 23234231221, "value3": norway, "value4": charlie}, 
     {"value1": 1398, "value2": 23423213121, "value3": england, "value4": alpha}]


getvals = operator.itemgetter('value1', 'value3', 'value4')

a.sort(key=getvals)

b = [g.next() for _, g in itertools.groupby(a, getvals)]
pprint.pprint(b)
