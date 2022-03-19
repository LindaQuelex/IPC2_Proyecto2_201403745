
from NodoCiudad import NodoCiudad

class ListaCiudades():
    def __init__(self):
        self.size=0
        self.primero:NodoCiudad=None
        self.ultimo =None

    def insertar(self, nombreciudad,row, column):
        nuevaciudad=NodoCiudad(nombreciudad, row, column)
        nuevaciudad.setid(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevaciudad
            self.ultimo=nuevaciudad
        else:
           self.ultimo.setsiguiente(nuevaciudad)
           self.ultimo=nuevaciudad  
        nuevaciudad.MatrizDispersa.insertar
        return nuevaciudad

    def mostrar_ciudades(self):
        tmp=self.primero
        for i in range(self.size):
            print(i,'Las ciudades disponibles son:', tmp.nombreciudad)
            tmp.MatrizDispersa.graficarNeato
            tmp = tmp.getsiguiente()
            
    def mostrar(self):
        tmp=self.primero 
        self.size+=1
        while tmp != None:
            print("temporal",tmp.id, tmp.nombreciudad)
            tmp=tmp.siguiente
    
    def retornar_nodo(self, id):
        aux=self.primero
        while aux.getid()< id:
            aux=aux.getsiguiente()
        return aux   
    



# ciudad= ListaCiudades()
# ciudad.insertar('uno','2',3)
# ciudad.insertar('dos','2',3)
# ciudad.insertar('tres','2',3)
# ciudad.insertar('cuatro','2',3)
# # ciudad.mostrar_ciudades() 
# ciudad.mostrar()
# ciudad.retornar_nodo(1)
# print(ciudad.retornar_nodo(0))



