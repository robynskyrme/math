

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


def collatz_seq_plus_prime(n):

    seq = 1
    while n != 7:
        if is_it_prime(n):
            n = 3 * n - 1
        else:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
        seq = seq + 1
        #print(n)

    return seq


def draw_bar(width):
    bar = ""
    for block in range(width):
        bar = bar + " "
    bar = bar + "•"
    return bar

if __name__ == "__main__":
    for j in range(1,1000):
        #print(j)
        print(draw_bar(collatz_seq_plus_prime(j)))