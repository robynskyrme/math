# 31.5.2023
# Encoding a square pixel grid in a single number
# (insomnia got me thinking about this last night)

# This is a cumbersome method involving massive numbers: primes and powers of 2, all multiplied together --
# practically useless, but a fun exercise (contains cell data, grid size, and negative-image option in a single integer)

# To generate a number:
# -- Choose grid size (grids are square) -- call this p
# -- In cells of the grid, left-right, write the primes starting at 3
# -- For cells to be "switched on", multiply by the prime in that cell
#
# -- e.g.    3   5   7        To draw a bottom-left top-right horizontal stripe on this grid,
#           11  13  17        multiply 7 * 13 * 19
#           19  23  29
#
# Then, multiply by 2^p (in this case 3, 2^3 = 8)
#
# So this grid's number is 13832
#
# Finally: to display its image in negative, add 1 to the final number e.g.
#      13832:       13833:
#         █          ██
#        █           █ █
#       █             ██

import math

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, 547]

                            # Simple factor test using modulo
def divides(x,y):
    result = False
    if x%y == 0:
        result = True
    return result

                            # Function to repeatedly halve a number n:
                            # returns the result n, and the number of times it was halved p
def halve(n):
    p = 0

    while n%2 == 0:
        n = n/2
        p +=1

    return int(n),p


                            # Function to draw the code-number as a grid
def grid(n):
                            # Array stores the on/off pixels to display
    blocks  = ["█", " "]

                            # The number will always be even (it's some multiple of a power of two)
                            # unless 1 has been added manually to indicate "negative": this swaps the pixels, if so
    if n%2 != 0:
        blocks[0], blocks[1] = blocks[1], blocks[0]
        n -= 1

                            # Variable to store size of grid
    p = 0
                            # Repeatedly divides by two until an odd number is found:
                            # the number of divisions is the grid size
    n, p = halve(n)

                            # Variable to store grid
    gridstring = ""

                            # Iterate over every cell (p squared)
    for c in range(p**2):
                            # ... matching each cell with an item in the list of primes given above
        if divides(n,primes[c]):
                            # if the prime divides n, colour the cell one colour
            gridstring += blocks[0]
                            # and if it doesn't, colour it the other colour
        else:
            gridstring += blocks[1]
                            # add a newline character every p characters
        if c%p == p-1:
            gridstring += "\n"

    return gridstring



if __name__ == "__main__":
    print(grid(119656343))