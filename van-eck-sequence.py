# 10.3.2023
#
# Van Eck's sequence
#
# NOT WORKING YET

class number_memory:
    def __init__(self, n, ago):
        self.n = n
        self.ago = ago

memorys = []
numbers = []

def van_eck(terms):
    ve = 0

    k = 0
    n = 0
    new = 0

    while n < terms:
        print(ve)
        for j in range(len(memorys)):
            memorys[j].ago = memorys[j].ago + 1

        if numbers.count(ve) == 0:
            new = 0
            memorys.append(number_memory(ve,0))
            numbers.append(ve)
        else:
            for j in range(len(memorys)):
                if memorys[j].n == ve:
                    k = j
            new = memorys[k].ago

        n += 1
        #for k in range(len(memorys)):
            #print(str(memorys[k].n) + ": appeared " + str(memorys[k].ago) + " digits ago")
        ve = memorys[k].ago




if __name__ == "__main__":
    van_eck(10)