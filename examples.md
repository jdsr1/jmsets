# Examples

**Ex1: Plotting (and saving) the Mandelbrot set in blues**

The full command
``>>> mplot(samples=512, n_iter=64,  region=None, p=0, colormap='Blues', savefig=True)``

Or, more simply
``>>> mplot(savefig=True)``

With a little bit of blur:
``>>> mplot(savefig=True, p=0.001)``

**Ex2: Zoom over a region of the Mandelbrot set**

Here we do a zoom over the region given by ``[xmin, xmax, ymin, ymax] = [0.25, 0.35, -0.05, 0.05]``.
For this, we first define the region ``r`` and give it as an argument to the ``mplot`` function:

```
>>> r = [0.25, 0.35, -0.05, 0.05]
>>> mplot(savefig=True, region=r)
```

If we want a better definition for our picture we can increment the number of iterations. We can 
change the color map as well.

```
>>> r = [0.25, 0.35, -0.05, 0.05]
>>> mplot(savefig=True, region=r, n_iter=128, colormap='Reds')
```
