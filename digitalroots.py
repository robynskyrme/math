


def digitalroot(n):

    sum = 0

    while n:
        sum += n % 10
        n = n//10

    if sum >= 10:
        sum = digitalroot(sum)

    return sum





if __name__ == "__main__":
    for i in range(2,100):
        slab = ""
        for k in range(digitalroot((i-1) * (i+1))):
            slab += ">"
        print(slab, i)