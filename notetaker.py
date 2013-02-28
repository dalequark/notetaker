import datetime, sys, getopt, os

className = "cos436"
myName = "Dale Markowitz"

todaysDate = datetime.datetime.now().strftime('%d_%b_%G')

#get params

try:
	args, opts = getopt.getopt(sys.argv[1:],["precept", "lecture"])
except getopt.GetoptError as err:
	print str(err)
	sys.exit(2)

#check to see if we've been given proper params 

if not opts:
	print "missing parameter 'precept' or 'lecture'"
	sys.exit(2)

fileName =  todaysDate + "_" + className + "_" + opts[0] + ".txt"

newnotes = open(fileName, "wb")

newnotes.write("Name: " + myName + "\n\n")
newnotes.write("Date: " + todaysDate + "\n\n")
newnotes.write(className + " " + opts[0] + "\n\n")
newnotes.write("Title: " + "\n")
for x in xrange(1,5):
	newnotes.write('\n')


newnotes.close()


os.system("open -a 'Sublime Text 2' " + fileName)