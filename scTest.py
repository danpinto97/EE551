import urllib2 as url
import re
from bs4 import BeautifulSoup

f = open("htmldata.txt", "wr")
site = "http://personal.stevens.edu/~gliberat/registrar/16f/16f_u.html#CPE"
page = url.urlopen(site)
soup = BeautifulSoup(page, "html.parser")
#days = soup.find_all("font", text = "This section is offered at:")
#f.write(soup.prettify())
data = soup.findAll(text=True)
# title = soup.title.text
# body = soup.find(text="DAY").findNext('#text')
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

result = filter(visible, data)
l = list(result)
print l[40]
count = 0
#print list(result)
#print body.text
all_links = soup.find_all("a")
for link in all_links:
	f.write(str(link.get("name")))
	f.write(str('\n'))
	f.write(l[count])
	f.write(str('\n'))
	count = count + 1
	#print days
	# f.write(str(link.get("Day")))
	# f.write(str('\n'))
f.close()


# count = 0
# f = open("htmldata.txt", 'r')
# d = open("htmldata2.txt", "wr")
# for line in f:
# 	if line.startswith("None"):
# 		count = count + 1
# 	else:
# 		d.write(line)
