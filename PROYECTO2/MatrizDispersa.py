import os
import webbrowser
from ListaCabecera import ListaCabecera
from NodoCabecera import NodoCabecera
from NodoCeldaMalla  import NodoCeldaUnitariaMalla
from ListaMilitares import ListaMilitares


class MatrizDispersa():
    def __init__(self):
        self.filas=ListaCabecera('Fila')
        self.columnas=ListaCabecera('Columna')

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
                        tmp.left.right=nuevaceldamalla
                        tmp.left=nuevaceldamalla
                        break

                    elif nuevaceldamalla.coordenadaX==tmp.coordenadaX and nuevaceldamalla.coordenadaY == tmp.coordenadaY:
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
            if nuevaceldamalla.coordenadaY < nodox.acceso.coordenadaY: #esta es la línea que aparece en el repositorio
            #if nuevaceldamalla.coordenadaX==nodoy.acceso.coordenadaX: #esta línea es diferente al repositorio
                nuevaceldamalla.down=nodoy.acceso
                nodoy.acceso.up= nuevaceldamalla
                nodoy.acceso=nuevaceldamalla
            else: 
                tmp2:NodoCabecera=nodoy.acceso
                while tmp2 != None:
                    if nuevaceldamalla.coordenadaX<tmp2.coordenadaX:
                        nuevaceldamalla.down=tmp2
                        nuevaceldamalla.up=tmp2.up
                        tmp2.up.down =nuevaceldamalla
                        tmp2.up=nuevaceldamalla
                        break;
                    elif nuevaceldamalla.coordenadaX == tmp2.coordenadaX and nuevaceldamalla.coordenadaY==tmp2.coordenadaY:
                        print('Ya existe una celda de la malla en esta posición de columna',nuevaceldamalla.coordenadaX, nuevaceldamalla.coordenadaY)
                        break
                    else: 
                        if tmp2.down ==None:
                            tmp2.down=nuevaceldamalla
                            nuevaceldamalla.up =tmp2
                            break
                        else:
                            tmp2=tmp2.down

    def graficarNeato(self, nombre):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, color="white" fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "Ciudad''' +'''" fillcolor="cornsilk" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" \nfontsize="16pt" \n
                    \n'''.format('\nCeldas de Malla ChapinEyes')

        # --graficar nodos ENCABEZADO
        # --graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" color="white" fillcolor="cornsilk" pos="-1,-{}!" shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{} [color="white"];'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=black color="white"];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.id)

        # --graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" color="white" fillcolor="cornsilk" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{} [color="white"];'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back color ="white"];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)

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
                else:
                    contenido += '\n\tnode[label=" " color="white" fillcolor="indianred" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                pivote_celda = pivote_celda.right
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.right != None:
                    contenido += '\n\ti{}_{}->i{}_{}[color= "white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.right.coordenadaX, pivote_celda.right.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.right.coordenadaX, pivote_celda.right.coordenadaY)
                pivote_celda = pivote_celda.right
            contenido += '\n\tx{}->i{}_{}[color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=back color= "white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : NodoCeldaUnitariaMalla = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.down != None:
                    contenido += '\n\ti{}_{}->i{}_{}[color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.down.coordenadaX, pivote_celda.down.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.down.coordenadaX, pivote_celda.down.coordenadaY) 
                pivote_celda = pivote_celda.down
            contenido += '\n\ty{}->i{}_{}[color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=back color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
        contenido += '\n}'
        #--- se genera DOT y se procede a ecjetuar el comando
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)



# matriz= MatrizDispersa()
# matriz.insertar(1,5,'R',4,1)
# matriz.insertar(1,4,'C',4,2)
# matriz.insertar(2,8,'E',4,2)
# matriz.insertar(1,10,'*','*','*')
# matriz.insertar(7,10,' ','*','*')
# matriz.insertar(10,10,'z','*','*')


# matriz.graficarNeato('Malla_Celdas_ChapinEyes')

