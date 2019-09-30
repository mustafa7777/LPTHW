from sys import argv

script, input_file = argv

def fileprint(f):
    print f.read()
    
def linereset(f):
    f.seek(0)

def linewrite(linecount, f):
    print linecount, f.readline()
    
currentfile = open(input_file)

print "First lets print the file:\n"

fileprint(currentfile)

print "now lets reset the line count....done\n"

linereset(currentfile)

print "now lets print the lines one by one:\n"

curline = 1
linewrite(curline, currentfile)

curline = curline + 1
linewrite(curline, currentfile)

curline = curline + 1
linewrite(curline, currentfile)

curline = curline + 1
linewrite(curline, currentfile)
