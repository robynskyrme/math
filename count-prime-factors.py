# 3.3.2023
#
# Count the prime factors of a number

                            # Method returns True if m divides n with modulo zero
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

    #print(factors)
                            # Return the _number_ of factors: this method just counts them
                            # Could be tweaked to return factors themselves
    return len(factors)




                            # Method to output a bar of length n, for the drawing of pretty patterns
def draw_bar(n):
    slab = ""
    for block in range(n):
        slab = slab + " "
    slab = slab + "|"
    print(slab)


                            # [An experiment in visualizing patterns, to return to later]
# def add_block(slab,parity,width):
#     if parity == True:
#         slab = slab + "█"
#         if len(slab)%width == 0:
#             slab = slab + "\n"
#     else:
#         slab = slab + " "
#         if len(slab)%width == 0:
#             slab = slab + "\n"
#
#     return slab




    # Take input
if __name__ == '__main__':
    n = 10000
    even = 0
    odd = 0
    tally = 100

    for c in range(1,n):
        #width = 100
        #block = ""

        if prime_factors(c)%2 == 0:
            tally = tally + 1
            # print(c)
            # print("Has an even # of prime factors")
        else:
            tally = tally - 1
            # print(c)
            # print("Has an odd # of prime factors")
        draw_bar(tally)

    print("\nLine above counts from 1 to 10,000; moves left if n has even number of prime factors, moves right if an odd number")
    x = 73
    print("\nIs " + str(x) + " prime? " + str(is_it_prime(x)))


        #print(block)
        #draw_bar(tally)
