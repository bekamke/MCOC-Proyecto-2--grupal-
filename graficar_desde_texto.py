# -*- coding: utf-8 -*-
"""
para graficar partículas a partir de archivo creado 

"""
from matplotlib.pylab import *

datos = loadtxt("resultado.txt")

print daros.shape
d = 0.15e-3

Nparticulas = (datos.shape[1]- 1)/4

figure ()

color = "#006893"
ax = gca()
colorlist = []
for i in range(Nparticulas):
    xi = datos[:, 1 + 4*i]/d 
    yi = datos[:, 1 + 4*i + 1]/d
    col = rand(3)
    colorlist.append(col)
    ax.plot(xi[0::100], yi[0::100], "o", color = col)
    ax.plot(xi, yi, "--", color = col, alpha = 0.5)
    
ax.set_ylim([0,5])
ax.axhline(0., color="k", linestyle = "--")
ax.axhline(1/30.,color="gray", linestyle = "--")
ax.set_xlabel("$\\dfrac{x}{d}$")
ax.set_ylabel("$\\dfrac{z}{d}$")

tight_layout()

show()



