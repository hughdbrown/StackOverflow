import sys
import codecs

#buildLog = open(sys.argv[1])
buildLog = codecs.open(sys.argv[1], "r", "utf-16")

match = u'buildLog'
for line in buildLog:
    if line.decode("iso-8859-1").find(match) >= 0:
        print line
