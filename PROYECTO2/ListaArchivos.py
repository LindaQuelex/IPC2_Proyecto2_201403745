from NodoArchivo import NodoArchivo

class ListaArchivos():
    def __init__(self):
        self.size=0
        self.primero:NodoArchivo=None
        self.ultimo =None

    def insertar(self, archivo ):
        nuevoarchivo=NodoArchivo(archivo)
        nuevoarchivo.setid(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevoarchivo
            self.ultimo=nuevoarchivo
        else:
           self.ultimo.setsiguiente(nuevoarchivo)
           self.ultimo=nuevoarchivo  
        # nuevoarchivo.MatrizDispersa.insertar
        return nuevoarchivo

    def mostrar_archivo(self):
        tmp=self.primero
        for i in range(self.size):
            print(i,'Los archivos cargados son:', tmp.nombrearchivo)
            #tmp.MatrizDispersa.graficarNeato
            tmp = tmp.getsiguiente()
            
    def mostrararchivo(self):
        tmp=self.primero 
        self.size+=1
        while tmp != None:
            print("temporal",tmp.id, tmp.nombrearchivo)
            tmp=tmp.siguiente
    
    def retornar_nodo_archivo(self, id):
        aux=self.primero
        while aux.getid()< id:
            aux=aux.getsiguiente()
        return aux   
    
