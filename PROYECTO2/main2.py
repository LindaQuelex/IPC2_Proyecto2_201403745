from ListaArchivos import ListaArchivos
from lecturaxml import LecturaXML
from ListaCiudades import ListaCiudades
import os
import xml.etree.ElementTree as ET
from ListaMilitares import ListaMilitares
from ListaRobots import ListaRobots
from MatrizDispersa import MatrizDispersa


crearlistaciudades=ListaCiudades()
listaarchivos=ListaArchivos()

listaRobotsRescue= ListaRobots()
listaRobotsFighter=ListaRobots()
crearlistaciudades=ListaCiudades()

print('\n','---------------------------------------------------', 'CHAPIN WARRIOS, S. A.','---------------------------------------------------')
print('MENÚ PRINCIPAL','\n')
question1=input('¿Desea iniciar proceso?'+'\n'+'Responda: si o no'+'\n')
while question1=='si': 
        filename=input('Ingrese el nombre del archivo a cargar al sistema de control'+'\n')
        listaarchivos.insertar(filename)
        contadorfile=0
        question=input('¿Desea cargar otro archivo al sistema de control?'+'\n'+'Responda si o no'+'\n')
        while question=='si':
                filename=input('Ingrese el nombre del archivo a cargar al sistema de control'+'\n')
                listaarchivos.insertar(filename)
                question=input('¿Desea cargar otro archivo al sistema de control?'+'\n'+'Responda si o no'+'\n')
                contadorfile+=1
        print('Finalizó la carga de archivos','\n', '\n','Los archivos cargados al sistema son: ')
        listaarchivos.mostrar_archivo()
        fileselect=input('Ingrese el nombre del archivo a procesar por el sistema de control'+'\n')
        relativepath='./ENTRADAS/'+ fileselect
        question2=input('Desea actualizar el archivo con los datos de otro archivo'+'\n'+'Responda si o no'+'\n')
        if question2=='si': 
            #actualización del archivo 1 con el archivo2 
            print('Se actualizó el archivo')
            elementTree(relativepath)
           
        else: 
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

            elementTree(relativepath)
            print('\n','Las ciudades disponibles son: ')
            crearlistaciudades.mostrar_ciudades()
            ciudadseleccionada=input('\n'+'Ingrese el número de la cuidad seleccionada'+'\n')
            tipomisión=input('\n'+'Ingrese el tipo de misión (seleccione 1 o 2)'+'\n'+'1. Misión de rescate'+'\n'+'2. Misión de extracción de recursos'+'\n')

salir=input('¿Desea salir de la aplicación' +'\n'+'Responda: si o no'+'\n')
if salir=='si':
    exit()
else: 
    print('¿Desea iniciar un nuevo proceso?')


    #         filenameselec=('Ingrese el nombre del archivo a procesar por el sistema de control','\n')
    #         question2=('Desea actualizar el archivo con los datos de otro archivo'+'\n'+'Responda si o no'+'\n')
    #         if question2=='si': 
    #                 #actualización del archivo 1 con el archivo2 
    #             print('Se actualizó el archivo')
    #             elementTree(filenameselec)
    #         else: 
    #             elementTree(filenameselec)
      #mostrar información del archivo xml
      #mostrar las ciudades disponibles
      #seleccionar ciudad a procesar
      #mostrar cantidad de ciudades
      #mostrar cantidad de recursos
      #Seleccionar tipo de mision
      #mostrar los robots disponibles dependiendo de la misión
      #validar que exista ciudad o recurso dependiendo en la ciudad para completar la misión de lo contrario  mostrar mision fallida y mostrar gráfica
      
