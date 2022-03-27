"""Hecho por David Eduardo Valencia CNYT"""
import numpy as np
from  numpy import linalg as LA
import math
import matplotlib.pyplot as plt
from sys import stdin

class observables:
    def __init__(self,matriz = [], estado = []):
        self.observable = matriz


    def valorEsperado(self,matriz,psi):
        psi = np.array(psi)
        if self.itsHermitain(matriz):
            operacion = np.inner(psi.conjugate(),np.dot(matriz,psi))
        return operacion

    def particulaLinea(self, particulas, v1, v2):
        posibilidad = 2**particulas

        return posibilidad
    def probabilidadObser(self,estado):
        probalidad = []
        for i in estado:
            a = i.real
            b = i.imag
            operacion = (math.sqrt(a**2 + b**2))**2
            probalidad.append(operacion)
        return probalidad



    def valorpropio2(self, matriz):
        w, v = LA.eig(matriz)  # La w representara los valores propios y sus vectores a forma de tupla
        v = np.transpose(v)
        return w, v


    def transiciones(self,estado,vector1):
        if self.itsNormalized(vector1):
            operacion = np.inner(np.conjugate(vector1),estado)
            operacion = round(operacion ** 2, 1) * 100
            return operacion
        else:
            vector = self.normalizer(vector1)
            operacion = np.inner(np.transpose(vector), estado)
            operacion = round(operacion**2,1)*100
            return operacion


    def itsHermitain(self, matriz):
        matriz = np.matrix(matriz)
        matrizDagger = matriz.getH()
        return (np.array_equal(matriz, matrizDagger))

    def itsNormalized(self, estado):
        if math.ceil(LA.norm(estado)) == 1:
            return True
        else:
            return False

    def normalizer(self,estado):
        auxiliar = []
        if not self.itsNormalized(estado):
            for i in (estado):
                auxiliar.append(i/LA.norm(estado))
            estadoprovi = auxiliar
        else:
            estadoprovi = estado
        return estadoprovi


    def graficador(self,matriz, estado):  # aqui se mostrara los vectores y valores propios ademas de la probabilidad de transicion de estados
        valores, vectores = self.valorpropio2(matriz)
        contador = 0
        for i in valores:
            contador += 1
            print("Valor propio #", contador, "\n", i)
        contador2 = 0
        for i in vectores:
            contador2 += 1
            print('Vectores Propio #',contador2,'\n',i)
        for i in range(len(vectores)):
            print("la probbailidad de pasar de:",estado," a ",vectores[i]," es ",self.transiciones(estado, vectores[i]),"%")




class cuantico:
    def __init__(self,ticks,matriz=[],estado=[]):
        self.size = 0
        self.estado = estado
        self.matriz = matriz
        self.ticks = ticks
        self.operacion2(ticks,matriz)
        self.valorpropio(matriz)


    def operacion2(self,ticks, matriz):
        for i in range(ticks):
            self.estado = np.dot(matriz, self.estado)
        return self.estado


    def probabilidad(self,estado):
        probalidad = []
        for i in estado:
            a = i.real
            b = i.imag
            operacion = (math.sqrt(a**2 + b**2))**2
            probalidad.append(operacion)
        return probalidad

    def itsNormalized(self,estado):
        if math.ceil(LA.norm(estado)) == 1:
            return True
        else:
            return False

    def normalizer(self,estado):
        auxiliar = []
        if not self.itsNormalized(estado):
            for i in (estado):
                auxiliar.append(i/LA.norm(estado))
            self.estado = auxiliar
        else:
            self.estado = estado

    def valorpropio(self,matriz):
        w = LA.eig(matriz) # La w representara los valores propios mientras que v seran los vectores propios
        return w

    def __str__(self):
        return str(self.estado)

class probabilisticos:
    def __init__(self,ticks,matriz = [], estado = []):
        self.ticks = ticks
        self.matriz = matriz
        self.estado = estado
        self.operacion(ticks,matriz)

    def operacion(self, ticks, matriz):
        for i in range(ticks):
            self.estado = np.dot(matriz, self.estado)

    def __str__(self):
        return str(self.estado)


class deterministico:
    def __init__(self,ticks,boolmatrix = [], estado = []):
        self.matrix = boolmatrix
        self.ticks = ticks
        self.estado = estado
        self.operacion(ticks,boolmatrix)

    def operacion(self,ticks,boolmatrix):
        for i in range(ticks):
            self.estado = np.dot(boolmatrix,self.estado)    #es importante que se tome el orden en cuenta puesto que este puede cambiar el resultado

    def __str__(self):
        return str({
            'estado':self.estado,
            'Ticks usados':self.ticks,
            'Matriz booleana': np.array(self.matrix),
        })



