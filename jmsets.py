"""
jmsets.py
================================================================================
Juan Diego Samaniego Rojas
August 2016 (Python 2.7.12)
--------------------------------------------------------------------------------
Some functions to explore the Julia and Mandelbrot sets. 
Module 'matplotlib' is required to do the graphics.
--------------------------------------------------------------------------------
For the quadratic general function f(z) = z^2 + c, where z,c are complex, the
Julia set is given by all the values of z such that |fn(z)| is bounded for all
n. Here, fn is the nth iteration of f, i.e., f3(z)=f(f(f(z))), and the marks ||
indicate the modulus of the function. The Julia set, J(f), is a function of the
parameter c.
The Mandelbrot set is a subset of the Julia parameters, such that iteration over
z=0 is bounded.

The more iterations, the better the graphics and the larger the computing time.
--------------------------------------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np
import math, random, time

# Parameters, constants and auxiliary functions --------------------------------
MAXITER = 64
PHI = (1+math.sqrt(5))/2
PI = math.pi
cos = math.cos
sin = math.sin
sqrt = math.sqrt

# Main functions ---------------------------------------------------------------
def jiterator(z0, c, n_iter=MAXITER, p=0):
    """
This is the Julia iterator. It returns the max number of iterations of the
function f(z0), described above, before it goes unbounded. The bound is here the
parameter R, which comes from the analysis of the general function f(z).
The argument p is the probability of z0 to be accepted without checking the
convergence of the function f.A value of p=0.001 gives the graphic a nice,
random touch of class.
    """
    R = (1 + sqrt(1 + 4*abs(c)) )/2.0
    z = z0**2 + c
    for j in range(n_iter):
        if random.random() < p: return int(n_iter*random.random())
        if abs(z) > R: return j
        z = z**2 + c
    return n_iter

def miterator(c, n_iter=MAXITER, p=0):
    """
This is the Mandelbrot iterator. As the Julia iterator, it returns the number
of iterations of f(z), with z0=0.
The argument p is the probability of z0 to be accepted without checking the
convergence of the function f. A value of p=0.001 gives the graphic a nice,
random touch of class.
"""
    z = c
    for j in range(n_iter):
        if random.random() < p: return int(n_iter*random.random())
        if abs(z) > 2: return j
        z = z**2 + c
    return n_iter

def main_cardioid(alfa):
    """
    alfa <angle in radians>
Returns the complex constant c, which is part of the main cardioid in the Mandelbrot
set at angle alfa. Try rational and irrational alfa.
"""
    t1 = 2*PI*alfa
    t2 = 4*PI*alfa
    z1 = 0.50*complex(cos(t1),sin(t1))
    z2 = 0.25*complex(cos(t2),sin(t2))
    c = z1 - z2
    return c

# Functions that return something to plot --------------------------------------

def jset(jparam, samples=512, n_iter=MAXITER, region=None, p=0):
    """
    jparam <complex constant>, samples [numbers to be checked],
    n_iter [number of iterations], region [region to plot]
Returns a matrix Z, where Zji is the number of iterations given by jiterator on
the complex(X[i], Y[j]). It also returns the limits of X and Y.
The optional variable 'region' is a list of the form [xmin,xmax, ymin,ymax],
which determines the region where the calculations are made.
This samples are made in the real and imaginary axis, and afterwards combined in
all possible ways (samples^2).
"""
    R = (1+sqrt(1+4*abs(jparam)))/2.0
    if region != None:
        xmin, xmax, ymin, ymax = region
        X = np.linspace(xmin, xmax, samples)
        Y = np.linspace(ymin, ymax, samples)
        limits = region
    else:
        X = np.linspace(-R, R, samples)
        Y = np.linspace(-R, R, samples)
        limits = [-R, R, -R, R]

    Z = np.empty((samples, samples))
    
    print('Julia set for c=%s' % jparam)
    print('R=%.4f' % R)
    print('Max number of iterations: %d' % n_iter)
    print('Running over %d complex numbers...' % (samples**2))
    for i,x in enumerate(X):
        for j,y in enumerate(Y):
            Z[j,i] = jiterator(complex(x,y), jparam, n_iter, p)
    
    return Z, limits

def mset(samples=512, n_iter=MAXITER, region=None, p=0):
    """
    samples [numbers to be checked], n_iter [number of iterations],
    region [region to plot]
Returns a matrix Z, where Zji is the number of iterations given by miterator on
the complex(X[i], Y[j]). It also returns the limits of X and Y.
The optional variable 'region' is a list of the form [xmin,xmax, ymin,ymax],
which determines the region where the calculations are made.
This samples are made in the real and imaginary axis, and afterwards combined in
all possible ways (samples^2).
"""
    if region != None:
        xmin, xmax, ymin, ymax = region
        X = np.linspace(xmin, xmax, samples)
        Y = np.linspace(ymin, ymax, samples)
        limits = region
    else:
        X = np.linspace(-2.0, .75, samples)
        Y = np.linspace(-1.5, 1.5, samples)
        limits = [-2.0, 0.75, -1.5, 1.5]
    
    Z = np.empty((samples, samples))
    
    print('Mandelbrot set')
    print('Max number of iterations: %d' % n_iter)
    print('Running over %d complex numbers...' % (samples**2))

    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            Z[j, i] = miterator(complex(x,y), n_iter, p)
    
    return Z, limits

# The real plotting functions --------------------------------------------------

def jplot(jparam, samples=512, n_iter=MAXITER, region=None, p=0, colormap='Blues',
          savefig=False):
    # Measuring time
    t1 = time.time()
    Z, limits = jset(jparam, samples, n_iter, region, p)
    t2 = time.time()
    delta_t = t2-t1
    print('Elapsed time: %d seconds' % delta_t)
    print('Max iteration: %d' % Z.max())

    # Graphic setup
    if savefig == True:
        sq = samples**2
        suffix = random.randint(0,1e4)
        name = 'julia_%d.png' % suffix

    # Actually plotting   
    plt.figure()
    size = [samples/100.]*2
    plt.gcf().set_size_inches(size)
    plt.setp(plt.gca(), xticks=[], yticks=[])
    plt.imshow(Z, origin='lower', cmap=colormap, extent=limits)
    plt.xlabel(r'$\Re{z}$'); plt.ylabel(r'$\Im{z}$')
    if savefig == True:
        plt.savefig(name, transparent=True)
        plt.close()
    else: plt.show()

def mplot(samples=512, n_iter=MAXITER, region=None, p=0, colormap='Blues',
          savefig=False):
    # Measuring time
    t1 = time.time()
    Z, limits = mset(samples, n_iter, region, p)
    t2 = time.time()
    delta_t = t2-t1
    print('Elapsed time: %d seconds' % delta_t)
    print('Max iteration: %d' % Z.max())

    # Graphic setup
    if savefig == True:
        sq = samples**2
        suffix = random.randint(0,1e4)
        name = 'mandelbrot_%d.png' % suffix

    # Actually plotting   
    plt.figure()
    size = [samples/100.]*2
    plt.gcf().set_size_inches(size)
    plt.setp(plt.gca(), xticks=[], yticks=[])
    plt.imshow(Z, origin='lower', cmap=colormap, extent=limits)
    plt.xlabel(r'$\Re{z}$'); plt.ylabel(r'$\Im{z}$')
    if savefig == True:
        plt.savefig(name, transparent=True)
        plt.close()
    else: plt.show()

# End --------------------------------------------------------------------------
