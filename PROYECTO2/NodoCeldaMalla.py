
from ListaMilitares import ListaMilitares

class NodoCeldaUnitariaMalla():
    def __init__(self,x,y,clasificacionceldaunitaria, estado,valoracion, cant_instransitable, cant_entradas,cant_caminos, cant_recuros,cant_civil):
        self.coordenadaX=x
        self.coordenadaY=y
        self.clasificacioncelda=clasificacionceldaunitaria
        self.estado=estado  #transitable e intransitable
        self.valoracion=valoracion
        self.cant_instransitable= cant_instransitable
        self.cant_entradas=cant_entradas
        self.cant_caminos= cant_caminos
        self.cant_recursos=cant_recuros
        self.cant_civil=cant_civil
        self.siguiente=None
        self.anterior=None
        self.up=None
        self.down=None
        self.right=None
        self.left=None
        self.size=0
        self.ListaMilitares =ListaMilitares()



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

    def getright(self):
        return self.right

    def setright(self, nuevacelda):
        self.right = nuevacelda

    

    def getcantciviles(self):
        return self.cant_civil

    def setcantciviles(self, nuevacelda):
        self.cant_civl = nuevacelda
