
# 16.2.2023
#
# "Light Switch Problem" problem from today's video on Numberphile
# https://www.youtube.com/watch?v=-UBDRX6bk-A

    # Method count the factors of a number
    # With a trip to stop counting at "up_to"
def count_factors(n,up_to):
    factors = 0
    i = 1
    while i < up_to+1:
        if n%i == 0:
            factors = factors + 1
        i = i + 1

    return factors


def is_even(n):
    even = True
    if n%2 == 1:
        even = False
    return even

    # t = total numbers to check
    # r = length of row to output, visually
    # p = How many people turn switches off
def generate_grid(t,r,p):
    grid = ""
    # Do each number individually
    for i in range(1,t+1):
        # Every switch begins off
        switch_on = False

        # Instead of switching it on and off multiple times, use two methods two tell whether it is odd or even

        factors = count_factors(i,p)

        if not is_even(factors):
            switch_on = True

        # Add it to the grid string if it's on
        if switch_on:
            grid = grid + str(i).rjust(3," ")

        # Otherwise add whitespace
        if not switch_on:
            grid = grid + "   "

        # Space them out
        grid = grid + " "

        # Add a linebreak at the end of each row
        if i%r == 0:
            grid = grid + "\n"

    return grid

if __name__ == '__main__':
    # Set some variables

    # How many light switches in total
    t = 1000

    # How many in each row, when displayed
    r = 30

    # This is set to 100 for the 'full' problem
    people = 1000

    grid = generate_grid(t,r,people)

    print(grid)