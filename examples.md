# Examples

**Ex1: Plotting (and saving) the Mandelbrot set in blues**

Using the functions inside ``jmsets.py`` you would need to execute:
``>>> zmat, lims = mandelbrot_set()``. 
Afterwards, the ``plotter`` function can be called as:
``>>> plotter(zmat, lims, colormap='Blues')``
The picture can be saved from the appearing window.

![Example 1](../assets/example-1.png?raw=true)

**Ex2: Zoom over a region of the Mandelbrot set**

Here we do a zoom over the region given by around the (0.3, 0.0) point,
using a dx of 0.1 with dx=dy, resulting in region given by the following
limit values: ``[xmin, xmax, ymin, ymax] = [0.25, 0.35, -0.05, 0.05]``.

``>>> region = [0.3, 0.0, 0.1, 0.1]``
``>>> zmat, lims = mandelbrot_set(region).``
``>>> plotter(zmat, lims)``
![Example 2a](../assets/example-2a.png?raw=true)

If we want a better definition for our picture we can increment the number of 
iterations when calling ``mandelbrot_set``. We can change the color map as well.

``>>> region = [0.3, 0.0, 0.1, 0.1]``
``>>> zmat, lims = mandelbrot_set(region, maxiter=128).``
``>>> plotter(zmat, lims, colormap="Reds")``
![Example 2b](../assets/example-2b.png?raw=true)

**Ex3: Using the ``main_cardioid`` function to generate a random Julia parameter**

``for iter in range(4):``
``    a = random.uniform(-2,2)``
``    c = main_cardioid(a)``
``    zmat, lims = julia_set(c)``
``    plotter(zmat, lims, colormap="prism")``

![Example 3a](../assets/example-3a.png?raw=true) ![Example 3b](../assets/example-3b.png?raw=true)

![Example 3c](../assets/example-3c.png?raw=true) ![Example 3d](../assets/example-3d.png?raw=true)

**Ex4: Incrementing the number of iterations to get a more detailed picture**

In this example we use 7*pi/4 as argument to the main cardioid function. The resulting Julia set is shown here, with
128, 256, 512 and 1024 iterations respectively.

![Example 4a](../assets/example-4a.png?raw=true)

![Example 4b](../assets/example-4b.png?raw=true)

![Example 4c](../assets/example-4c.png?raw=true)

![Example 4d](../assets/example-4d.png?raw=true)
