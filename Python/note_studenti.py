#!/usr/bin/env python

import sys

def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    try:
        fp = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid file name"
        usage()
        sys.exit(1)

    students = list(fp)
    print students
    nota_max = 0
    for s in students:
        items=s.split('\t')
        print items
        if int(items[3]) > nota_max:
            nota_max = int(items[3])
            nume = items[0]
      

    print "Nota maxima: %d si numele : %s" % (nota_max, nume)

if __name__ == "__main__":
    sys.exit(main())
