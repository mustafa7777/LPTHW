#this program will def arguments and print them out using variables
def resistors_and_capacitors(resistor_count, capacitor_count):
    print "You have %d resistors" % resistor_count
    print "You have %d capacitors" % capacitor_count
    print "You have enough to complete the test board!"
    print "Warm up your soldering iron.\n"
    
    
print "We can give the variables numbers directly"
resistors_and_capacitors(40, 50)

print "We can define the variables"
resistor_total = 10
capacitor_total = 22
resistors_and_capacitors(resistor_total, capacitor_total)

print "We can add ourselves"
resistors_and_capacitors(10 + 10, 14 + 11)

print "Or we can add them to a previous line"

resistors_and_capacitors(2000 + resistor_total, 1000 + capacitor_total)
