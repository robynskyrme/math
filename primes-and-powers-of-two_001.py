
# Visualize whether primes result in further primes when various powers of two are added to them
# Options in main for how many primes to check, and how many powers of 2 to check



import math

from math import isqrt

def is_n_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


# def is_n_prime(n):
#     top = n
#     bottom = 1
#     f = 1
#     integercount = 0
#     while f >= 1:
# #        print(integercount)
#         if f%1 == 0:
#             integercount = integercount + bottom
#         f = top/bottom
#         top = top-bottom
#         bottom = bottom + 1
#
#     if integercount == 6:
#     #    print (n, "is prime")
#         return True
# # ... with an if statement:
#     if  n == 2:
#         return True
#     else:
#     #    print (n, "is not prime")
#         return False


def listpowers(p,t):
    output = ""
    pcount = 0
    n = 1
    while pcount <= p-1:
        # Check if it's prime, add to prime counter, and look for powers of 2
        if is_n_prime(n):
            output = ""
            pcount += 1

            for power in range(t,-1,-1):
                if is_n_prime(n+pow(2,power)):
#                    print(str(n) + " is prime...")
#                    print(str(n) + " plus " + str(pow(2,power)) + " is prime, too: " + str(n+pow(2,power)))
#                    output = output + str(power) + ", "
                    output = str(output) + "  o" # str(power).rjust(3," ")
                else:
                    output = output + "   "
            output = output + "   " + str(n).rjust(3," ")
            print(output)
        n += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    primes = 163
    powers = 41

    listpowers(primes,powers)

# Prime p shown far left: a number n appears in the grid if p + 2^n is also prime
# So the '1's column indicates when a prime is the smaller of a pair of twin primes;
# the '16's column indicates the smaller of two primes which differ by 65536, etc.
#
# Output for primes = 37, powers = 37:
#                                                                                                                  0     2
#                       30    28                            18    16 15       12              7  6     4  3  2  1        3
#                                                                                11                 5     3     1        5
#                       30    28                      20    18    16                10     8     6     4     2           7
#                    31    29                23                      15                 9     7     5     3     1       11
#                                                     20                                   8           4     2          13
#              33                                  21                      13                                   1       17
#                       30                                                                       6           2          19
#                                                                                             7           3             23
#  37          33                27          23                17    15    13           9     7     5     3     1       29
#     36                                                                      12                       4                31
#                             28                      20                14    12    10     8     6     4     2          37
#  37                                  25                      17          13    11                 5           1       41
#                                         24                18    16    14    12                 6     4     2          43
#                                                                                                   5                   47
#        35                      27                      19                                   7           3             53
#              33                                  21    19                             9                 3     1       59
#                 32                                                          12           8                            61
#                       30    28                22                      14          10           6     4     2          67
#              33                27    25          21          17    15    13                 7     5     3     1       71
#                                         24                18    16                10           6     4                73
#           34                                                                      10                       2          79
#        35                                  23                                  11           7                         83
#                          29                23                                  11     9                 3             89
#                                   26                            16    14                 8           4     2          97
#              33                                        19          15    13           9     7           3     1      101
#                                                                       14                 8     6           2         103
#                          29                      21                                   9           5           1      107
#                                                           18          14                       6           2         109
#                                                                                11           7                        113
#                                                     20    18                      10     8     6           2         127
#                                            23                17                11     9           5     3            131
#                                                  21                      13                                   1      137
#                                                                                   10                                 139
#              33          29    27    25                      17    15                 9     7     5     3     1      149
#                                                                 16                                   4               151
#                                                                             12    10                 4               157