import courseScrape as scrape
import itertools as it
schedule = []
#I want to change it so it asks which time from the class list to add rather than inputting a time because the user can input anything

fallSite = "http://personal.stevens.edu/~gliberat/registrar/17f/17f_u.html"
springSite = "http://personal.stevens.edu/~gliberat/registrar/17s/17s_u.html"

schedule = []
conflict = False
count2 = 0

def lS2(c, a):
    global conflict
    conflict = False
    for i in xrange(len(schedule)):#need to check type and if list == true run thru that list
        if type(c[a]) == list and type(schedule[i]) == list:#and schedule[i] is a list
            for j in xrange(len(c[a])):
                for d in xrange(len(schedule[i])):
                    if c[a][j] == schedule[i][d]:
                        conflict = True
                        print "Conflict!"
                        return
    if conflict == False:
        schedule.append(c[0])
        schedule.append(c[a])


def addClasses(a):
    global conflict, count, count2
    count = 2#xlist[2] is where class times start

    for idx, j in enumerate(a):#go thru/number the list of classes
        class1 = scrape.courseScrape(j,False, fallSite)#nth class is class1
        for i in range(1, len(class1)):
            lS2(class1,count)#search for conflict starting at first time
            if conflict:#if there's a conflict increment count to check next time
                count = count + 1
            else:
                count = 2#reset count if no conflict
                break
            if len(schedule)/2 == len(xlist):
                print "Final schedule: ", schedule
                exit()
            if count == (len(class1)):#delete schedule and rotate order and start again
                count = 2
                print "Current Schedule: ", schedule
                del schedule[:]
                count2 = count2+1
                print "NEW PERMUTATION"
                #a = rotate(a,idx)
                if count2 > len(b):
                    print "Sorry no possible schedule."
                    exit()
                else:
                    addClasses(b[count2])

def rotate(l, n):
    return l[n:] + l[:n]

xlist = []
# for i in xrange(5):
#     x = raw_input("Enter a class name you'd like to add (i.e. CPE 593): ")
#     xlist.append(x)
# startA = xlist
xlist = ["CPE 593", "CPE 390", "CPE 345"]#doesnt work
b = list(it.permutations(xlist, len(xlist)))
addClasses(xlist)
#xlist = [a for a in xlist] #turns raw input into a string of floating point values

print schedule
