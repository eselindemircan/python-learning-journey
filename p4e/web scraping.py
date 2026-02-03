
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_2346296.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
total=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    tagm=str(tag)
    choosen=re.findall('comments">([0-9]+)<',tagm)
    sayi=int(choosen[0])
    total=total+sayi
    #alternative 
    #for tag in tags:
    #total += int(tag.text)
print(total)   
