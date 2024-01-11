
def find_consecutive_sums(n):
    base = n
    i = 1
    j = n
    s = "= " + str(n)
    while j < n*n:
        s = s + " + " + str(n+i)
        j = j+n+i
        i = i+1
    return j,s


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for check in range (1,20000):
        cs = find_consecutive_sums(check)
        if cs[0] == check*check:
            print (cs[0], "("+str(check)+"^2)")
            print (cs[1])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
