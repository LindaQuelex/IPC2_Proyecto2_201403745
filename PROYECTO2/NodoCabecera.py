from ListaCiudades import ListaCiudades
from ListaRobots import ListaRobots

class NodoCabecera():
    def __init__(self,clasificacioncelda, estado, mision,valoracion):
        self.clasificacioncelda=clasificacioncelda
        self.estado=estado  #transitable e intransitable
        self.siguiente=None
        self.anterior=None
        self.size=0
        self.ListaCiudades= ListaCiudades()
        self.ListaRobots= ListaRobots()
