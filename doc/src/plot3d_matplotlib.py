import os
from math import *
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

font = {'size'   : 24}
font2 = {'size'   : 12}

h0 = 2277.   # Height of the top of the mountain (m)
R = 4.       # Radius of the mountain (km)
#endinitvalues

# Grid for x, y values (km)
x = y = np.linspace(-10.,10.,41)
xv, yv = np.meshgrid(x, y, indexing='ij', sparse=False)

# indexing='ij' means an xy-coordinate system
# indexing='xy' means coordinates as row/column indices in a matrix
hv = h0/(1 + (xv**2+yv**2)/(R**2))      # Elevation coordinates (m)
# endinitgrid

s = np.linspace(0, 2*np.pi, 100)
curve_x = 10*(1 - s/(2*np.pi))*np.cos(s)
curve_y = 10*(1 - s/(2*np.pi))*np.sin(s)
curve_z = h0/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))
# endparamcurve




# Simple plot of mountain
from matplotlib import cm

fig = plt.figure(1)
ax = fig.gca(projection='3d')
ax.plot_wireframe(xv, yv, hv, rstride=2, cstride=2)

# Simple plot of mountain and parametric curve
fig = plt.figure(2)
ax = fig.gca(projection='3d')
ax.plot_surface(xv, yv, hv, cmap=cm.coolwarm, rstride=1, cstride=1)

# add the parametric curve. linewidth controls the width of the curve
ax.plot(curve_x, curve_y, curve_z, linewidth=5)
# endsimpleplots



h0 = 22.77
R = 4.

hv = h0/(1 + (xv**2+yv**2)/(R**2))

# Define a coarser grid for the vector field
x2 = y2 = np.linspace(-10.,10.,11)
x2v, y2v = np.meshgrid(x2, y2, indexing='ij', sparse=False)
h2v = h0/(1 + (x2v**2 + y2v**2)/(R**2)) # Surface on coarse grid
# endcoarsergrid

dhdx, dhdy = np.gradient(h2v) # dh/dx, dh/dy
# endgradient


# Default two-dimensional contour plot with 7 colored lines
fig = plt.figure(3)
ax = fig.gca()
ax.contour(xv, yv, hv)

# Default three-dimensional contour plot
fig = plt.figure(4)
ax = fig.gca(projection='3d')
ax.contour(xv, yv, hv)

# Plot of mountain and contour lines projected on the coordinate planes
fig = plt.figure(5)
ax = fig.gca(projection='3d')
ax.plot_surface(xv, yv, hv, cmap=cm.coolwarm, rstride=1, cstride=1)
# zdir is the projection axis
# offset is the offset of the projection plane
ax.contour(xv, yv, hv, zdir='z', offset=-1000, cmap=cm.coolwarm)
ax.contour(xv, yv, hv, zdir='x', offset=-10,   cmap=cm.coolwarm)
ax.contour(xv, yv, hv, zdir='y', offset=10,    cmap=cm.coolwarm)

# View the contours by displaying as an image
fig = plt.figure(6)
ax = fig.gca()
ax.imshow(hv)

# 10 contour lines (equally spaced contour levels)
fig = plt.figure(7)
ax = fig.gca()
ax.contour(xv, yv, hv, 10)

# 10 black ('k') contour lines
fig = plt.figure(8)
ax = fig.gca()
ax.contour(xv, yv, hv, 10, colors='k')

# Specify the contour levels explicitly as a list
fig = plt.figure(9)
ax = fig.gca()
levels = [500., 1000., 1500., 2000.]
ax.contour(xv, yv, hv, levels=levels)

# Add labels with the contour level for each contour line
fig = plt.figure(10)
ax = fig.gca()
cs = ax.contour(xv, yv, hv)
plt.clabel(cs)
#end contourplots






# Draw contours and gradient field of h
fig = plt.figure(11)
ax = fig.gca()
ax.quiver(x2v, y2v, dhdx, dhdy, color='r',
          angles='xy', scale_units='xy')
ax.contour(xv, yv, hv)
plt.axis('equal')
# end draw contours and gradient field of h

# Draw contours and normal vector field of h
fig = plt.figure(12)
ax = fig.gca(projection='3d')

