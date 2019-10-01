from matplotlib.pylab import *

# Unidades base SI (m, kg, s)
_m = 1.
_kg = 1.
_s = 1.
_mm = 1e-3*_m
_gr = 1e-3*_kg 


vf_x = 5.0*_m/_s
vf_y = 0.0*_m/_s

x_0 = array([0., 1.], dtype=double)
v_0 = array([1., 1.], dtype=double)

x_i = zeros(2, dtype=double)      # posicion actual
v_i = zeros(2, dtype=double)      # velocidad actual
x_i_m1 = zeros(2, dtype=double)   # posicion siguiente
v_i_m1 = zeros(2, dtype=double)   # velocidad siguiente

g = 9.81*_m/(_s**2)         # gravedad
d = 1*_mm                   # diametro de la particula
rho = 1550*_kg/(_m**3)      # densidad de la particula, considerando que sea arena 
Cd = 0.47                   # coeficiente de Drag para particula esferica

m = rho*pi*((d/2)**3)*(4/3) # masa de la particula


# Inicializar Euler en x_0
dt = 2e-6*_s    # paso de tiempo 
tmax = 1*_s    # tiempo máximo de simulacion
ti = 0.*_s     # tiempo actual

W = array([0., -m*g])  #Fuerza de peso 
vf = array([vf_x, vf_y])

Nt = int32(2*tmax / dt)
x_store = x_0 #zeros((2, Nt))
v_store = v_0 #zeros((2, Nt))
t_store = zeros(Nt)

#metodo de euler
x_store=[]
v_store=[]
i = 0

while ti < tmax:

	if i % 100 == 0:
		print "ti =", ti," |x| =", sqrt(dot(x_i,x_i))
    	#print "xi =", xi
    	#print "vi =", vi

	# evaluar v relativa
	vrel = vf - v_i                      # velocidad relativa
	norm_vrel = sqrt(dot(vrel, vrel))   # norma velocidad relativa

	# evaluar fuerzas sobre la particula
	fD = 0.5*Cd*norm_vrel*vrel          # Fuerza de Drag
	Fi = W + fD                               # Sumatoria de todas las fuerzas que se ejercen sobre la particula

	#print "Fi =", Fi
	# evaluar aceleracion
	ai = Fi / m

	#print "a_i =", a_i
	# integrar
	xim1 = x_i + v_i*dt + ai*(dt**2/2)
	vim1 = v_i + ai*dt

	# avanzar al siguiente paso
	t_store[:] = ti

	ti += dt
	i += 1
	x_i = xim1
	v_i = vim1
	x_store.append(x_i)
	v_store.append(v_i)

# guardar ultimo paso
x_store.append(x_i)
v_store.append(v_i)
#t_store[:] = ti

#print x_store
#print v_store
figure()
plot(x_store, v_store)
show()
