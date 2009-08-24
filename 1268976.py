#!/usr/bin/env python

import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://forums.epicgames.com/archive/index.php?f-356-p-164.html"
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

links = [str(match) for match in soup('a')]
print len(links), " links"

import re

s = r'<a href="http://forums.epicgames.com/archive/index.php\?t-([0-9]+).html">(.+?)</a>( <i>\(([0-9]+?) replies\))'
s = r'<a href="http://forums.epicgames.com/archive/index.php\?t-([0-9]+).html">(.+?)</a>'
#s = r'<a href="forums.epicgames.com/archive/index.php\?t-([0-9]+).html">'
#s = r'<a href="forums.epicgames.com/archive/index.php'
#s = r'<a href="http://forums.epicgames.com/archive/'
regex = re.compile(s)
for link in links:
    if regex.match(link):
        print link

print "replies" in page
print "forums.epicgames.com" in page

