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

   * para 4 particulas, obtenemos un tiempo de 11,138 seg:
![caso 4 particulas](https://user-images.githubusercontent.com/53712876/68254991-c56ab880-000a-11ea-8405-7266a9fd5e24.png)

   * para 8 particulas, obtenemos un tiempo de 20,366 seg:
![caso 8 particulas](https://user-images.githubusercontent.com/53712876/68254992-c56ab880-000a-11ea-8ed8-c3c7592c6357.png)

   * para 10 particulas, obtenemos un tiempo de 26,812 seg:
![caso 10 particulas](https://user-images.githubusercontent.com/53712876/68254986-c4398b80-000a-11ea-923a-94f340d35670.png)

   * para 20 particulas, obtenemos un tiempo de 51,012 seg
![caso 20 particulas](https://user-images.githubusercontent.com/53712876/68254988-c4d22200-000a-11ea-94d3-8b97c538c477.png)

   * para 30 particulas, obtenemos un tiempo de 80,007 seg:
![caso 30 particulas](https://user-images.githubusercontent.com/53712876/68254989-c4d22200-000a-11ea-954f-802edaeb0815.png)

   * para 40 particulas, obtenemos un tiempo de 106,704 seg:
![caso 40 particulas](https://user-images.githubusercontent.com/53712876/68254990-c4d22200-000a-11ea-9ca0-53b32edc15d3.png)

   * gráfico número de partículas vs tiempo:
   
![grafico](https://user-images.githubusercontent.com/53712876/68255882-3f9c3c80-000d-11ea-8814-67558180dc44.png)

- Comportamiento del codigo segun el ordenador de Benjamin Kamke:

   * para 4 particulas, obtenemos un tiempo de 52,38 seg:
![Para 4 particulas](https://user-images.githubusercontent.com/53590243/68257811-f21ed000-000a-11ea-83d0-2762e4da6241.png)
 
   * para 8 particulas, obtenemos un tiempo de 101,1 seg:
![Para 8 particulas](https://user-images.githubusercontent.com/53590243/68257868-22666e80-000b-11ea-90da-a89cf9b2a56e.png)

   * para 10 particulas, obtenemos un tiempo de 133,025 seg:   
![para 10 particulas](https://user-images.githubusercontent.com/53590243/68257942-60fc2900-000b-11ea-8bd7-ba73365f999d.png)

   * para 20 particulas, obtenemos un tiempo de 272,6 seg:
![Para 20 particulas](https://user-images.githubusercontent.com/53590243/68257965-82f5ab80-000b-11ea-8768-4186199993c9.png)

   * para 30 particulas, obtenemos un tiempo de 490,74 seg:
![Para 30 particulas](https://user-images.githubusercontent.com/53590243/68258104-031c1100-000c-11ea-9faf-d770fd36ea67.png)


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

