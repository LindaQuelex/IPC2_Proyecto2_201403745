class NodoArchivo():
    def __init__(self, nombrearchivo):
        self.nombrearchivo= nombrearchivo
        self.siguiente=None
        self.anterior=None
        self.id=0

    def getnombrearchivo(self):
        return self.nombrearchivo 

    def setnombrearchivo(self, nombrearchivo):
        self.archivo= nombrearchivo

    def getid(self):
        return self.id

    def setid(self, id):
        self.id =id

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevoarchivo):
        self.siguiente = nuevoarchivo

    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevoarchivo):
        self.anterior = nuevoarchivo