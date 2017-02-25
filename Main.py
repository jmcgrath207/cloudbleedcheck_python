import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import re
import socket
import zipfile
import tempfile

soup = BeautifulSoup(open("Export.html"))
r = requests.get('https://github.com/pirate/sites-using-cloudflare/archive/master.zip')

with tempfile.NamedTemporaryFile() as temp:
    temp.write(r.content)
    temp.flush()
    zip_ref = zipfile.ZipFile(temp.name, 'r')
    read = zip_ref.read(zip_ref.filelist[5].filename)
    read = read.split(b'\n')

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
                if str.encode(text) in read and not text == '':
                    print("This domain name is affected: "  + text)
            else:
                print("Did not respond dns lookup " + text)
        except:
            pass # used to pass notes that are in the password store









