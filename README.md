# MCOC-Proyecto-2
# INTRODUCCION:
En este proyecto se implementará y validará un modelo de simulación de transporte de
sedimentos en base a un método lagrangiano, es decir que sigue a cada partícula individualmente.
La validación se hará a nivel del comportamiento de una partícula y luego con el comportamiento
estadístico de cantidades crecientes de partículas. Además, se explorará cómo influyen las
decisiones de algoritmo de implementación, conocido como complejidad computacional, y
métodos de input-output (IO) en el rendimiento del programa.

# OBJETIVOS:
Diseñar un modelo que simule el transporte de partículas de sedimento en el fondo del agua.
Entender la influencia de la implementación de algoritmos computacionales, entre ellos
algoritmos de complejidad computacional y métodos (IO).
[Meta 3]: implementación del código para una partícula con perfil de velocidad

# RESULTADOS PARA UNA PARTÍCILA:

Para el estudio del comportamiento de una partícula transportada por un fluido se usaron los siguinetes datos y supuestos:
* La partícula transportada corresponde a una grano de arena
* La forma de la artícula es considerada como esférica 
* EL comportamiento se estudia mediante relaciones Euler-Lagrange

* Datos usados

    * diámetro de partícula = 1 mm
    * densidad de partícula = 155 kg/m^3
    * coeficiente Drag para partícula esférica = 0,47

El desplazamiento en x de la partícula según la velocidad con que se mueve se muestran el el siguiente gráfico, donde el eje "x" representa el desplazameinto y el eje "y" la velocidad en cierto instante 

![real p2](https://user-images.githubusercontent.com/53712876/65996866-a65a9300-e46e-11e9-945e-d2ca47f3125f.png)

# ENTREGA 6 (CODIGO OPTIMIZADO)
- Comportamiento del codigo segun el ordenador de Santiago Moreno:
   * para 4 particulas, obtenemos un tiempo de 17,047 seg:
   ![grafico_4part](https://user-images.githubusercontent.com/53713496/68253233-293eb280-0006-11ea-8581-3c22d9eae137.png)
   
   * para 8 particulas, obtenemos un tiempo de 31,409 seg:
   ![grafico_8part](https://user-images.githubusercontent.com/53713496/68253550-ee894a00-0006-11ea-9731-2be3b19561dc.png)
   
   * para 10 particulas, obtenemos un tiempo de 42,083 seg:
   ![grafico_10part](https://user-images.githubusercontent.com/53713496/68253621-1d9fbb80-0007-11ea-83bc-dbe6a0f05ea4.png)
   
   * para 20 particulas, obtenemos un tiempo de 63,878 seg:
   
