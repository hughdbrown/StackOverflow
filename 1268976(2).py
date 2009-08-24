import urllib2
from BeautifulSoup import BeautifulSoup
import re

url = "http://forums.epicgames.com/archive/index.php?f-356-p-164.html"
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

pattern = r'<a href="http://forums.epicgames.com/archive/index.php?t-([0-9]+).html">(.?+)</a> <i>((.?+) replies)'
#pattern = r'href="http://forums.epicgames.com/archive/index.php?t-622233.html">Gears of War 2: Horde Gameplay</a> <i>(20 replies)'

for match in re.finditer(pattern, page, re.S):
    print match(0)
