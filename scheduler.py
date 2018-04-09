import urllib as url
import re
from walkerScrape import findclass

schedule = []
conflict = False

def lS2(c, a):
    for i in xrange(len(schedule)):#need to check type and if list == true run thru that list
        if type(c[a]) == list and type(schedule[i]) == list:#and schedule[i] is a list
            for j in xrange(len(c[a])):
                for d in xrange(len(schedule[i])):
                    if c[a][j] == schedule[i][d]:
                        conflict = True
                        print "Conflict!"
                        return
    schedule.append(c[0])
    schedule.append(c[a])


def addClasses(a):
    count = 1
    print "Current Schedule: ", schedule
    for idx, j in enumerate(a):
        class1 = findclass(j)
        lS2(class1,count)
        if conflict == True:
            count = count + 1
        else:
            count = 1
        if count > (len(class1)-1):
            del schedule[:]
            a = rotate(a,idx)
            if a == startA:
                print "Sorry no possible schedule."
                break
            else:
                addClasses(a)

def rotate(l, n):
    return l[n:] + l[:n]

xlist = []
for i in xrange(5):
    x = raw_input("Enter a class name you'd like to add (i.e. CPE 593): ")
    xlist.append(x)
startA = xlist
addClasses(xlist)
#xlist = [a for a in xlist] #turns raw input into a string of floating point values

print schedule
