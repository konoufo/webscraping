import requests
from bs4 import BeautifulSoup

import sqlite3


##thematics and language for quotes
lang = "fr"
theme = "amour"
## iterator
i = 0
## quote_checker
checker = u'\xab'
## list of quotes
line = [u'']
## temp_quote
linet = u''

source = requests.get("http://evene.lefigaro.fr/citations/mot.php?mot="+theme)
content = source.text
soup = BeautifulSoup(content)
##
for things in soup.find_all('h3'):
    for thing in things.stripped_strings:
        string_thing = unicode(thing)
        linet = u' '.join([linet,string_thing])
    if checker in linet:
        line.append(linet)
        i = i + 1
## open database
db = sqlite3.connect('c:/quotes.sqlite')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS quotes(id INTEGER PRIMARY KEY, quoted TEXT unique,
                thematics TEXT, lang TEXT)''')
db.commit

for k in range(1,i-1):
## test to check only quotes are scraped
##    print repr(line[k])
##print repr(u'" ')
    try:
        cursor = db.cursor()
        cursor.execute('''INSERT INTO quotes(quoted, thematics, lang) VALUES (?,?,?)''',(line[k], theme, lang))
    except sqlite3.IntegrityError:
        ## doublon spoted !
        continue
db.commit()
db.close()
