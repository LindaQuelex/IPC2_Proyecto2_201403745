from email.mime import image
import os
import webbrowser
from ListaCabecera import ListaCabecera
from NodoCabecera import NodoCabecera
from NodoCeldaMalla  import NodoCeldaUnitariaMalla


class MatrizDispersa():
    def __init__(self):
        self.filas=ListaCabecera('Fila')
        self.columnas=ListaCabecera('Columna')
        self.id=0

    def insertar(self,x,y,clasificacionceldaunitaria, estado,valoracion,cant_instransitable, cant_entradas,cant_caminos, cant_recuros,cant_civil):
        nuevaceldamalla=NodoCeldaUnitariaMalla(x,y,clasificacionceldaunitaria, estado, valoracion,cant_instransitable, cant_entradas,cant_caminos, cant_recuros,cant_civil)
        nodox=self.filas.getCabecera(x)
        nodoy=self.columnas.getCabecera(y)
        self.id+=1
        if nodox==None:
            nodox=NodoCabecera(x)
            self.filas.insertarnodocabecera(nodox)
        if nodoy==None:
            nodoy=NodoCabecera(y)
            self.columnas.insertarnodocabecera(nodoy)
        
        if nodox.acceso ==None:
            nodox.acceso=nuevaceldamalla

        else:
            if int(nuevaceldamalla.coordenadaY) < int(nodox.acceso.coordenadaY):
                nuevaceldamalla.right=nodox.acceso
                nodox.acceso.left=nuevaceldamalla
                nodox.acceso=nuevaceldamalla

            else: 
                tmp=nodox.acceso
                while tmp !=None:
                    if int(nuevaceldamalla.coordenadaY)<int( tmp.coordenadaY):
                        nuevaceldamalla.right=tmp
                        nuevaceldamalla.left=tmp.left
                        tmp.left.right=nuevaceldamalla
                        tmp.left=nuevaceldamalla
                        break

                    elif int(nuevaceldamalla.coordenadaX)==int(tmp.coordenadaX) and int(nuevaceldamalla.coordenadaY) == int(tmp.coordenadaY):
                        print('Ya existe un nodo en esta posición de fila', nuevaceldamalla.coordenadaX, nuevaceldamalla.coordenadaY)
                        break;   
                         
                         #aquí se debe actualizar el dato                
                    else: 
                        if tmp.right==None:
                            tmp.right=nuevaceldamalla
                            nuevaceldamalla.left=tmp
                            break
                        else: 
                            tmp=tmp.right

        if nodoy.acceso==None:
            nodoy.acceso=nuevaceldamalla
        else: 
            if int(nuevaceldamalla.coordenadaY) < int(nodox.acceso.coordenadaY): #esta es la línea que aparece en el repositorio
            #if nuevaceldamalla.coordenadaX==nodoy.acceso.coordenadaX: #esta línea es diferente al repositorio
                nuevaceldamalla.down=nodoy.acceso
                nodoy.acceso.up= nuevaceldamalla
                nodoy.acceso=nuevaceldamalla
            else: 
                tmp2:NodoCabecera=nodoy.acceso
                while tmp2 != None:
                    if int(nuevaceldamalla.coordenadaX)<int(tmp2.coordenadaX):
                        nuevaceldamalla.down=tmp2
                        nuevaceldamalla.up=tmp2.up
                        tmp2.up.down =nuevaceldamalla
                        tmp2.up=nuevaceldamalla
                        break
                    elif int(nuevaceldamalla.coordenadaX) == int(tmp2.coordenadaX) and int(nuevaceldamalla.coordenadaY)==int(tmp2.coordenadaY):
                        print('Ya existe una celda de la malla en esta posición de columna',nuevaceldamalla.coordenadaX, nuevaceldamalla.coordenadaY)
                        break
                    else: 
                        if tmp2.down ==None:
                            tmp2.down=nuevaceldamalla
                            nuevaceldamalla.up =tmp2
                            break
                        else:
                            tmp2=tmp2.down

        nuevaceldamalla.ListaMilitares.insertar_militar                   
        return nuevaceldamalla
        

    def graficarNeato(self, nombre):
        contenido = '''digraph G{
    node[shape=circle, width=0.7, height=0.7, color="white" fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "Ciudad''' +'''" fillcolor="cornsilk" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial" \nfontsize="16pt" \n
                    \n'''.format('\nCeldas de Malla ChapinEyes'+ '\n'+'\nSimbología de colores'+ '\nNegro: Intransitable'+ '\nVerde: Punto de entrada'+ '\nBlanco: Camino'+ '\nRojo: Unidad Militar'+ '\nAzul: Unidad Civil'+ '\nGris: Recurso')
                    

        # --graficar nodos ENCABEZADO
        # --graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" color="white" fillcolor="white" pos="-1,-{}!" nodesep=0.02  ranksep=0.02 shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente!= None:
            contenido += '\n\tx{}->x{} [color="cornsilk" nodesep=0.02  ranksep=0.02];'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=black color="cornsilk" nodesep=0.02  ranksep=0.02];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{}[color="cornsilk"];'.format(self.filas.primero.id)

        # --graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" color="white" fillcolor="white" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{} [color="cornsilk"];'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back color ="cornsilk"];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{}[color="cornsilk"];'.format(self.columnas.primero.id)

        #ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda :NodoCeldaUnitariaMalla= pivote.acceso
            while pivote_celda != None:
                # --- buscamos posy
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.clasificacioncelda == '*':
                    contenido += '\n\tnode[label=" " color="white" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.clasificacioncelda == ' ':
                    contenido += '\n\tnode[label=" " color="white" fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.clasificacioncelda == 'E':
                    contenido += '\n\tnode[label=" " color="white" fillcolor="yellowgreen" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.clasificacioncelda == 'C':
                    contenido += '\n\tnode[label=" " color="white" fillcolor="skyblue1" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.clasificacioncelda == 'R':
                    contenido += '\n\tnode[label=" " color="white" fillcolor="azure3" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.clasificacioncelda == 'M':
                    contenido += '\n\tnode[label=" " color="white" fillcolor="indianred" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                else:
                    contenido += '\n\tnode[label=" " color="white" fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                pivote_celda = pivote_celda.right
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.right != None:
                    contenido += '\n\ti{}_{}i{}_{}[color= "white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.right.coordenadaX, pivote_celda.right.coordenadaY)
                    contenido += '\n\ti{}_{}i{}_{}[dir=back color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.right.coordenadaX, pivote_celda.right.coordenadaY)
                pivote_celda = pivote_celda.right
            contenido += '\n\tx{}i{}_{}[color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}i{}_{}[dir=back color= "white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : NodoCeldaUnitariaMalla = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.down != None:
                    contenido += '\n\ti{}_{}i{}_{}[color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.down.coordenadaX, pivote_celda.down.coordenadaY)
                    contenido += '\n\ti{}_{}i{}_{}[dir=back color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.down.coordenadaX, pivote_celda.down.coordenadaY) 
                pivote_celda = pivote_celda.down
            contenido += '\n\ty{}i{}_{}[color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}i{}_{}[dir=back color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
        contenido += '\n}'
        #--- se genera DOT y se procede a ecjetuar el comando
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)

    def ubicarcoordenada(self,fila,columna):
        try: 
            tmp:NodoCeldaUnitariaMalla=self.filas.getCabecera(fila).getAcceso()
            while tmp!=None:
                if tmp.coordenadaX== fila and tmp.coordenadaY == columna:
                    print('hola mundo')
                    print(tmp.clasificacioncelda)
                    return tmp
                tmp=tmp.getright()
            return None
        except: 
            print('No existe')
            return None

    def actualizarMilitar(self,fila,columna, valoraciónmilitar):
        try: 
            tmp:NodoCeldaUnitariaMalla=self.filas.getCabecera(fila).getAcceso()
            while tmp!=None:
                if tmp.coordenadaX== fila and tmp.coordenadaY == columna:
                    tmp.clasificacioncelda="M"
                    tmp.valoracion=valoraciónmilitar
                    print(tmp.clasificacioncelda)
                    return tmp
                    
                tmp=tmp.getright()
            return None
        except: 
            print('No existe')
            return None


         
    

        

            
        # pivote_celda.ListaMilitares.mostrar_militares()
        # return pivote_celda

# matriz= MatrizDispersa()
# matriz.insertar(1,5,'R',4,1,None,None, None,None,100)
# matriz.insertar(1,4,'C',4,2,None,None, None,None,None)
# matriz.insertar(2,8,'E',4,2,None,None, None,None,None)
# matriz.insertar(1,1,'*','*','*',None,None, None,None,None)
# matriz.insertar(7,11,' ','*','*',None,None, None,None,None)
# matriz.insertar(10,12,'*','*','*',None,None, None,None,None)
# matriz.insertar(15,12,'*','*','*',None,None, None,None,None)
# matriz.insertar(7,1,'M','*','*',None,None, None,None,None)




# matriz.graficarNeato('prueba')
# matriz.actualizarMilitar(10,12,100)
# matriz.actualizarMilitar(1,5,100)
# matriz.graficarNeato('Malla_Celdas_ChapinEyes')


