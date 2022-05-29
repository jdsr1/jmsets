/*
 * Iterator functions for Julia and Mandelbrot sets.
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <complex.h>

// Prototypes

int julia_iter(complex, complex, int);
int* julia_set(complex, int, int, int);


int julia_iter(complex z0, complex param, int maxit) {
    float boundary;
    complex zn;

    zn = z0*z0 + param;

    boundary = 0.5 + 0.5*csqrt(1.0 + 4.0*cabs(param));

    for (int i=0; i<maxit; i++) {
        if (cabs(zn) > boundary)
            return i;
        zn = zn*zn + param;
    }

    return maxit;
}


int* julia_set(complex param, int width, int height, int maxit) {
    float boundary, step, xmin, xmax, ymin, ymax, limits[4];
    float x_samples[width], y_samples[height];
    complex z0;
    int i, iter, j, zi;
    int *z_samples;

    boundary = 0.5 + 0.5*csqrt(1.0 + 4.0*cabs(param));

    xmin = -boundary;
    xmax = boundary;
    ymin = xmin;
    ymax = xmax;

    step = 2.0*boundary/(width-1);
    for (i=0; i < width; i++) {
        x_samples[i] = xmin + i*step;
    }

    step = 2.0*boundary/(height-1);
    for (j=0; j < height; j++) {
        y_samples[j] = xmin + j*step;
    }

    z_samples = malloc(width*height*sizeof(int));

    for (i=0; i < width; i++) {
        for (j=0; j < height; j++) {
            z0 = x_samples[i]*I + y_samples[j];
            iter = julia_iter(z0, param, maxit);
            zi = i*width + j;
            z_samples[zi] = iter;
        }
    }

    return z_samples;
}
