import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import time

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Darius.html'
print("Retrieving:", url)
try:
    html = urllib.request.urlopen(url, context=ctx).read()
except ConnectionResetError:
    html = urllib.request.urlopen(url, context=ctx).read()
    
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
reps = 7
position = 18

tags = soup('a')
for rep in range(reps):
    url = tags[position-1].get('href')
    print("Retrieving:", url)
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        time.sleep(2)
    except ConnectionResetError:
        html = urllib.request.urlopen(url, context=ctx).read()
        time.sleep(2)
        
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
