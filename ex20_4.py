from sys import argv

script, input_file = argv

def display_content(f):
    print f.read()
    
def res(f):
    f.seek(0)
    
def line_display(licount, f):
    print licount, f.readline()

my_file = open(input_file)
    
print "firtsly lets print the contents of the file:\n"

display_content(my_file)

print "now lets reset the line count...... done:\n"

res(my_file)

print "lastly we'll display the lines one by one:\n"

linenumber = 1
line_display(linenumber, my_file)

linenumber = 1
line_display(linenumber + 1, my_file)

linenumber = 1
line_display(linenumber + 1, my_file)
