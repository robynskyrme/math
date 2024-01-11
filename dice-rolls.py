# 4.3.2023
# Simple methods to roll a dice of d sides n times, and repeat that a certain number of times
#
# Plus an extra example method to test whether the numbers rolled are in descending order

import random


                            # This method
def rolldice(n,d):
                            # creates a list
    rolls = []
                            # creates a loop to roll n times
    for roll in range(n):
                                    # rolls the dice
        result = random.randint(1,d)
                                    # and adds the result to the list
        rolls.append(result)
    return rolls

                            # This method takes the list of rolls as input
def in_desc_order(rolls):
                            # Sets a variable to assume that the list of rolls is in descending order
    desc = True
                            # Chceks that this is true one by one
    for c in range(len(rolls)-1):
        if rolls[c] <= rolls[c+1]:
                            # flips the variable if at any point the decending-order rule is broken
            desc = False
                            # And returns the variable as a boolean
    return desc

if __name__ == "__main__":
                            # n = how many rolls
                            # d = D sides of die
    n = 3
    d = 6
                            # How many times to repeat a set of rolls
    r = 999999

                            # This section repeats the set of rolls r times
                            # One variable to keep a running average; another to keep a running count
    average = 0
    tally = 0

    for c in range(1,r+1):
        rolls = rolldice(n,d)

        if in_desc_order(rolls):
            tally = tally + 1
            slab = "  HIT  "
        else:
            slab = "       "

        average = tally/c

        print(str(rolls) + "     " + slab +  str(tally) + "/" + str(c) + "    " + str(average))