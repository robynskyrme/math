def does_it_divide(m,n):
    factor = True
    if n%m != 0:
        factor = False
    return factor

                            # Method returns True if n is prime
def is_it_prime(n):
    prime = True
    half = int(n/2)
                            # (test counts down from half of in, one integer at a time, asks if it divides:
    for c in range(half,1,-1):
                            # (if it ever does, n is not prime)
        if does_it_divide(c,n) == True:
            prime = False
                            # There is a special case for excluding 1, which would otherwise return as prime
    if n == 1:
        prime = False
    return prime

                            # Method to count the prime factors of n
                            # Create a list
def prime_factors(n):
    factors = []
    half = int(n/2)

                            # Every time a factor is found....
    for c in range(half,1,-1):
        if n%c == 0:
                            # Check if it's a prime factor,
            if is_it_prime(c):
                            # And add it to the list
                factors.append(c)

                            # Without checking everything from n/2 to n, add n itself if it is already prime
    if is_it_prime(n):
        factors.append(n)


    fullfactors = []
    for factor in factors:
        c = n
        while c == int(c):
            c = c/factor
            fullfactors.append(factor)
        del fullfactors[-1]


    #print(factors)
                            # Return the _number_ of factors: this method just counts them
                            # Could be tweaked to return factors themselves
    return fullfactors


def collatz(n):
    if n%2 == 0:
        n = n//2
    else:
        n = 3 * n + 1
    return n



if __name__ == "__main__":

    n = 871
    tripwire = False

    while not tripwire:
        if n ==1 and collatz(n) == 4:
            tripwire = True

        slab = str(n)
        slab = slab.rjust(6)
        if n%3 == 0:
            slab = slab + "  0--  "
        if n%3 == 1:
            slab = slab + "  -1-  "
        if n%3 == 2:
            slab = slab + "  --2  "

        slab = slab + str(prime_factors(n))
        print(slab)
        n = collatz(n)
