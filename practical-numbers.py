# 24.5.2023
# Practical Numbers

# All integers up to n can be made by addition using the factors of n


                            # Method returns True if m divides n with modulo zero
def does_it_divide(m,n):
    factor = True
    if n%m != 0:
        factor = False
    return factor


                            # Method to count the  factors of n
                            # Create a list
def factors(n):
    factors = []
    half = int(n/2)+1

                            # Every time a factor is found....
    for c in range(half,1,-1):
        if n%c == 0:
            factors.append(c)

                            # Without checking everything from n/2 to n, add n itself if it is already prime

    factors.append(1)

    return factors


                            # Method to try all combinations by counting in binary
def combinations(arr):
    count = len(arr)

    result = []

    for j in range (1,2**count):
        comb = []
        bindig = bin(j)[2:]
        bindig = bindig.rjust(len(arr),"0")

        for k in range(len(bindig)):
            if bindig[k] == "1":
                comb.append(arr[k])

        result.append(comb)

    return result


def practical(n):
    result = False

    integers_up_to_n = []

    integers_up_to_n.append(1)

    for j in range(n):
        integers_up_to_n.append(0)

    combs = combinations(factors(n))
    print(combs)

    for k in range(len(combs)):
        s = sum(combs[k])
        if s <= n:
            integers_up_to_n[s] += 1

    print(integers_up_to_n)

    if integers_up_to_n.count(0) == 0:
        result = True

    return result

if __name__ == "__main__":

    for k in range (10):
        if practical(k):
            print(k)
