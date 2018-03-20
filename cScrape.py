import urllib2 as url
import re
from bs4 import BeautifulSoup

f = open("htmldata.txt", "wr")

site = "http://personal.stevens.edu/~gliberat/registrar/16f/16f_u.html#CPE"
page = url.urlopen(site)
soup = BeautifulSoup(page, "html.parser")
data = soup.findAll(text=True)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True
    #gets all text

result = filter(visible, data)
l = list(result) #puts text in a list
count = 0#used a separate counter from the for loop because of errors with type

all_links = soup.find_all("a")#finds every new class line basically
#only using text so no need to look for tags b/c website is weird
for link in all_links:
	f.write(l[count])
	# f.write(str('\n'))
	count = count + 1
f.close()
