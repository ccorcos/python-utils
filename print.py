import pprint

def pr(level, *args, **kwargs):
    string = " ".join([pprint.pformat(arg) for arg in args])
    string = string.replace("'", "").replace('"', '')
    if level == 0:
        sym = "="
        w = 78
        string = " " + string + " "
        n = len(string)
        d = w - n
        l = ''
        r = ''
        if d > 0:
            if d % 2 == 0:
                l = sym * int(d / 2.)
                r = l
            else:
                l = sym * int(d / 2.)
                r = sym * int(d / 2. + 1)
            print ''
            print sym * w
            print l + string + r
            print sym * w
            print ''
        else:
            print ''
            print sym * w
            print string
            print sym * w
            print ''
    elif level == 1:
        print " - " + string
    elif level == 2:
        print "   * " + string
    elif level == 3:
        print "     = " + string
    elif level == 4:
        print "       > " + string
    elif level == 4:
        print "         + " + string
    elif level == 100:
        lines = string.split("\n")
        for line in lines:
            print "      " + line
    else:
        print "? " + string
