from matplotlib.pylab import *

# Unidades base SI (m, kg, s)
_m = 1.
_kg = 1.
_s = 1.
_mm = 1e-3*_m
_gr = 1e-3*_kg 

# velocidades iniciales
vfx = 5.0*_m/_s
vfy = 0.0*_m/_s

x0 = array([0., 1.], dtype=double)
v0 = array([1., 1.], dtype=double)

xi = x0 #zeros(2, dtype=double)      # posicion actual
vi = v0 #zeros(2, dtype=double)      # velocidad actual
xim1 = zeros(2, dtype=double)   # posicion siguiente
vim1 = zeros(2, dtype=double)   # velocidad siguiente

g = 9.81*_m/(_s**2)         # gravedad
d = 1*_mm                   # diametro de la particula
rho = 2700*_kg/(_m**3)      # densidad de la particula, considerando que sea arena 
Cd = 0.47                   # coeficiente de Drag para particula esferica

m = rho*(4./3./8.)*pi*(d**3) # masa de la particula

# Inicializar Euler en x_0
dt = 2e-6*_s    # paso de tiempo 
tmax = 0.1*_s    # tiempo maximo de simulacion
ti = 0.*_s     # tiempo actual

W = array([0., -m*g])  #Fuerza de peso 
vf = array([vfx, vfy])

Nt = int32(2*tmax / dt) # numero de tiempos que tengo
x_store = zeros((2, Nt))
v_store = zeros((2, Nt))
t_store = zeros(Nt)

# metodo de euler
i = 0
while ti < tmax:

	if i % 100 == 0:
		print "ti =", ti," |xi| =", sqrt(dot(xi,xi))
    	#print "xi =", xi
    	#print "vi =", vi

	# evaluar v relativa
	vrel = vf - vi                      # velocidad relativa
	norm_vrel = sqrt(dot(vrel, vrel))   # norma velocidad relativa

	# evaluar fuerzas sobre la particula
	fD = 0.5*Cd*norm_vrel*vrel          # Fuerza de Drag
	Fi = W + fD                               # Sumatoria de todas las fuerzas que se ejercen sobre la particula

	#print "Fi =", Fi

	# evaluar aceleracion
	ai = Fi / m
	#print "a_i =", a_i

	# integrar
	xim1 = xi + vi*dt + ai*(dt**2/2) # base del algoritmo, se calcula la posicion con esta formula
	vim1 = vi + ai*dt

	# avanzar al siguiente paso
	x_store[:, i] = xi
	v_store[:, i] = vi
	t_store[:] = ti

	ti += dt
	i += 1
	xi = xim1
	vi = vim1
	

# guardar ultimo paso
x_store[:, i] = xi
v_store[:, i] = vi
t_store[i] = ti

print x_store

figure()
plot(x_store[0, :i], x_store[1, :i])
show()
