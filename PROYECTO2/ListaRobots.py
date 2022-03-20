
from NodoRobot import NodoRobot


class ListaRobots():
    def __init__(self):
        self.size=0
        self.primero:NodoRobot=None
        self.ultimo =None

    def insertar_robot(self, x,y,nombrerobot, tipodemision, valoracion):
        nuevorobot=NodoRobot(x,y,nombrerobot, tipodemision, valoracion)
        nuevorobot.setid(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevorobot
            self.ultimo=nuevorobot
        else:
           self.ultimo.setsiguiente(nuevorobot)
           self.ultimo=nuevorobot  
        #nuevorobot.MatrizDispersa.insertar
        return nuevorobot

    def mostrar_robot(self):
        tmp=self.primero
        for i in range(self.size):
            print(i,'.-', 'Nombre del robot:', tmp.nombrerobot,'--->Tipo de Robot:', tmp.tipodemision, '--->Capacidad:',tmp.valoracion)
            #tmp.MatrizDispersa.graficarNeato
            tmp = tmp.getsiguiente()

    def retornar_nodo(self, id):
        aux=self.primero
        while aux.getid()< id:
            aux=aux.getsiguiente()
        print(aux.nombrerobot,'--->',aux.tipodemision,'--->' ,'Capacidad:',aux.valoracion)
        return aux   

    def recorrer(self):
        if self.primero is None:
            print('la lista esta vacía')