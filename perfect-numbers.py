# 29.4.2023
# Search for perfect numbers

def does_it_divide(m,n):
    factor = True
    if n%m != 0:
        factor = False
    return factor

def perfect(n):
    h = int(n/2)
    factors = []
    for k in range(h,0,-1):
        if does_it_divide(k,n):
            factors.append(k)

    if sum(factors) == n:
        return True
    else:
        return False


if __name__ == "__main__":
    for n in range(123456):
        if perfect(n):
            print(n)