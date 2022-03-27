
from NodoTipoCelda import NodoTipoCelda

class ListaTipoCelda():
    def __init__(self):
        self.size=0
        self.primero:NodoTipoCelda=None
        self.ultimo =None

    def insertar_tipo_celda(self, tipocelda ):
        nuevotipocelda=NodoTipoCelda(tipocelda)
        nuevotipocelda.setid(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevotipocelda
            self.ultimo=nuevotipocelda
        else:
           self.ultimo.setsiguiente(nuevotipocelda)
           self.ultimo=nuevotipocelda  
        # nuevotipocelda.MatrizDispersa.insertar
        return nuevotipocelda

    def mostrar_tipo_celda(self):
        tmp=self.primero
        for i in range(self.size):
            print(i, tmp.tipocelda)
            #tmp.MatrizDispersa.graficarNeato
            tmp = tmp.getsiguiente()
            
    def mostraratipocelda(self):
        tmp=self.primero 
        self.size+=1
        while tmp != None:
            print("temporal",tmp.id, tmp.tipocelda)
            tmp=tmp.siguiente
    
    def retornar_nodo_tipocelda(self, id):
        aux=self.primero
        while aux.getid()< id:
            aux=aux.getsiguiente()
        return aux   
    
