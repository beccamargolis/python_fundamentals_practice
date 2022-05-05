#1. Multiples of Three – but Not All
#Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

for x in range (-300, 1, 3):
    if x == -3:
        continue
    elif x == -6:
        continue
    else:
        print(x)

#2. Printing Integers with While
#Print integers from 2000 to 5280, using a WHILE.

i = 2000
while i <= 5280:
    print(i)
    i += 1

#3. Counting, the Dojo Way
#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

for x in range (1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#4. Flexible Countdown
#Given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR.
#For (2,9,3), print 9 6 3 (on successive lines).

def find_multiples(low_num, high_num, mult):
    for x in range ((high_num + 1), low_num, -1):
        if x % mult == 0:
            print(x)

find_multiples(2,9,3)