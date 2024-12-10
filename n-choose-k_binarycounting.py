# 10.12.2024
# using binary counting to enumerate and display the options for n choose k

def nchoosek(n,k):
    z = n-k
    o = k

    limit = (2 ** (o+z+1)) - (2 ** z+1)

    sequence = []

    limit += 1

    for count in range(limit):
        if binarypossible(count,o,z):
            sequence.append(count)

    return sequence


def binarypossible(n,o,z):
    binstr = bin(n)[2:]
    # print(binstr)
    binstr = binstr.rjust(o+z,"0")

    if len(binstr) > o+z:
        return False

    if binstr.count("0") != z:
        return False

    if binstr.count("1") != o:
        return False

    print(binstr + " = " + str(n))

#    print(str(n))

    return True







if __name__ == "__main__":
    for j in range(3,12):
        print("")
        print(str(j) + " choose 3:")
        seq = (nchoosek(j,3))
        print (len(seq))