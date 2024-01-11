
# 26.2.2023
#
# The Mandelbrot Set
#
# I can't believe I actually made it work....... honestly, I've been wanting to code this since I was about twelve


import cmath

def add_point(s,filled):
    if filled == 0:
        s = s + " "
    if filled == 1:
        s = s + "•"
    return s

def checkpoint(c):
    z = complex(0,0)
    filled = 0
    itercount = 0

    for iter in range (600):
        if z.real**2 + z.imag**2 > 2:
            z = complex(2,0)

        # The Mandelbrot Set
        z = z**2 + c

        # Burning Ship fractal
        # z = (abs(z.real) + abs(z.imag)*complex(0,1))**2 + c


    if z.real**2 + z.imag**2 > 2:
        filled = 1

    return filled

def plot_mandelbrot():
    output = ""
    for y in range(48,-49,-2):
        y = y / 46
        for x in range(-100,50):
            x=x/50
            output = add_point(output,checkpoint(complex(x,y)))
        output = output + "\n"
    print(output)

if __name__ == '__main__':
    plot_mandelbrot()
