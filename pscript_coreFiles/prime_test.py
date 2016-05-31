def prime(x):
    #print x,
    increment = 0
    for count in range(1,x+1):
        if x%count==0:
            increment = increment + 1
    if increment==2:
        #print "Its Prime
        return 1
    else:
        #print "Its NOT prime"
        return 0

#prime(x)
