# 24.8.2023 -- going to introduce a sieve


import math

def prime(n):
                                # Special cases:
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True

    max = (int(math.ceil(math.sqrt(n))))

    sieve = [0]

    for s in range(max):
        sieve.append(1)

    d = 2
                                # Count up to sqrt(n)
    while d <= max:
                                # Only check a new divisor if it has not already been eliminated
        if sieve[d] == 1:
            if n % d == 0:
                return False
                                # If a number d does not divide n, then eliminate all multiples of d from the search
        for j in range(d,len(sieve),d):
            sieve[j] = 0
        d += 1

    return True





if __name__ == "__main__":
    for n in range (5000,10000):

        star = ""

        if prime(n):
            print(str(n))
