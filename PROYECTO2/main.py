import xml.etree.ElementTree as ET
from ListaCiudades import ListaCiudades
from ListaRobots import ListaRobots

listaCiudades= ListaCiudades()
listaRobots= ListaRobots()

print('\n','---------------------------------------------------', 'CHAPIN WARRIOS, S. A.','---------------------------------------------------')
print('MENÚ PRINCIPAL','\n','Archivos disponibles para procesar:','\n')
#debería mostrar los nombre de los archivos  
print('Ingrese el nombre del archivo principal  a procesar:','\n')
#capturar el nombre del archivo y obtener ruta relativa
print('¿Desea agregar otro archivo para actualizar la información del archivo principal?','\n')
#si el usuario elige dos entonces hay que crear el metodo de sobreescritura para actualizar la información del archivo principal
#cuando se actualice el archivo, enviar la ruta relativa como parámetro ruta al método de ElementTree


def elementTree(ruta):
    contador=0
    tree=ET.parse(ruta)
    raiz= tree.getroot()
    for listaciudadesorobots in raiz:
        if listaciudadesorobots.tag=="listaCiudades":
            contadordos=0
            for ciudad in listaciudadesorobots:
                contadortres=0
                for nombre in ciudad:
                    nombretag=nombre.tag
                    if nombre.tag=="nombre":
                        nombreciudad=nombre.text
                        filasciudad=(nombre.attrib['filas'])
                        columnasciudad=(nombre.attrib['columnas'])
                    if nombre.tag=="fila":
                        numfilamalla=nombre.attrib['numero']
                        celdasciudad=nombre.text
                        celdaunitaria=celdasciudad
                        contadorseis=0
                        for celda in celdaunitaria:
                            print(celda)
                            #insertar en matriz dispersa
                            contadorseis+=1
                    if nombre.tag =="unidadMilitar":
                        capacidadmilitar=nombre.text
                        filamilitar=nombre.attrib['fila']
                        columnamilitar=nombre.attrib['columna']
                    contadortres+=1
                contadordos+=1
                #insertar en listas y matrizdispersa
        if listaciudadesorobots.tag=="robots":
            contadorcuatro=0
            for robots in listaciudadesorobots:
                contadorcinco=0
                for robot in robots: 
                    nombrerobot=robot.text
                    tipodelrobot=robot.attrib['tipo']
                    if tipodelrobot=="ChapinFighter":
                        capacidadrobot=robot.attrib['capacidad']
                    else:
                        capacidadrobot=0
                    contadorcinco+=1
                contadorcuatro+=1
        contador+=1   

elementTree('./ENTRADAS/entrada01.xml')   

