import urllib2 as url
from bs4 import BeautifulSoup 

f = open("htmldata.txt", "wr")
site = "http://personal.stevens.edu/~gliberat/registrar/16f/16f_u.html#CPE"
page = url.urlopen(site)
soup = BeautifulSoup(page)

#f.write(soup.prettify())

all_links = soup.find_all("a")
for link in all_links:
	f.write(str(link.get("name")))
	f.write(str('\n'))
f.close()
count = 0
f = open("htmldata.txt", 'r')
d = open("htmldata2.txt", "wr")
for line in f:
	if line.startswith("None"):
		count = count + 1
	else:
		d.write(line)