# Libreria-juegos-cuanticos

Esta libreria esta hecha con el fin de hacer pruebas sobre juegos ya sean deterministicos, probabilisticos o cuanticos

### Para usar la libreria

Se requiere tener instalado numpy y matplotlib estas se pueden instalar py -m pip install --nombre de liberia--

## Descripcion:
la libreria funciona con juegos deteerministicos , probabilisticos y cuanticos, dentro de estos las funciones son claras en su funcionamiento y coincidero que la parte 
mas importante por aclarar son:

### Uso de los imaginarios
Para los imaginarios se usa la naturaleza de estos en python es decir siempre que vaya una i se pondra una j.Algo importante es que la j tiene que estar siempre acompañada por un numero real es decir si dado el caso tengo un i solo es decir 1i pues en python pondre 1j para evitar problemas con las operacion de estos numeros, demas la libreria hara el resto apoyandose de numpy  para los arreglos o matrices segun se necesite.

### Observables 
Como se ve esta libreria esta basada en clases y objetos, en esta clase de observables he querido implementar la parte de que se grafique de manera correcta teniendo la funcion de graficar dentro de esta clase, esta funcion se encargara de graficar los valores y vectores propios de una matriz cuales quiera, ademas de eso mostrara la probabilidad de que del estado inicial pase a alguna de sus vectores propios es por esto que el objeto "graficador" pide un estado que seria el inicial que tiene.
Si se desea saber los vectores propios y valores propios ademas de sus probabilidades hayq ue llamar la funcion graficador en vez de las funciones de cada uno separado, aunque es posible y no habra ningun problema este dara el valor suelto sin el formato hehco en graficador.

Ademas de esto esta la implementacion de si la matriz es hermitania se hayara el valor esperado, es importante que si se quiere saber si la matriz es hermitania tambien hay una funcion o objeto segun se quiera ver, la cual devolvera un booleano donde nos dira si es o no es.

Lo mismo pasara con que si esta normalizado el vector estado o no y si se quiere normalizarlo tambien se podra hacer con la funcion normalizer la cual recibira el estado que se quiera normalizar.

## Entrada de datos:
los ticks se insertaran con un solo numero es decir ejemplo : 3 *enter* si se quiere se podra modificar desde el codigo fuente.
ademas para solucionar uno de los ejercicios el 4.4.2 en vez de ticks es steps pero en escencia sera lo mismo ya que para ese aunque la solucion se implemtenta
usando 3 pasos igual el libro pedia que esta se diera por una entrada.

## CASOS DE USO:
### DETERMINISTICO:
matriz = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
estado = [3,2,5,9,0,7]

### PROBABILISTICO:
MATRIZ = [[0,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[0,1/3,0,0,1,0,0,0,0,0,0],[0,1/3,0,0,0,1,0,0,0,0,0],[0,1/3,1/3,0,0,0,1,0,0,0,0],[0,0,1/3,0,0,0,0,1,0,0,0],[0,0,1/3,1/3,0,0,0,0,1,0,0],[0,0,0,1/3,0,0,0,0,0,1,0],[0,0,0,1/3,0,0,0,0,0,0,1]]
estado = [1,0,0,0,0,0,0,0,0,0,0]

### CUANTICO:
rendija1 = [[0,0,0,0,0,0,0,0],[1/math.sqrt(2),0,0,0,0,0,0,0],[1/math.sqrt(2),0,0,0,0,0,0,0], [0,-1/math.sqrt(6)+1j/math.sqrt(6),0,1,0,0,0,0],[0,-1/math.sqrt(6)-1j/math.sqrt(6),0,0,1,0,0,0],[0,1/math.sqrt(6)-1j/math.sqrt(6),-1/math.sqrt(6)+1j/math.sqrt(6),0,0,1,0,0],[0,0,-1/math.sqrt(6)-1j/math.sqrt(6),0,0,0,1,0],[0,0,1/math.sqrt(6)-1j/math.sqrt(6),0,0,0,0,1]]
estado = [1,0,0,0,0,0,0,0]

### OBSERVABLES:
observable = [[1/2,0],[0,1/2]]
psi = [1,0] el cual 
y como vectores para probar la probabilidad de ellos
vec = [1, 1]
vec2 = [-1,1]

no interesa que no esten normalizdos ya que la funcion esta implementada para normalizarlos.

## Autor
David eduardo Valencia
