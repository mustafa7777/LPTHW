def add(a, b):
    print "ADDING %d to %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d from %d" % (b, a)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d with %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d by %d" % (a, b)
    return a / b

print "lets do some math:\n"

first_calculation = add(3, 5)
second_calculation = subtract(6, 4)
third_calculation = multiply(10, 5)
fourth_calculation = divide(100, 25)

print "Our calculations are as follows:\n%d\n%d\n%d\n%d\n" % (first_calculation, second_calculation, third_calculation, fourth_calculation)

print "Now we're going to play around with numbers calculated above:\n"

final_calculation = add(first_calculation, subtract(second_calculation, multiply(third_calculation, divide(fourth_calculation, 1))))

print "The final result is ", final_calculation
