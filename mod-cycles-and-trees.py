# Step toward visualizing the cycles and trees created by mapping n to f(n)

def get_result(n,modulo):
    n = 2*n + 1

    n = n % modulo

    return n



def get_gamut(q):
    results = []
    for i in range(q):
        results.append(get_result(i,q))

    return results


def analyse(f):
    cycles = []
    chains = []
    used = set()
    checked = set()

    for n in range(len(f)):
        if n not in checked:

            used.add(n)
            current = [n]

            cycle = False
            chaindone = False

            while cycle == False and chaindone == False:
                n = f[n]

                if n in used:
                    chaindone = True
                if n in current:
                    cycle = True

                current.append(n)
                used.add(n)
                checked.add(n)

            if cycle:
                cycles.append(current)
            else:
                chains.append(current)
        checked.add(n)

    return cycles, chains



if __name__ == "__main__":
    q = 24

    gamut = get_gamut(q)

    scene = analyse(gamut)
    print("Cycles: ",scene[0],"\nChains: ",scene[1])