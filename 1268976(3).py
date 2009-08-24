#!/usr/bin/env python


import urllib2
import re
from BeautifulSoup import BeautifulSoup

url = "http://forums.epicgames.com/archive/index.php?f-356-p-164.html"
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

# Get all the links
links = [str(match) for match in soup('a')]

s = r'<a href="http://forums.epicgames.com/archive/index.php\?t-\d+.html">(.+?)</a>' 
#s = r'<a href="http://forums.epicgames.com/archive/index.php(.+?)</a>' 
r = re.compile(s)
for link in links:
    m = r.match(link)
    if m:
        print m.groups(1)[0]
