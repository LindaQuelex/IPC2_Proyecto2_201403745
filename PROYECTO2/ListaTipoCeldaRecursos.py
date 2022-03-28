
from NodoTipoCeldaRecursos import NodoCantidadCeldaRecursos

class ListaTipoCeldaRecursos():
    def __init__(self):
        self.size=0
        self.primero:NodoCantidadCeldaRecursos=None
        self.ultimo =None
  
    
    def insertar_tipo_celda_recursos(self, tipocelda ):
        nuevotipocelda=NodoCantidadCeldaRecursos(tipocelda)
        nuevotipocelda.setid(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevotipocelda
            self.ultimo=nuevotipocelda
        else:
           self.ultimo.setsiguiente(nuevotipocelda)
           self.ultimo=nuevotipocelda  
        return nuevotipocelda

    def mostrar_tipo_celda(self):
        tmp=self.primero
        for i in range(self.size):
            print(tmp.cantidadcelda)
            #tmp.MatrizDispersa.graficarNeato
            tmp = tmp.getsiguiente()
            
    def mostraratipocelda(self):
        tmp=self.primero 
        self.size+=1
        while tmp != None:
            print("temporal",tmp.id, tmp.cantidadcelda)
            tmp=tmp.siguiente
    
    def retornar_nodo_tipocelda(self, id):
        aux=self.primero
        while aux.getid()< id:
            aux=aux.getsiguiente()
        return aux   
    
