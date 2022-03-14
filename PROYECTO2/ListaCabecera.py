from NodoCabecera import NodoCabecera

class ListaCabecera():
    def __init__(self, tipo):
        self.primero=None
        self.ultimo=None
        self.tipo=tipo
        self.size=0

    def insertarnodocabecera(self,nuevo:NodoCabecera):
        self.size+=1
        if self.primero ==None:
            self.primero=nuevo
            self.ultimo=nuevo
        else: 
            if nuevo.id  < self.primero.id:
                nuevo.siguiente=self.primero
                self.primero.anterior=nuevo
                self.primero=nuevo
            elif nuevo.id> self.ultimo.id:
                self.ultimo.siguiente=nuevo
                nuevo.anterior=self.ultimo
                self.ultimo=nuevo
            else:
                tmp :NodoCabecera=self.primero
                while tmp != None:
                    if nuevo.id<tmp.id:
                        nuevo.siguiente=tmp
                        nuevo.anterior =tmp.anterior
                        tmp.anterior.siguiente=nuevo
                        tmp.anterior=nuevo
                        break
                    elif nuevo.id > tmp.id:
                        tmp=tmp.siguiente
                    else:
                        break

    def mostrarCabecera(self):
        tmp=self.primero
        while tmp !=None:
            print('Cabecera',self.tipo,tmp.id)
            tmp=tmp.siguiente

    
    def getCabecera(self, id):
        tmp=self.primero
        while tmp!= None:
            if id==tmp.id:
                return tmp
            tmp.siguiente
        return None

    

# cabecera= ListaCabecera('fila')
# n1=NodoCabecera(3)
# n2=NodoCabecera(9)
# n3=NodoCabecera(4)
# cabecera.insertarnodocabecera(n1)
# cabecera.insertarnodocabecera(n2)
# cabecera.insertarnodocabecera(n3)
# cabecera.mostrarCabecera()


                


