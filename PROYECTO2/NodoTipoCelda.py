class NodoTipoCelda():
    def __init__(self, tipocelda):
        self.tipocelda=tipocelda
        self.siguiente=None
        self.anterior=None
        self.id=0

    def gettipocelda(self):
        return self.tipocelda

    def settipocelda(self, tipocelda):
        self.tipocelda= tipocelda

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