
import cmath
import math

def analyze_point(x,y,maxiter):

    colour = 0

    # The Mandelbrot Set

    z = complex(0,0)
    c = complex(x,y)

    iter = 0
    steps = 0

    while iter < maxiter:
        if z.real**2+z.imag**2 < 2:
                z = z**2 + c
                steps += 1
        iter += 1

    colour = maxiter-steps



    # Circle (test)

    # if x**2 + y**2 > 1:
    #     colour = 1
    # else:
    #     colour = 0

    return colour

def add_point(slab,colour,spect):

    cols = [" ","*","o","0","•"]

    div = spect/len(cols)
    colour = math.floor(colour/div)

    slab = slab + cols[colour]

    return slab

def plot_all(xn,xx,xs,yn,yx,ys,maxiter):

    plane = ""

    xn = xn * xs
    xx = xx * xs

    yn = yn * ys
    yx = yx * ys

    for y in range(yx,(yn-1),-1):
        y = y/ys
        for x in range(xn,(xx+1)):
            x = x/xs
            plane = add_point(plane,analyze_point(x,y,maxiter),maxiter)
        plane = plane + "\n"

    print(plane)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    xn = -2
    xx = 1
    xs = 90

    yn = -2
    yx = 2
    ys = 30

    maxiter = 180

    plot_all(xn,xx,xs,yn,yx,ys,maxiter)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/