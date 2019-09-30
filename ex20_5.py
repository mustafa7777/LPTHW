from sys import argv
script, input_file = argv

def file_print(f):
    print f.read()
    
def count_reset(f):
    f.seek(0)
    
def line_print(licount, f):
    print licount, f.readline()
    
my_file = open(input_file)

print "printout of file:\n"
file_print(my_file)

print "reseting line_count..... done\n"
count_reset(my_file)

print "printing lines one at time"

line_print(1, my_file)
line_print(1+1, my_file)
line_print(1+2, my_file)
