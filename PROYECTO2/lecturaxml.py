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
class LecturaXML():
    def __init__(self):
        self.xml=0
        
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
