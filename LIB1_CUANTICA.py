import numpy as np
import math
from sys import stdin

class cuantico:
    def __init__(self,ticks,matriz=[],estado=[]):
        self.matriz = matriz
        self.estado = estado
        self.ticks = ticks
        self.operacion2(ticks,matriz)

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
    print(rendicuantica)
    estadocuanti = rendicuantica.operacion2(ticks,rendija1)
    probabilidad = rendicuantica.probabilidad(estadocuanti)
    print(probabilidad)

    #HACER UN PRINT DE UN DIAGRAMA DE BARRAS
