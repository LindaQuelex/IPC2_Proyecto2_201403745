from ListaCabecera import ListaCabecera
from NodoCabecera import NodoCabecera
from NodoCeldaMalla  import NodoCeldaUnitariaMalla

class MatrizDispersa():
    def __init__(self):
        self.filas=ListaCabecera()
        self.columnas=ListaCabecera()

    def insertar(self,x,y,clasificacionceldaunitaria, estado,valoracion):
        nuevaceldamalla=NodoCeldaUnitariaMalla(x,y,clasificacionceldaunitaria, estado,valoracion)
        nodox=self.filas.getCabecera(x)
        nodoy=self.columnas.getCabecera(y)
        if nodox==None:
            nodox=NodoCabecera(x)
            self.filas.insertarnodocabecera(nodox)
        if nodoy==None:
            nodoy=NodoCabecera(y)
            self.columnas.insertarnodocabecera(nodoy)
        
        if nodox.acceso ==None:
            nodox.acceso=nuevaceldamalla

        else:
            if nuevaceldamalla.coordenadaY < nodox.acceso.coordenadaY:
                nuevaceldamalla.right=nodox.acceso
                nodox.acceso.left=nuevaceldamalla
                nodox.acceso=nuevaceldamalla

            else: 
                tmp=nodox.acceso
                while tmp !=None:
                    if nuevaceldamalla.coordenadaY< tmp.coordenadaY:
                        nuevaceldamalla.right=tmp
                        nuevaceldamalla.left=tmp.left
                        tmp.left=nuevaceldamalla
                        break;

                    elif nuevaceldamalla.coordenadaX==tmp.coordenadaX and nuevaceldamalla.coordenadaY == tmp.coordenadaX:
                         break;   
                         #aquí se debe actualizar el dato                
                    else: 
                        if tmp.right==None:
                            tmp.right=nuevaceldamalla
                            nuevaceldamalla.left=tmp
                            break;
                        else: 
                            tmp=tmp.right

        if nodoy.acceso==None:
            nodoy.acceso=nuevaceldamalla



