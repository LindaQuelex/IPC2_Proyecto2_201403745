class NodoMilitares(): 
    def __init__(self, valoracion, pos_x, pos_y):
        self.valoracion=valoracion
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.siguiente= None
        self.anterior=None
        self.id=0

    def getvaloracion(self):
        return self.valoracion

    def setvaloracion(self, valoracion):
        self.valoracion =valoracion

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



        
        


