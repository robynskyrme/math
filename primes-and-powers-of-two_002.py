
# Visualize whether primes result in further primes when various powers of two are added to them
# Options in main for how many primes to check, and how many powers of 2 to check

import math

def is_n_prime(n):
    top = n
    bottom = 1
    f = 1
    integercount = 0
    while f >= 1:
#        print(integercount)
        if f%1 == 0:
            integercount = integercount + bottom
        f = top/bottom
        top = top-bottom
        bottom = bottom + 1

    if integercount == 6:
    #    print (n, "is prime")
        return True
# ... with an if statement:
    if  n == 2:
        return True
    else:
    #    print (n, "is not prime")
        return False


def listpowers(p,t):
    output = ""
    pcount = 0
    n = 1
    while pcount <= p-1:
        # Check if it's prime, add to prime counter, and look for powers of 2
        if is_n_prime(n):
            output = ""
            pcount += 1

            for power in range(t,0,-1):
                if is_n_prime(n+pow(2,power)):
#                    print(str(n) + " is prime...")
#                    print(str(n) + " plus " + str(pow(2,power)) + " is prime, too: " + str(n+pow(2,power)))
#                    output = output + str(power) + ", "
                    output = str(output) + "∙"   # str(power).rjust(3," ")
                else:
                    output = output + " "
            output = output + "   " + str(n).rjust(3," ")
            print(output)

        if not is_n_prime(n):
            if n%2 != 0:
                output = ""
                pcount += 1
                for power in range(t, 0, -1):
                    if is_n_prime(n+pow(2,power)):
                        #                   print(str(n) + " is prime...")
                        #                    print(str(n) + " plus " + str(pow(2,power)) + " is prime, too: " + str(n+pow(2,power)))
                        #                    output = output + str(power) + ", "
                        output = str(output) + "∙"  # str(power).rjust(3," ")
                    else:
                        output = output + " "
                output = output + "   " + str(n).rjust(3," ")
                print(output)


        n += 1

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    primes = 163
    powers = 37

    listpowers(primes,powers)

# Prime p shown far left: a number n appears in the grid if p + 2^n is also prime
# So the '1's column indicates when a prime is the smaller of a pair of twin primes;
# the '16's column indicates the smaller of two primes which differ by 65536, etc.
#