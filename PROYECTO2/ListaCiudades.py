
from NodoCiudad import NodoCiudad


class ListaCiudades():
    def __init__(self):
        self.size=0
        self.primero:NodoCiudad=None
        self.ultimo =None


    def insertar(self, nuevo :NodoCiudad):
        self.size+=1
        if self.primero==None:
            self.primero =nuevo
            self.ultimo=nuevo
        else:
            if nuevo.id < self.primero.id:
               nuevo.siguiente=self.primero
               self.primero.anterior=nuevo
               self.primero =nuevo
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente =nuevo
                nuevo.anterior =self.ultimo
                self.ultimo =nuevo
            else:
                tmp : NodoCiudad =self.primero
                while tmp != None:
                    if nuevo.id < tmp.id:
                        nuevo.siguiente =tmp
                        nuevo.anterior =tmp.anterior
                        tmp.anterior.siguiente= nuevo
                        tmp.anterior=nuevo
                        break
                    elif nuevo.id >tmp.id:
                        tmp = tmp.siguiente
                    else:
                        break 
         
    def mostrar_pisos(self):
        tmp=self.primero
        for i in range(self.size):
            print('El número correlativo del piso es:','(',i,')','\n','El nombre de la ciudad es:', tmp.nombreciudad)
            tmp.MatrizDispersa.graficarNeato()
            tmp = tmp.siguiente




Ciudad = ListaCiudades()
Ciudad.insertar('Amsterdam')
Ciudad.insertar('Tokyo')
Ciudad.insertar('Guatemala')
Ciudad.insertar('México')
Ciudad.mostrar_pisos()


