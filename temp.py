#!/usr/bin/python2.7

import sys

def printHelp():
    print """Python 2.7 Tempurature Converter
Proper usage:
    temp <option> <temp>
Options:
    -h: Displays this message.
    -f: Convert to Farenheit.
    -c: Convert to Celsius."""
    exit()

def main():
    if len(sys.argv) == 1 or len(sys.argv) > 3 or sys.argv[1] == '-h':
        printHelp()
    
    m = sys.argv[1].lower()
    if m == '-c' or m == '-f':
        try:
            t = float(sys.argv[2])
        except ValueError:
            print "Improper format!"
            printHelp()
    else:
        print "Improper format!"
        printHelp()

    if m == '-c':
        newTemp = (t - 32) / 1.8
        print "%sF = %dC" % (t, newTemp)
    elif m == '-f':
        newTemp = t * 1.8 + 32
        print "%sC = %dF" % (t, newTemp)
    else:
        exit("SANITY CHECK FAILURE!")


if __name__ == '__main__':
    main()
