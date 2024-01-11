
   # 8.2.2023


   # Method checks whether repeated division by a number 1) results in integer values,
   # and 2) eventually arriving at 1,  counting the steps as it goes


   # Problem: works only with integers, need to either code in (or refuse to deal with) zero or negatives


def is_power_of_m(n,m):
   p = 0
   c = n
   while c/m == int(c/m):
       p = p+1
       c = c/m
   if c == 1:
       return True,p
   else:
       return False,0




    # Loops to demonstrate method

if __name__ == '__main__':


# m is the power to be checked -- loop to check powers 2 to 10
   for m in range (2,11):

       # Loop to check all nmubers from 1-999999 individually
       for n in range(1,999999):
           check = is_power_of_m(n,m)
           if check[0]:
               print(str(n) + " is " + str(m) + " to the power of " + str(check[1]))
           else:
               m = m    # This line is only here becuase it doesn't like an empty 'else', if the following line is commented out
           #    print(str(n) + " is not a power of " + str(m))
       print ("\n")