if __name__ == '__main__':
    #deterministico
    booleanmatriz = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
    estado =np.transpose([3,2,5,9,0,7])
    ticks = stdin.readline().strip()
    ticks = int(ticks)
    canicas = deterministico(ticks,booleanmatriz,estado)
    print(canicas)

    #probabilistico
    rendija = [[0,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[0,1/3,0,0,1,0,0,0,0,0,0],[0,1/3,0,0,0,1,0,0,0,0,0],[0,1/3,1/3,0,0,0,1,0,0,0,0],[0,0,1/3,0,0,0,0,1,0,0,0],[0,0,1/3,1/3,0,0,0,0,1,0,0],[0,0,0,1/3,0,0,0,0,0,1,0],[0,0,0,1/3,0,0,0,0,0,0,1]]
    estado1 = np.transpose([1,0,0,0,0,0,0,0,0,0,0])
    ticks = stdin.readline().strip()
    ticks = int(ticks)
    rendijas = probabilisticos(ticks,rendija,estado1) #Esta es con 3 rendijas
    print('ESTADO = \n',rendijas)

    #cuantica
    rendija1 = [[0,0,0,0,0,0,0,0],[1/math.sqrt(2),0,0,0,0,0,0,0],[1/math.sqrt(2),0,0,0,0,0,0,0], [0,-1/math.sqrt(6)+1j/math.sqrt(6),0,1,0,0,0,0],[0,-1/math.sqrt(6)-1j/math.sqrt(6),0,0,1,0,0,0],[0,1/math.sqrt(6)-1j/math.sqrt(6),-1/math.sqrt(6)+1j/math.sqrt(6),0,0,1,0,0],[0,0,-1/math.sqrt(6)-1j/math.sqrt(6),0,0,0,1,0],[0,0,1/math.sqrt(6)-1j/math.sqrt(6),0,0,0,0,1]]
    estado2 = np.transpose([1,0,0,0,0,0,0,0])
    ticks = int(stdin.readline().strip())
    rendicuantica = cuantico(ticks,rendija1,estado2)
    print("Estado Final:\n",rendicuantica)
    estadocuanti = rendicuantica.operacion2(ticks,rendija1)
    probabilidad = rendicuantica.probabilidad(estadocuanti)
    print("PROBABILIDAD:\n",probabilidad)
    #HACER UN PRINT DE UN DIAGRAMA DE BARRAS
    eje_x = []
    for i in range (len(probabilidad)):
        eje_x.append(i)
    eje_y = []
    for i in probabilidad:
        eje_y.append(i*100)
    plt.bar(eje_x,eje_y)
    plt.ylabel("Probabilidad (%)")
    plt.xlabel('posiciones')
    plt.title("Probabilidades de estado")
    plt.savefig("Barras Probabilisticas.jpg")

    """------------------SEGUNDA LIBRERIA-------------------------"""

    # implementaciones
    print()
    psi2 = [1,0]
    vec = [1, 1]
    vec2 = [-1,1]
    probabilidad1 = observables(psi2, vec)
    proba = probabilidad1.transiciones(psi2,vec)
    print("Probabilidad de paso de",psi2,'a',vec,'\n',proba,'%')

    particu = stdin.readline().strip()
    particu = int(particu)
    enlinea = observables(psi2,vec)
    particulas = enlinea.particulaLinea(particu, vec, vec2)
    print("Cantidad de particulas:\n",particulas)

    # Valor esperado y mas funciones se encontraran en los ejemplos hechos


    # Ejemplos
    print()
    #4.3.1:
    observable = [[1/2,0],[0,1/2]]
    print('matriz',observable,'Con valores y vectores propios:\n')
    psi = [1,0]
    obser = observables(observable, psi)
    grafica = obser.graficador(observable,psi)
    valorEsperado = obser.valorEsperado(observable,psi)
    print("El valor esperado de la matriz es:\n",valorEsperado)


    print()
    # 4.4.2:
    unitari = [[0,1/math.sqrt(2),1/math.sqrt(2),0],[1j/math.sqrt(2),0,0,1/math.sqrt(2)],[1/math.sqrt(2),0,0,1j/math.sqrt(2)],[0,1/math.sqrt(2),-1/math.sqrt(2),0]]
    ini_state = np.transpose([1,0,0,0])
    steps = stdin.readline().strip() # para fines de el ejercicio este sera 3
    steps = int(steps)
    dynamics = cuantico(steps, unitari, ini_state)
    print("Estado Final:\n", dynamics)
    print()