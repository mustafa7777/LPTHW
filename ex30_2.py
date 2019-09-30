print "you walk into a dark room and there are two doors, choose a door, 1 or 2."

door = raw_input("> ")


if door == "1":

    print "there is an opening to a tunnel with some light at the end of it"
    print "what do you do now, go through the tunnel or go back to the dark room"
    print "enter '1' to leave through the tunnel, otherwise enter '2' to return to the dark room"
    tunnel = raw_input("> ")
    
    if tunnel == "1":
        print "you have made it out safely, hopefully you can handle all the light outside"
        
    elif tunnel == "2":
        print "you are now stuck in the dark room with no way out, try screaming for help"
        
    else:
        print "choosing %s is probably the safest choice, good job!" % tunnel

if door == "2":
    print "there's an escape hatch"
    print "what would you like to do?"
    print "to use the hatch enter 1 otherwise enter 2 to return to the dark room"
    hatch = raw_input("> ")

    if hatch == "1":
        print "you are safely out of there, good job."

    elif hatch == "2":
        print "you are now permanantly stuck in here, try screaming for help!"

    else:
        print "wise decision %s is, good job, you are safe now!" % hatch


