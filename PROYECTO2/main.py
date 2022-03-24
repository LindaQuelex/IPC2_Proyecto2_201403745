import os
import xml.etree.ElementTree as ET
from ListaCiudades import ListaCiudades
from ListaMilitares import ListaMilitares
from ListaRobots import ListaRobots
from MatrizDispersa import MatrizDispersa
from ListaArchivos import ListaArchivos

listaRobotsRescue= ListaRobots()
listaRobotsFighter=ListaRobots()
crearlistaciudades=ListaCiudades()

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
                        crearlistaciudades.insertar(nombreciudad,filasciudad,columnasciudad)
                    if nombre.tag =="unidadMilitar":
                        capacidadmilitar=nombre.text
                        filamilitar=nombre.attrib['fila']
                        columnamilitar=nombre.attrib['columna']    
                    if nombre.tag=="fila":
                        numfilamalla=nombre.attrib['numero']
                        celdasciudad=nombre.text
                        celdaunitaria=celdasciudad
                        contadorseis=0
                        posicióny=0
                        for celda in celdaunitaria:
                            #print(celda)
                            #crearlistaciudades.retornar_nodo(contadordos). MatrizDispersa.insertar(numfilamalla,contadorseis,celda,'none', 'none').ListaMilitares.insertar_militar(filamilitar,columnamilitar, capacidadmilitar)
                            crearlistaciudades.retornar_nodo(contadordos).MatrizDispersa.insertar(numfilamalla,contadorseis,celda, 'none', 'none')
                            #insertar en matriz dispersa, actualizada con los datos de los militares 
                            contadorseis+=1
                            posicióny+=1                 
                        # print(capacidadmilitar)
                        # print(filamilitar)
                        # print(columnamilitar)
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
                        listaRobotsFighter.insertar_robot(0,0,nombrerobot,tipodelrobot,capacidadrobot)
                    elif tipodelrobot=="ChapinRescue":
                        capacidadrobot=0
                        listaRobotsRescue.insertar_robot(0,0,nombrerobot,tipodelrobot,capacidadrobot)
                    contadorcinco+=1
                contadorcuatro+=1
        contador+=1   


print('\n','---------------------------------------------------', 'CHAPIN WARRIOS, S. A.','---------------------------------------------------')
print('MENÚ PRINCIPAL','\n')
question=input('¿Desea iniciar proceso?'+'\n'+'Responda: si o no'+'\n')

if question=="si":
    filename=input('\n'+"Ingrese el nombre del archivo a procesar:"+'\n')
    relativepath='./ENTRADAS/'+filename
    elementTree(relativepath)   
    print('\n','Las ciudades disponibles son: ')
    crearlistaciudades.mostrar_ciudades()
    ciudadseleccionada=input('\n'+'Ingrese el número de la cuidad seleccionada'+'\n')
    tipomisión=input('\n'+'Ingrese el tipo de misión (seleccione 1 o 2)'+'\n'+'1. Misión de rescate'+'\n'+'2. Misión de extracción de recursos'+'\n')
    #print('\n'+'Los robots disponibles son los siguientes:'+'\n')

    if tipomisión=="1":
        #agregar la validación de si existen celdas unidades civile para completar la misión
        if listaRobotsRescue.size==0:
            print('No existe robot ChapinRescue para llevar a cabo la misión')
            print('¿Desea iniciar un nuevo proceso?')
        elif listaRobotsRescue.ultimo.getid()==0:
            print('El único robot ChapinRescue disponible es:')
            listaRobotsRescue.mostrar_robot()
            #generar gráfica
            crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_de_Rescate')
        elif listaRobotsRescue.ultimo.getid()>0:
            print('Los robots ChapinRescue disponibles son:')
            listaRobotsRescue.mostrar_robot()
            retornarrobot=input('\n'+'Ingrese el número de Robot seleecionado:'+'\n')
            print('\n','El robot que realizará la misión es:')
            listaRobotsRescue.retornar_nodo(int(retornarrobot))
            #generar gráfica
            crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_de_Rescate')
    elif tipomisión=="2":
        #agregar la validación de si existen unidades de recursos
        if listaRobotsFighter.size==0:
            print('No existe robot ChapinFighter para llevar a cabo la misión')
        elif listaRobotsFighter.ultimo.getid()==0:
            print('El único robot ChapinFighter disponible es:')
            listaRobotsFighter.mostrar_robot()
            #generar gráfica
            crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_Extracción_de_Recursos')
        elif listaRobotsFighter.ultimo.getid()>0:
            print('Los robots ChapinFighter disponibles son:')
            listaRobotsFighter.mostrar_robot()
            retornarrobot=input('\n'+'Ingrese el número de Robot seleecionado:'+'\n')
            print('\n','El robot que realizará la misión es:')
            listaRobotsFighter.retornar_nodo(int(retornarrobot))
            #generar gráfica
            crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_Extracción_de_Recursos')
            
else:
    salir=input('¿Desea salir de la aplicación' +'\n'+'Responda: si o no'+'\n')
    if salir=='si':
        exit()
    else: 
        print('¿Desea iniciar un nuevo proceso?')

#crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Malla_Celdas')

# try:
#     with open('./ENTRADAS/'+filename) as f_obj:
#         contents=f_obj.read()
# except FileNotFoundError:
#     msg="Parece que el archivo"+ filename+"no existe"
#     print(msg)
#     #filename=input("Intente de nuevo"+'\n'+"Ingrese el nombre del archivo"+'\n')