import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import re
import socket

soup = BeautifulSoup(open("Export.html"))

for br in soup.findAll('br'):
    next = br.nextSibling # Grabs Nested Br text
    if not (next and isinstance(next,NavigableString)):
        continue
    next2 = next.nextSibling
    if next2 and isinstance(next2,Tag) and next2.name == 'br':
        next = next.split(',')
        text = re.sub(r'.*:\/\/|\/.*','',next[0])
        try:
            if bool(socket.gethostbyname(text)):
                r = requests.get('http://cloudbleedcheck.com/?domain=' + text)
                matched_soup = BeautifulSoup(r.content)
                check_if = matched_soup.findAll("p", id= "result-msg")
                if str(check_if[0].contents[0]) == "This domain name is affected":
                    print(str(check_if[0].contents[0]) + ": " + text)
            else:
                print("Did not respond " + text)
        except:
            pass # used to pass notes that are in the password store









