# Function to display all ways of choosing 2 from a set of data, using binary counting

import time


def choose2(n):
    max = 2 ** (n-1) + 1

    binarylist = []

    extent = n-1
    count = 2

    while count <= max:
        shifted = count + 1
        for a in range(extent):
            binarylist.append(shifted)
            shifted *= 2
        count *= 2
        extent -= 1

    print(binarylist)
    displaycombinations(binarylist,n)


def displaycombinations(list,length):

    for n in list:
        print(str(bin(n)[2:]).rjust(length,"0"))


if __name__ == "__main__":
    stopwatch = time.time()

    choose2(11)

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
