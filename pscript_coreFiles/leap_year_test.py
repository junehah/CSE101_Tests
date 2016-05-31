def leap_year(x):
    if (x%4==0 and x%100!=0):
            #print "Its a leap year"
            return 'true'
    else:
        #print "It is NOT a leap year"
        return 'false'

#leap_year(2000)
