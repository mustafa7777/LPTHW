from sys import argv
script, input_file = argv

def filedisplay(f):
    print f.read()
    
def linerestart(f):
    f.seek(0)
    
def lineprint(line_count, f):
    print line_count, f.readline()
    
myfile = open(input_file)

print "lets firstly print the file:\n"

filedisplay(myfile)

print "now we have to reset the line count..... done\n"

linerestart(myfile)

print "now we'll print the lines one at a time.\n"

currentline = 1

lineprint(currentline, myfile) 

currentline = 1

lineprint(currentline + 1, myfile)

currentline = 1

lineprint(currentline + 2, myfile)
