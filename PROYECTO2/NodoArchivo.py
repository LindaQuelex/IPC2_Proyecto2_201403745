class NodoArchivo():
    def __init__(self, archivo):
        self.nombrearchivo= archivo
        self.siguiente=None
        self.anterior=None
        self.id=0

    def getarchivo(self):
        return self.archivo 

    def setarchivo(self, archivo):
        self.archivo= archivo

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