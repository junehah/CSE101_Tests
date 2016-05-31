def main():
    print "--you are in main"
    x = input("select the following" + '\n' + "---> ")
    if x == 1:
        conversion()
    elif x==2:
        even()
    elif x==3:
        prime()
    elif x==4:
        summ()
    else:
        print "select only 1 (conversion), 2(even), 3(prime)"
        main()

def conversion():
    x = input("enter the following number to convert to Celcius" + '\n' + "--->")
    c = (x-32)*5/9
    print c
    main()

def even():
    x = input("enter a number to check if its even" + '\n' + "--->")
    if (x%2==0):
        print "even"
    else:
        print "odd"
    main()

def prime():
    x = input("enter a number to check for prime" + '\n' + "--->")
    increment = 0
    for count in range(1,x+1):
        if x%count==0:
            increment = increment + 1
    if increment==2:
        print "prime"
    else:
        print "not prime"
    main()

def summ():
    for i in range (1, x+1):
        x=x+i
    print x

main()
