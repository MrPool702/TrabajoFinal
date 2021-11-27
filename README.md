# TrabajoFinal
## Integrantes
| Nombre     | Código | 
| :---        |    ----:   |       
|  More Perez Moises Ernesto      | 201910358 | 
| Cahuas Vergara Miguel Angel   | 202016505 | 
| Escobedo Mori Jorgeluis| 201924132 |
| Aquino Iman Herly Fernando| 20171E997 |
| Leon Leon John Sahir| 20191C036 |
*todas los issues tiene su propia respuesta y anexos dentro de sus comentarios*
## Video expositivo del grupo trabajo  parcial
https://www.youtube.com/watch?v=xtsQ3pcKnEA

## Video expositivo del grupo trabajo  final
https://www.youtube.com/watch?v=UjpI2oN7iUg

# Informe del Trabajo Final

####UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS

- CURSO DE Complejidad algorítmica
- Carrera de ingeniería de Software
- Sección WV72
- Ciclo 2021-02

# CONTENIDO
1.	Introducción
2.	Problema planteado
3.	Objetivos
4.	Generación del grafo
5.	Conceptos de los algoritmos
6.	Prueba de algoritmos
7.	referencias

# Introducción
Para el curso de complejidad algorítmica, se pidio desarrollar un algoritmo que sea capaz de generar un grafo de alrededor de un millón de nodos, esto con la finalidad de poder simular un problema de contexto real el cual sería el de hallar el camino óptimo entre destinos y puntos de partida. Para esto durante el curso se nos explicó distintos conceptos y algoritmos que nos podrán ayudar con el desarrollo del trabajo. Cabe mencionar que todo el trabajo debía ser desarrollado en Python. Además de que cada avance debía ser registrado en un repositorio de GitHub.

# Problema planteado
El caso que nos entregaron consistía en desarrollar un algoritmo el cual sea capaz de generar un grafo con detalles específicos, uno de ellos era que dicho grafo tuviese puntos de entregas y puntos de almacenamiento en zonas aleatorias del grafo además de tener pesos o distancias razonables, además lo mencionado anteriormente era requerido escribir un algoritmo capaz de recorrer todo el grafo y hallar las distancia entre los puntos de entrega y los puntos de almacenamiento, esto en base al peso de los nodos en el grafo.  El trabajo final nos permitía escoger un algoritmo existente e implementar mejoras de modo que sea más eficiente, además de sustentarlo o en el mejor de los casos desarrollar un nuevo algoritmo desde cero que cumpla con los requisitos solicitados por el trabajo.

# Objetivos
El objetivo del curso era demostrar que tenemos la habilidad de poder desarrollar soluciones competentes que tenga peso y relevancia en el mundo laboral actual, para esto se nos dio un caso de contexto real donde debíamos diseñar un algoritmo complejo que le dé solución a problema de contexto real y común en el día a día, como lo es hallar la ruta más corta entre caminos. Para ello no solo debíamos crear soluciones eficientes, sino que además de ello era necesario tomar en cuentas restricciones extras como lo era determinar que el tiempo y costo de memoria de nuestra solución sea compatible con todo tipo de computador, de esta forma desarrollando una solución eficiente. 

# Generación del grafo
Para la generación del grafo hicimos uso de un pequeño data set el cual contenía 1 millón de elementos, los cuales consistían datos numéricos específicos que cumplirían la función representarían los nodos del grafo. Para que el compilador sea capaz de interpretar dichos elementos decidimos crear una clase llamada “Punto” los cuales estarían encargados de almacenar los datos de la data set uno por uno y a su vez esta clase punto estaría almacenada en una lista. 

# Conceptos empleados
- # Relajación lineal:  
Relajación consiste principalmente en seleccionar o delimitar un subconjunto de restricciones del problema de optimización a resolver y devolver el conjunto de las mejores soluciones factibles encontradas hasta ese momento, en tal caso se actualiza el valor de la mejor solución factible.

- ## Funciones heurísticas para mejorar y limitar el Dijkstra:
La función heurística es uno de los conceptos más básicos de la inteligencia artificial, pues con este se trata de buscar la mejor medida a un problema dado en este caso en específico se decidió se decidió emplear el algoritmo para la optimización del algoritmo de Dijkstra pues haciendo uso de este concepto podemos limitar la búsqueda entre camino que realiza el algoritmo de Dijkstra, aunque una de las desventajas de esta técnica es que no asegura que siempre devuelva la mejor solución existente. 
 
- # Back Tracking:
Back tracking es el algoritmo de búsqueda profunda más conocido para el recorrido de árboles y grafos pues con este se puede recorrer cada uno de los nodos que conforman la estructura a recorrer, para el desarrollo del trabajo final uno de nuestros compañeros hizo uso de esta técnica en sus algoritmos con la finalidad de obtener un recorrido completo del grafo y de esa forma encontrar el camino más corto entre nodos. 


# Prueba de algoritmos
para la parte final del trabajo cada integrante del grupo desarrollo e implemento una mejora al algoritmo de Dijkstra haciendo uso de nuevos conceptos aprendidos durante el curso y algunos otros conceptos aprendidos mediante repositorios académicos, uno de los conceptos más usado en la implementación de los algoritmos fueron las funciones heurísticas, pues con esta técnica se podía limitar la búsqueda del algoritmo de Dijkstra y a la vez obtener un mejor tiempo de compilación. Por otro lado, otro de los conceptos usados fue el algoritmo estrella con esta función se buscó mejorar el tiempo de compilación del algoritmo y encontrar el camino mas corto entre nodos más eficiente.

# Referencias
- •	Wikipedia contributors. (2021, 18 noviembre). A* search algorithm. Wikipedia.
 Recuperado 20 de noviembre de 2021, de https://en.wikipedia.org/wiki/A*_search_algorithm
- •	Wikipedia contributors. (2021a, julio 5). D*. Wikipedia. Recuperado 19 de noviembre de 2021, de https://en.wikipedia.org/wiki/D*
