from ListaTipoCeldaRecursos import ListaTipoCeldaRecursos
from MatrizDispersa import MatrizDispersa
from ListaTipoCelda import ListaTipoCelda

class NodoCiudad():
    def __init__(self,nombreciudad, row, column):
        self.nombreciudad=nombreciudad
        self.row=row
        self.column=column
        self.siguiente=None
        self.anterior=None
        self.id=0
        self.MatrizDispersa=MatrizDispersa()
        self.ListaTipoCelda=ListaTipoCelda()
        self.ListaTipoCeldaRecursos=ListaTipoCeldaRecursos()
        

    def getid(self):
        return self.id

    def setid(self, id):
        self.id =id

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevaciudad):
        self.siguiente = nuevaciudad

    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevaciudad):
        self.anterior = nuevaciudad
