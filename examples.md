# Examples

**Ex1: Plotting (and saving) the Mandelbrot set in blues**

The full command
``>>> mplot(samples=512, n_iter=64,  region=None, p=0, colormap='Blues', savefig=True)``

Or, more simply
``>>> mplot(savefig=True)``
![Example 1a](https://i.imgsafe.org/0d52c6399a.png)

With a little bit of blur:
``>>> mplot(savefig=True, p=0.001)``
![Example 1b](https://i.imgsafe.org/0d5301b825.png)

**Ex2: Zoom over a region of the Mandelbrot set**

Here we do a zoom over the region given by ``[xmin, xmax, ymin, ymax] = [0.25, 0.35, -0.05, 0.05]``.
For this, we first define the region ``r`` then give it as an argument to the ``mplot`` function:

```
>>> r = [0.25, 0.35, -0.05, 0.05]
>>> mplot(savefig=True, region=r)
```
![Example 2a](https://i.imgsafe.org/0d5304543a.png)

If we want a better definition for our picture we can increment the number of iterations. We can 
change the color map as well.

```
>>> r = [0.25, 0.35, -0.05, 0.05]
>>> mplot(savefig=True, region=r, n_iter=128, colormap='Reds')
```
![Example 2b](https://i.imgsafe.org/0d531261c8.png)

**Ex3: Using the ``main_cardiod`` function to generate a random Julia parameter**

The next code generates 4 random complex numbers and plugs them into the ``jplot`` function. 
It saves each figure as a 250x250 pixels PNG file.

```
for iter in range(4):
  a = random.uniform(-2,2)
  c = main_cardioid(a)
  jplot(c, samples=1024, savefig=True, size=[2.5,2.5], colormap='prism')
```
![Example 3a](https://i.imgsafe.org/0db1989d4c.png) ![Example 3b](https://i.imgsafe.org/0db19e95e3.png)

![Example 3c](https://i.imgsafe.org/0db1a99792.png) ![Example 3d](https://i.imgsafe.org/0db1b82f89.png)

**Ex4: Incrementing the number of iterations to get a more detailed picture**

In this example we use 7*pi/4 as argument to the main cardioid function. The resulting Julia set is shown here, with
128, 256, 512 and 1024 iterations respectively.

![Example 4a](../assets/example-4a.png?raw=true)

![Example 4b](../assets/example-4b.png?raw=true)

![Example 4c](../assets/example-4c.png?raw=true)

![Example 4d](../assets/example-4d.png?raw=true)
