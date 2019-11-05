# -*- coding: utf-8 -*-
"""
crear archivo de texto o carpeta con datos de partículas en cada instante
"""
from matplotlib.pylab import *
from parameters import *
from functions import *
import time
import scipy as sp

norm = lambda v: sqrt(dot(v,v))

#reuse_initial_condition = True
reuse_initial_condition = False

doit = True
#doit = False


t = arange(0, tmax, dt)
Nt = len(t)

Nparticulas = 20


if reuse_initial_condition:
    print "reusing initial conditions"
    data = load("initial_condition.npz")
    x0 = data["x0"]    #posicion en x
    y0 = data["y0"]    #posicion en y
    vx0 = data["vx0"]  #velocidad en x
    vy0 = data["vy0"]  #velocidad en y
    Nparticulas = data["Nparticulas"]  #cantidad de particulas con que se trabaja
else:
    print "generating new initial conditions"
    itry = 1
    while True:
         dmin = infty
         x0 = 800 * d * rand(Nparticulas)
         y0 = 5* d * rand(Nparticulas) + 1*d
         for i in range(Nparticulas):
             xi, yi = x0[i], y0[i]
             for j in range(i+1, Nparticulas):
                 xj, yj = x0[j], y0[j]
                 dij = sqrt((xi - xj)**2 + (yi - yj)**2)
                 dmin = min(dmin, dij)
         print "Try # ", itry, "dmin/d = ", dmin/d
         if dmin > 0.9 * d:
             break
         itry += 1
         
    vx0 = ustar * rand(Nparticulas)
    vy0 = 0
    savez("initial_condition.npz", x0 = x0, y0 = y0, vx0 = vx0, vy0 = vy0, Nparticulas = Nparticulas)
        
# 0.14 /0.15e-3    1.4/0.15e-3 = 9333.33
t = arange(0, tmax, dt)
Nt = len(t)

from scipy.integrate import odeint

#guardar solo pasos necesarios 
zk = sp.zeros((4*Nparticulas)) #guardar paso zk
zkm1 = sp.zeros((4*Nparticulas)) #guardar paso zkm1

#condiciones iniciales para zk en tiempo = 0
zk[0::4] = x0
zk[1::4] = y0
zk[2::4] = vx0
zk[3::4] = vy0

#fout = open("resultado.txt", "w") #para guardar datos en archivo de texto
import h5py #para optimizar espacio

fout = h5py.File("resultado.hdf5", "w")
 #se pueden guardar todos lo parametros

fout_parametros = fout.create_group("parametros")

fout_parametros["dt"] = dt
fout_parametros["g"] = g
fout_parametros["d"] = d
fout_parametros["rho_agua"] = rho_agua
fout_parametros["rho_particula"] = rho_particula
fout_parametros["tmax"] = tmax
fout_parametros["Cd"] = Cd
fout_parametros["Cm"] = Cm
fout_parametros["CL"] = CL
fout_parametros["Rp"] = Rp
fout_parametros["ustar"] = ustar
fout_parametros["tau_star"] = tau_star
fout_parametros["R"] = R
fout_parametros["alpha"] = alpha
fout_parametros["ihat"] = ihat
fout_parametros["jhat"] = jhat
fout_parametros["tau_cr"] = tau_cr
fout_parametros["A"] = A
fout_parametros["k_penal"] = k_penal

fout_z = fout.create_dataset("z", (Nt, 1 + 4 * Nparticulas), dtype = double)
# print Nt
# exit(0)

done = zeros(Nparticulas, dtype = int32)
impacting_set = zeros(Nparticulas, dtype = int32)

print "Integrating"
k = 0

import time

start = time.time()

tiempo_bloque_1 = 0
tiempo_bloque_2 = 0

if doit:
    while dt*k < int(tmax/dt - 1)*dt:
        #escribir archivo de texto para cada paso de tiempo
        # fout.write("{}", format(dt*k))
        ti = time.time()
       
        #en cada paso de tiempo se guarda el estado de cada particula
        # savetxt(fout, zk, fmt = "%.10e ", newline = "")
       
        fout_z[k, 0] = dt * k
        fout_z[k, 1:] = zk
        
        tf = time.time()
        tiempo_bloque_1 += tf -ti
        
        #fout.write("\n")
        
        if k % 100 == 0:
            print "k = {}   t = {}  ".format(k, k*dt)
        done *= 0
        
        ti= time.time()
        
        for i in range(Nparticulas):
            irange = slice(4*i, 4*i+4)

            zk_i = zk[irange]
            
            di = d
            if done[i] == 0:
                hay_impacto = False
                impacting_set *= 0
                M = 1
                
                for j in range(i + 1, Nparticulas):
                    jrange = slice(4*j, 4*j+4)
                    zk_j = zk[jrange]
                    dj = d
                    
                    rij = zk_j[0:2] - zk_i[0:2]

                    if norm(rij) < 0.5*(d-dj)*3: #ver si es mas o menos
                        hay_impacto = True
                        impacting_set[0] = i
                        impacting_set[M] = j
                        M += 1
            
                if hay_impacto:
                    zk_all= zk_i
                    for j in impacting_set[1:M]:
                        jrange = slice(4*j, 4*j+4)
                        zk_j = zk[jrange]
                        zk_all = hstack((zk_all, zk_j))
                    
                    zkm1_all =odeint(zp_M_particulas, zk_all, [dt*k, dt*(k+1)], args = (M,))
                    
                    zkm1[irange] = zkm1_all[1,0:4]
                    
                    done[i] = 1
                    pos_j = 1
                    for j in impacting_set[1:M]:
                        jrange = slice(4*j, 4*j+4)
                        zkm1[jrange] = zkm1_all[1,4*pos_j:4*pos_j+4]
                        done[j] = 1
                        pos_j += 1
                else:
                    zkm1_i = odeint(zp_una_particula, zk_i, [dt*k, dt*(k+1)])
                    
                    # z[k+1, irange] = zkm1_i[1,0:4]
                    zkm1[irange] = zkm1_i[1,0:4]
                    done[i] = 1
        
        tf = time.time()
        tiempo_bloque_2 = tf - ti
        
        zk = zkm1
        k += 1 #k representa paso de tiempo

end = time.time()


print "tiempo_bloque_1: ", tiempo_bloque_1
print "tiempo_bloque_2: ", tiempo_bloque_2
print "tiempo total: ", end - start

print "Tiempo de escritura es {}\% del tiempo total.", format(tiempo_bloque_1/(end - start) * 100)

fout.close()                    
