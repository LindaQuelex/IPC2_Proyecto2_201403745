

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
            print(i, tmp.nombreciudad,tmp.row, tmp.column)
            tmp.MatrizDispersa.graficarNeato
            tmp = tmp.getsiguiente()
            
    def mostrar(self):
        tmp=self.primero 
        self.size+=1
        while tmp != None:
            print("temporal",tmp.id, tmp.nombreciudad,tmp.row, tmp.column)
            tmp=tmp.siguiente
    
    def retornar_nodo(self, id):
        aux=self.primero
        while aux.getid()< id:
            aux=aux.getsiguiente()
        return aux   
    
    # def insertar2(self,nuevaciudad:NodoCiudad):
    #     self.size+=1
    #     nuevaciudad.setid(self.size)
    #     if self.primero ==None:
    #         self.primero=nuevaciudad
    #         self.ultimo=nuevaciudad
    #     else: 
    #         if nuevaciudad.nombreciudad == self.primero.nombreciudad:
    #             nuevaciudad.siguiente=
    #             self.primero.siguiente= self.primero.siguiente
    #             self.primero=nuevaciudad
    #             self.primero.id=nuevaciudad.id
    #             #print(nuevaciudad.id,nuevaciudad.nombreciudad, nuevaciudad.row, nuevaciudad.column)  
    #         elif nuevaciudad.nombreciudad==self.ultimo.nombreciudad:
    #             #print('hola',nuevaciudad.id,nuevaciudad.nombreciudad, nuevaciudad.row, nuevaciudad.column)
    #             self.ultimo= nuevaciudad
                
    #             #print(self.size,'hola',nuevaciudad.id,nuevaciudad.nombreciudad, nuevaciudad.row, nuevaciudad.column)
    #         else: 
    #             self.ultimo.siguiente=nuevaciudad
    #             nuevaciudad.anterior=self.ultimo
    #             self.ultimo=nuevaciudad
    #             #print(nuevaciudad.id, nuevaciudad.nombreciudad, nuevaciudad.row, nuevaciudad.column)
    #         # elif nuevaciudad.nombreciudad!=self.primero.nombreciudad:
    #         #     tmp : NodoCiudad=self.primero
    #         #     while tmp !=None:
    #         #         if nuevaciudad.nombreciudad!= tmp.nombreciudad:
    #         #             nuevaciudad.siguiente=tmp
    #         #             nuevaciudad.anterior =tmp.anterior
    #         #             tmp.anterior.siguiente=nuevaciudad
    #         #             tmp.anterior=nuevaciudad
    #         #             break
    #         #         if nuevaciudad.nombreciudad== tmp.nombreciudad:
    #         #             tmp=nuevaciudad
            
    #             #print('prueba',nuevaciudad.id, nuevaciudad.nombreciudad,nuevaciudad.row, nuevaciudad.column)


 





# nodo=ListaCiudades()
# n1=NodoCiudad('ga',1,20)
# n2=NodoCiudad('s',5,10)
# n3=NodoCiudad('gt',100,10)
# n4=NodoCiudad('ga',1,10)
# nodo.insertar2(n1)
# nodo.insertar2(n2)
# nodo.insertar2(n3)
# nodo.insertar2(n4)


# ciudad=ListaCiudades()
# ciudad.insertar2("Seul",2,1)
# ciudad.insertar2("Seul",3,1)

#nodo.mostrar_ciudades()

# ciudad= ListaCiudades()
# ciudad.insertar('uno','2',3)
# ciudad.insertar('dos','2',3)
# ciudad.insertar('tres','2',3)
# ciudad.insertar('cuatro','2',3)
# # ciudad.mostrar_ciudades() 
# ciudad.mostrar()
# ciudad.retornar_nodo(1)
# print(ciudad.retornar_nodo(0))



