class NodoCantidadCelda():
    def __init__(self, cantidadcelda):
        self.cantidadcelda=cantidadcelda
        self.siguiente=None
        self.anterior=None
        self.id=0

    def getcantidadelda(self):
        return self.cantidadcelda

    def settipocelda(self, cantidadacelda):
        self.cantidadcelda= cantidadacelda
        
    def getid(self):
        return self.id

    def setid(self, id):
        self.id =id

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevacelda):
        self.siguiente = nuevacelda

    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevacelda):
        self.anterior = nuevacelda