from NodoMilitares import NodoMilitares

class ListaMilitares():
    def __init__(self):
        self.size=0
        self.primero:NodoMilitares=None
        self.ultimo =None

    def insertar_militar(self, pos_x, pos_y, valoración):
        nuevaunidadmilitar=NodoMilitares(pos_x, pos_y, valoración)
        nuevaunidadmilitar.setid(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevaunidadmilitar
            self.ultimo=nuevaunidadmilitar
        else:
           self.ultimo.setsiguiente(nuevaunidadmilitar)
           self.ultimo=nuevaunidadmilitar  
        #nuevaunidadmilitar.MatrizDispersa.insertar
        return nuevaunidadmilitar

    def mostrar_militares(self):
        tmp=self.primero
        for i in range(self.size):
            print(i,'Los valores de las unidades militares son:', tmp.valoracion)
            #tmp.MatrizDispersa.graficarNeato
            tmp = tmp.getsiguiente()
            
    def mostrar(self):
        tmp=self.primero 
        self.size+=1
        while tmp != None:
            print("temporal",tmp.id, tmp.valoracion)
            tmp=tmp.siguiente
    
    def retornar_nodo(self, id):
        aux=self.primero
        while aux.getid()< id:
            aux=aux.getsiguiente()
        return aux   
    

