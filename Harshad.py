def digit_sum(n):
    sum = 0

    while n:
        rightmost = n % 10
        n = n // 10
        sum += rightmost

    return sum

def is_harshad(n):
    sum = digit_sum(n)
    if n % sum == 0:
        return True
    else:
        return False


if __name__  == "__main__":
    for i in range (1,2027):
        if is_harshad(i):
            print(i)