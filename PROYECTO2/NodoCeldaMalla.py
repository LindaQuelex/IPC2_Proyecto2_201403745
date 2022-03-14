class NodoCeldaUnitariaMalla():
    def __init__(self,x,y,clasificacionceldaunitaria, estado,valoracion):
        self.coordenadaX=x
        self.coordenadaY=y
        self.clasificacioncelda=clasificacionceldaunitaria
        self.estado=estado  #transitable e intransitable
        self.valoracion=valoracion
        self.siguiente=None
        self.anterior=None
        self.up=None
        self.down=None
        self.right=None
        self.left=None
        self.size=0