ax.quiver(x2v, y2v, h2v, -dhdx, -dhdy, np.ones_like(dhdx),\
          color='r', length=2)
ax.contour(xv, yv, hv, 20)
# end draw contours and normal vector field of h

# Draw surface and normal vector field of h
fig = plt.figure(13)
ax = fig.gca(projection='3d')
ax.plot_surface(xv, yv, hv, cmap=cm.coolwarm, rstride=1, cstride=1)
# length controls the length of the vectors
ax.quiver(x2v, y2v, h2v, -dhdx, -dhdy, np.ones_like(dhdx),\
          color='r', length=2)
# end draw surface and normal vector field of h

h0 = 22.77   # Height of the top of the mountain (m)
R = 4.

x = y = np.linspace(-10.,10.,41)
xv, yv = np.meshgrid(x, y, sparse=False, indexing='ij')
hv = h0/(1 + (xv**2+yv**2)/(R**2))

# Define grid for 3D gradient field
x2 = y2 = np.linspace(-10.,10.,5)
z2 = np.linspace(0, 50, 5)
x2v, y2v, z2v = np.meshgrid(x2, y2, z2, indexing='ij', sparse=False)
h2v = h0/(1 + (x2v**2 + y2v**2)/(R**2))
g2v = z2v - h2v
dhdx, dhdy, dhdz = np.gradient(g2v)
# end define grid for 3D gradient field

# Draw 3D vector field with countours of 3D scalar field
fig = plt.figure(14)
ax = fig.gca(projection='3d')
# opacity controls how contours are visible through each other
for lev in [5, 15, 25, 35, 45]:
    ax.plot_surface(xv, yv, hv + lev, cmap=cm.coolwarm,\
                    rstride=1, cstride=1)

# scale_mode='none' says that the vectors should not be scaled
ax.quiver(x2v, y2v, z2v, dhdx, dhdy, dhdz, color='r', length=4)
# end draw 3D vector field with countours of 3D scalar field


plt.rc('font', **font)

plt.figure(1)
plt.savefig('images/simple_plot_matplotlib.pdf')
plt.savefig('images/simple_plot_matplotlib.png')

plt.figure(2)
plt.savefig('images/simple_plot_colours_matplotlib.pdf')
plt.savefig('images/simple_plot_colours_matplotlib.png')

# Save contour plots

plt.figure(3)
plt.savefig('images/default_contour_matplotlib.pdf')
plt.savefig('images/default_contour_matplotlib.png')

plt.figure(4)
plt.savefig('images/default_contour3_matplotlib.pdf')
plt.savefig('images/default_contour3_matplotlib.png')

plt.figure(5)
plt.savefig('images/contour3_dims_matplotlib.png')
plt.savefig('images/contour3_dims_matplotlib.pdf')

plt.figure(6)
plt.savefig('images/contour_imshow_matplotlib.pdf')
plt.savefig('images/contour_imshow_matplotlib.png')

plt.figure(7)
plt.savefig('images/contour_10levels_matplotlib.pdf')
plt.savefig('images/contour_10levels_matplotlib.png')

plt.figure(8)
plt.savefig('images/contour_10levels_black_matplotlib.pdf')
plt.savefig('images/contour_10levels_black_matplotlib.png')

plt.figure(9)
plt.savefig('images/contour_speclevels_matplotlib.pdf')
plt.savefig('images/contour_speclevels_matplotlib.png')

plt.figure(10)
plt.savefig('images/contour_clabel_matplotlib.pdf')
plt.savefig('images/contour_clabel_matplotlib.png')


# Save vector field plots

plt.rc('font', **font2)

plt.figure(11)
plt.savefig('images/quiver_matplotlib_advanced.pdf')
plt.savefig('images/quiver_matplotlib_advanced.png')

plt.rc('font', **font)

plt.figure(12)
plt.savefig('images/quiver_contour_matplotlib.png')
plt.savefig('images/quiver_contour_matplotlib.pdf')

plt.figure(13)
plt.savefig('images/quiver_surf_matplotlib.png')
plt.savefig('images/quiver_surf_matplotlib.pdf')

plt.rc('font', **font2)

plt.figure(14)
plt.savefig('images/quiver_matplotlib.png')
plt.savefig('images/quiver_matplotlib.pdf')
