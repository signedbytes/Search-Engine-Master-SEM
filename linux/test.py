#!/usr/bin/python
import time

def stopwatch(seconds):
    start = time.time()
    # time.time() returns the number of seconds since the unix epoch.
    # To find the time since the start of the function, we get the start
    # value, then subtract the start from all following values.
    time.clock()    
    # When you first call time.clock(), it just starts measuring
    # process time. There is no point assigning it to a variable, or
    # subtracting the first value of time.clock() from anything.
    # Read the documentation for more details.
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed) 
        time.sleep(1)  
stopwatch(4)
