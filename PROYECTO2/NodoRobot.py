class NodoRobot():
    def __init__(self,x,y,nombrerobot, tipodemision, valoracion):
        self.coordenadaX=x
        self.coordenadaY=y
        self.nombrerobot= nombrerobot
        self.tipodemision=tipodemision
        self.valoracion=valoracion
        self.siguiente=None
        self.anterior=None
        self.size=0
        self.up=None
        self.down=None
        self.right= None
        self.left=None
        self.id=None
        


    def getid(self):
        return self.id

    def setid(self, id):
        self.id =id

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevorobot):
        self.siguiente = nuevorobot

    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevorobot):
        self.anterior = nuevorobot

