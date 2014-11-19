import requests
from bs4 import BeautifulSoup

import sqlite3
##thematics for quotes
theme = "amour"
## iterator
i = 0
## list of quotes
line = [u'']
## temp_quote
linet = u''

source = requests.get("http://evene.lefigaro.fr/citations/mot.php?mot="+theme)
content = source.text
soup = BeautifulSoup(content)
##
for things in soup.find_all('h3')
    for thing in things.stripped_strings
        linet = u''.join([linet,unicode(thing)])
    line[i] = linet
    i = i + 1
for k in range(1,i)
    print line[k]
