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
   ![grafico_20part](https://user-images.githubusercontent.com/53713496/68253677-488a0f80-0007-11ea-9114-bad4d27bd530.png)
   
   * para 30 particulas, obtenemos un tiempo de 101,269 seg:
   ![grafico_30part](https://user-images.githubusercontent.com/53713496/68253688-5344a480-0007-11ea-9357-2f5aae681f96.png)
   
   * para 40 particulas, obtenemos un tiempo de 137,651 seg:
   ![grafico_40part](https://user-images.githubusercontent.com/53713496/68253696-56d82b80-0007-11ea-87d1-8ffcf29e16c2.png)
   
   * grafico nunmero de particulas vs tiempo:
   ![grafico nparticulas vs tiempo](https://user-images.githubusercontent.com/53713496/68254682-eda5e780-0009-11ea-9f93-9950d41dee3c.png)

- Comportamiento del codigo segun el ordenador de Maria Jesus Gutierrez:

- Comportamiento del codigo segun el ordenador de Benjamin Kamke:

- Comportamiento del codigo segun el ordenador de Klaus Brien:

   * para 4 particulas, obtenemos un tiempo de 17,549 seg:
   ![grafico_4part](https://user-images.githubusercontent.com/53713496/68255563-5d1cd680-000c-11ea-9078-83a77d206b96.png)

   * para 8 particulas, obtenemos un tiempo de 32,379 seg:
   ![grafico_8part](https://user-images.githubusercontent.com/53713496/68255564-5d1cd680-000c-11ea-9a30-ace07faa1642.png)
   
   * para 10 particulas, obtenemos un tiempo de 34,851 seg:
   ![grafico_10part](https://user-images.githubusercontent.com/53713496/68255565-5d1cd680-000c-11ea-9995-e3f38ed40baa.png)
   
   * para 20 particulas, obtenemos un tiempo de 63,949 seg:
   ![grafico_20part](https://user-images.githubusercontent.com/53713496/68255566-5d1cd680-000c-11ea-955b-e9438f92ef10.png)
   
   * para 30 particulas, obtenemos un tiempo de 108,357 seg:
   ![grafico_30part](https://user-images.githubusercontent.com/53713496/68255567-5db56d00-000c-11ea-90f0-05ad38072578.png)
   
   * para 40 particulas, obtenemos un tiempo de 134,059 seg:
   ![grafico_40part](https://user-images.githubusercontent.com/53713496/68255568-5db56d00-000c-11ea-8594-a8dfbb7a3810.png)
   
   * grafico nunmero de particulas vs tiempo:
   ![grafico npart vs tiempo](https://user-images.githubusercontent.com/53713496/68255562-5c844000-000c-11ea-86f8-c5839f4c2528.png)
   
