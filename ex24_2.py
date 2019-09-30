ten = 20 - 5 + 15 - 20
print "This should be ten: %s" % ten

def random_numbers(startup):
    firstrandom = startup * 1000
    secondrandom = firstrandom / 500
    thirdrandom = secondrandom + 500
    return firstrandom, secondrandom, thirdrandom 
    
    
startpoint = 150
first, second, third = random_numbers(startpoint)

print "the start point is %d" % startpoint
print "we have %d first, %d second, %d third" % (first, second, third)
