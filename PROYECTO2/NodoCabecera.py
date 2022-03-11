


class NodoCabecera():
    def __init__(self,clasificacioncelda, estado,valoracion):
        self.clasificacioncelda=clasificacioncelda
        self.estado=estado  #transitable e intransitable
        self.valoracion=valoracion
        self.siguiente=None
        self.anterior=None
        self.up=None
        self.down=None
        self.right=None
        self.left=None
        self.size=0
      
