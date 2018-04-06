import urllib as url
import re
from walkerScrape import findclass

schedule = []

def lS2(c, a):
    for i in xrange(len(schedule)):#need to check type and if list == true run thru that list
        if type(c[a]) == list and type(schedule[i]) == list:#and schedule[i] is a list
            for j in xrange(len(c[a])):
                for d in xrange(len(schedule[i])):
                    if c[a][j] == schedule[i][d]:
                        print "Conflict!"
                        return
    schedule.append(c[0])
    schedule.append(c[a])

while True:
    key = raw_input("What course would you like to search? ")
    class1 = findclass(key)
    print class1

    num = raw_input("Which time slot would you like to add? (Starting with 1) ")
    lS2(class1, int(num))
    print "Current Schedule: ",schedule
