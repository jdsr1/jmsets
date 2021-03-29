#!/usr/bin/python
#!encoding: utf-8

import numpy as np
from matplotlib import pyplot as plt

# Get available colormaps
colormaps = [cmap for cmap in plt.colormaps()]
colormaps.sort()


# Main cardiod complex value at angle alpha [rad]
def main_cardioid(alfa):
    t1 = 2 * np.pi * alfa
    t2 = 4 * np.pi * alfa
    z1 = 0.50 * complex(np.cos(t1), np.sin(t1))
    z2 = 0.25 * complex(np.cos(t2), np.sin(t2))
    c = z1 - z2
    return c


# Julia set number of iterations
def julia_iterations(z_0, c_param, maxiter=64):
    boundary = (1 + np.sqrt(1 + 4 * np.abs(c_param)) ) / 2.0
    
    z_n = z_0**2 + c_param
    for n in range(maxiter):
        if np.abs(z_n) > boundary:
            return n
        z_n = z_n**2 + c_param
    return maxiter


# Mandelbrot set number of iterations
def mandelbrot_iterations(zvalue, maxiter=64):
    zvalue0 = zvalue
    for n in range(maxiter):
        if abs(zvalue) > 2:
            return n
        else:
            zvalue = zvalue**2 + zvalue0
    return maxiter


# Return the matrix and (x,y) limits of the set
def julia_set(c_param, region=None, width=64, height=64, maxiter=64):
    if region is not None:
        point_x, point_y, delta_x, delta_y = region
        xmin = point_x - 0.5*delta_x
        xmax = point_x + 0.5*delta_x
        ymin = point_y - 0.5*delta_y
        ymax = point_y + 0.5*delta_y
    else:
        boundary = (1 + np.sqrt(1 + 4 * np.abs(c_param)) ) / 2.0
        xmin = -boundary
        xmax = boundary
        ymin = -boundary
        ymax = boundary

    x_samples = np.linspace(xmin, xmax, width)
    y_samples = np.linspace(ymin, ymax, height)
    z_samples = np.empty((height, width))

    limits = [xmin, xmax, ymin, ymax]
    
    for col, x in enumerate(x_samples):
        for row, y in enumerate(y_samples):
            z = complex(x, y)
            iterations = julia_iterations(z, c_param, maxiter)
            z_samples[row, col] = iterations
    
    return z_samples, limits


# Returns the elements of the Mandelbrot set and their (x,y) limits
def mandelbrot_set(region=None, width=64, height=64, maxiter=64):
    if region is not None:
        point_x, point_y, delta_x, delta_y = region
        xmin = point_x - 0.5*delta_x
        xmax = point_x + 0.5*delta_x
        ymin = point_y - 0.5*delta_y
        ymax = point_y + 0.5*delta_y
    else:
        xmin = -2.0
        xmax =  0.75
        ymin = -1.5
        ymax =  1.5

    x_samples = np.linspace(xmin, xmax, width)
    y_samples = np.linspace(ymin, ymax, height)
    z_samples = np.empty((height, width))

    limits = [xmin, xmax, ymin, ymax]

    for col, x in enumerate(x_samples):
        for row, y in enumerate(y_samples):
            z = complex(x, y)
            iterations = mandelbrot_iterations(z, maxiter)
            z_samples[row, col] = iterations
    
    return z_samples, limits


# Plotter for the set data
def plotter(matrix, limits, colormap="Blues"):
    height, width = matrix.shape
    dpi = 96
    size = [width / dpi, height / dpi]

    plt.figure()
    plt.setp(plt.gca(), xticks=[], yticks=[])
    plt.gcf().set_size_inches(size)
    plt.imshow(matrix, origin="lower", cmap=colormap, extent=limits)
    plt.show()

