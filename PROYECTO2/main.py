from tkinter import *
from tkinter import filedialog
from ListaCiudades import ListaCiudades
import os
import xml.etree.ElementTree as ET
from ListaRobots import ListaRobots
from MatrizDispersa import MatrizDispersa
from ListaTipoCelda import ListaTipoCelda

listaRobotsRescue= ListaRobots()
listaRobotsFighter=ListaRobots()
crearlistaciudades=ListaCiudades()

def elementTree(ruta):
    contador=0   #cantidad de procesos para conocer lista ciudades o robots
    tree=ET.parse(ruta)
    raiz= tree.getroot()
    for listaciudadesorobots in raiz:
        if listaciudadesorobots.tag=="listaCiudades":
            contadordos=0 #cuantas ciudades en cada lista de ciudades
            for ciudad in listaciudadesorobots:
                contadortres=0   #cuantas filas y milatares. Y cantidad de etiquetas nombre
                contadorintransitable=0
                contadorentradas=0
                contadorcamino=0
                contadorrecursos=0
                contadorcivil=0
                for nombre in ciudad:
                    nombretag=nombre.tag
                    if nombre.tag=="nombre":
                        nombreciudad=nombre.text
                        filasciudad=(nombre.attrib['filas'])
                        columnasciudad=(nombre.attrib['columnas'])
                        crearlistaciudades.insertar(nombreciudad,filasciudad,columnasciudad)
                        #crearlistaciudades.mostrar_ciudades()
                    elif nombre.tag=="fila":
                        numfilamalla=nombre.attrib['numero']
                        celdasciudad=nombre.text
                        celdaunitaria=celdasciudad
                        contadorseis=0
                        posicióny=0
                        for celda in celdaunitaria:
                            if celda== '*':
                                contadorintransitable+=1
                            elif celda=='E':
                                contadorentradas+=1
                            elif celda=='C':
                                contadorcivil+=1
                                crearlistaciudades.retornar_nodo(contadordos).ListaTipoCelda.insertar_tipo_celda(contadorcivil)
                            elif celda=='R':
                                contadorrecursos+=1
                                crearlistaciudades.retornar_nodo(contadordos).ListaTipoCeldaRecursos.insertar_tipo_celda_recursos(contadorrecursos)
                            elif celda==' ':
                                contadorcamino+=1
                            crearlistaciudades.retornar_nodo(contadordos).MatrizDispersa.insertar(numfilamalla,contadorseis,celda, 'none', 'none', contadorintransitable, contadorentradas,contadorcamino,contadorrecursos,contadorcivil)
                            #crearlistaciudades.retornar_nodo(contadordos).MatrizDispersa.actualizarMilitar(1,1,100)
                            #crearlistaciudades.retornar_nodo(contadordos).MatrizDispersa.graficarNeato('prueba2')
                            contadorseis+=1
                            posicióny+=1
                    elif nombre.tag =="unidadMilitar":
                        capacidadmilitar=nombre.text
                        filamilitar=nombre.attrib['fila']
                        columnamilitar=nombre.attrib['columna'] 
                        crearlistaciudades.retornar_nodo(contadordos).MatrizDispersa.actualizarMilitar(filamilitar,columnamilitar,capacidadmilitar)         
                        #crearlistaciudades.retornar_nodo(contadordos).MatrizDispersa.graficarNeato('prueba')
                    contadortres+=1
                contadordos+=1
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
question1=input('¿Desea iniciar la aplicación?'+'\n'+'Responda: si o no'+'\n')
if question1=='si': 
    raiz=Tk()
    def abrirArchivo():
        archivo=filedialog.askopenfilename(title="abrir", initialdir="C:/Users/Linda Quelex/Desktop/UNIVERSIDAD 2022/LAB IPC2/PROYECTO 2/IPC2_Proyecto2_201403745/PROYECTO2/ENTRADAS")
        elementTree(archivo)
    Button(raiz,text="Seleccionar Archivo", command=abrirArchivo).pack()
    raiz.mainloop()
    print('\n','Finalizó la carga de archivos','\n')
    contadorprocesos=0
    while contadorprocesos>=0:
        print('............................................................................................')
        tipomisión=input('\n'+'Ingrese el tipo de misión (seleccione 1 o 2)'+'\n'+'1. Misión de rescate'+'\n'+'2. Misión de extracción de recursos'+'\n')
        print('\n')
        if tipomisión=="1":
            if listaRobotsRescue.size==0:
                print('No existe robot ChapinRescue para llevar a cabo la misión')
                print('.......................................')
                print('Tipo de misión: Rescate','\n','Unidad civil rescatada: ninguna','\n','Robot utlizado: ninguno')
                print('Resultado----->Misión imposible')
                print('.......................................')
            elif listaRobotsRescue.ultimo.getid()==0:
                print('El único robot ChapinRescue disponible es:')
                listaRobotsRescue.mostrar_robot()
                print('\n')
                print('Las ciudades disponibles para completar la misión son: ')
                crearlistaciudades.mostrar_ciudades()
                ciudadseleccionada=input('\n'+'Ingrese el número de la cuidad seleccionada'+'\n')
                conteociviles=crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).ListaTipoCelda.size
                if conteociviles==0:
                    print('------------------------')
                    print('¡ALERTA!')
                    print('La ciudad no tiene unidades civiles para rescatar')
                    print('------------------------')
                elif conteociviles==1:
                    print('\n')
                    print('Existe una única unidad civil a rescatar')
                    print('\n', 'Ingrese las coordenadas del punto de entrada:')
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Seleccionar_Punto_Entrada')
                    filaentrada=input('Ingrese fila:'+'\n')
                    columnaentrada=input('Ingrese columna:'+'\n')
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_de_Rescate')
                    print('.......................................')
                    print('Tipo de misión: Rescate','\n','Unidad civil rescatada:','x',',','y','\n','Robot utlizado:', listaRobotsRescue.ultimo.nombrerobot, '(ChapinRescue)')
                    print('Resultado----->Mision realizada')
                    print('.......................................')
                elif conteociviles>1:
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Seleccionar_Unidad_Civil')
                    print('\n','Ingrese las coordenadas de la unidad civil a rescatar:')
                    filacivil=input('Ingrese fila:'+'\n')
                    columnacivil=input('Ingrese columna:'+'\n')
                    print('\n', 'Ingrese las coordenadas del punto de entrada:')
                    filaentrada=input('Ingrese fila:'+'\n')
                    columnaentrada=input('Ingrese columna:'+'\n')
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_de_Rescate')
                    print('.......................................')
                    print('Tipo de misión: Rescate','\n','Unidad civil rescatada:',filacivil,',',columnacivil,'\n','Robot utlizado:', listaRobotsRescue.ultimo.nombrerobot, '(ChapinRescue)')
                    print('Resultado----->Mision realizada')
                    print('.......................................')
            elif listaRobotsRescue.ultimo.getid()>0:  
                print('Los robots ChapinRescue disponibles son:')
                listaRobotsRescue.mostrar_robot()
                retornarrobot=input('\n'+'Ingrese el número de Robot seleecionado:'+'\n')
                print('\n','El robot que realizará la misión es:')
                listaRobotsRescue.retornar_nodo(int(retornarrobot))
                print('\n')
                print('Las ciudades disponibles para completar la misión son: ')
                crearlistaciudades.mostrar_ciudades()                
                ciudadseleccionada=input('\n'+'Ingrese el número de la cuidad seleccionada'+'\n')
                conteociviles=crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).ListaTipoCelda.size
                if conteociviles==0:
                    print('------------------------')
                    print('¡ALERTA!')
                    print('La ciudad no tiene unidades civiles para rescatar')
                    print('------------------------')
                elif conteociviles==1:
                    print('\n')
                    print('Existe una única unidad civil a rescatar')
                    print('\n', 'Ingrese las coordenadas del punto de entrada:')
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Seleeccionar_Punto_Entrada')
                    filaentrada=input('Ingrese fila:'+'\n')
                    columnaentrada=input('Ingrese columna:'+'\n')
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_de_Rescate')
                    print('.......................................')
                    print('Tipo de misión: Rescate','\n','Unidad civil rescatada:','x',',','y','\n','Robot utlizado:', listaRobotsRescue.ultimo.nombrerobot, '(ChapinRescue)')
                    print('Resultado----->Mision realizada')
                    print('.......................................')
                elif conteociviles>1:
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Seleccionar_Unidad_Civil')
                    print('\n', 'Ingrese las coordenadas de la unidad civil a rescatar:')
                    fila=input('Ingrese fila:'+'\n')
                    columna=input('Ingrese columna:'+'\n')
                    print('\n', 'Ingrese las coordenadas del punto de entrada:')
                    filaentrada=input('Ingrese fila:'+'\n')
                    columnaentrada=input('Ingrese columna:'+'\n')  
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_de_Rescate')
                    print('.......................................')
                    print('Tipo de misión: Rescate','\n','Unidad civil rescatada:',fila,',',columna,'\n','Robot utlizado:', listaRobotsRescue.retornar_NombreRobotRescate(int(retornarrobot)).nombrerobot, '(ChapinRescue)')
                    print('Resultado----->Mision realizada')
                    print('.......................................') 
        elif tipomisión=="2": 
            if listaRobotsFighter.size==0:
                print('No existe robot ChapinFighter para llevar a cabo la misión')
                print('Tipo de misión: Extracción','\n','Recursos rescatados: ninguno','\n','Robot utlizado: ninguno')
                print('Resultado----->Misión imposible')
                print('.......................................')
            elif listaRobotsFighter.ultimo.getid()==0:
                print('El único robot ChapinFighter disponible es:')
                listaRobotsFighter.mostrar_robot()
                print('\n')
                print('Las ciudades disponibles para completar la misión son: ')
                crearlistaciudades.mostrar_ciudades()
                ciudadseleccionada=input('\n'+'Ingrese el número de la cuidad seleccionada'+'\n')
                conteorecursos=crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).ListaTipoCeldaRecursos.size
                if conteorecursos==0:
                    print('------------------------')
                    print('¡ALERTA!')
                    print('La ciudad no tiene recursos para extraer')
                    print('------------------------')
                elif conteorecursos==1:
                    print('\n')
                    print('Existe un único recurso a extraer')
                    print('\n')
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Selección_Punto_Entrada')
                    print('\n', 'Ingrese las coordenadas del punto de entrada:')
                    filaentrada=input('Ingrese fila:'+'\n')
                    columnaentrada=input('Ingrese columna:'+'\n')
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_de_Extracción')
                    print('.......................................')
                    print('Tipo de misión: Extracción','\n','Recurso extraido:','x',',','y','\n','Robot utlizado:', listaRobotsFighter.ultimo.nombrerobot, '(ChapinFighter- Capacidad de combate inicial:','cap_inicial',',','Capacidad de combate final: '+'cap_final',')')
                    print('Resultado----->Mision realizada')
                    print('.......................................')
                elif conteorecursos>1:
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Seleccionar_Recurso_a_Extraer')
                    print('\n', 'Ingrese las coordenadas del recurso a extraer:')
                    filarecurso=input('Ingrese fila:'+'\n')
                    columnarecurso=input('Ingrese columna:'+'\n')
                    print('\n', 'Ingrese las coordenadas del punto de entrada:')
                    filaentrada=input('Ingrese fila:'+'\n')
                    columnaentrada=input('Ingrese columna:'+'\n')  
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_de_Extracción')
                    print('.......................................')
                    print('Tipo de misión: Extracción','\n','Recurso Extraido:',filarecurso,',',columnarecurso,'\n','Robot utlizado:', listaRobotsFighter.retornar_NombreRobotRescate(int(retornarrobot)).nombrerobot, '(ChapinFighter- Capacidad de combate inicial:','cap_inicial',',','Capacidad de combate final'+'cap_final',')')
                    print('Resultado----->Mision realizada')
                    print('.......................................') 
            elif listaRobotsFighter.ultimo.getid()>0:
                print('Los robots ChapinFighter disponibles son:')
                listaRobotsFighter.mostrar_robot()
                retornarrobot=input('\n'+'Ingrese el número de Robot seleecionado:'+'\n')
                print('\n','El robot que realizará la misión es:')
                listaRobotsFighter.retornar_nodo(int(retornarrobot))
                print('\n')
                print('Las ciudades disponibles para completar la misión son: ')
                crearlistaciudades.mostrar_ciudades()
                ciudadseleccionada=input('\n'+'Ingrese el número de la cuidad seleccionada'+'\n')
                conteorecursos=crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).ListaTipoCeldaRecursos.size
                if conteorecursos==0:
                    print('------------------------')
                    print('¡ALERTA!')
                    print('La ciudad no tiene recursos para extraer')
                    print('------------------------')
                elif conteorecursos==1:
                    print('\n')
                    print('Existe un único recurso a extraer')
                    print('\n')
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Selección_Punto_Entrada')
                    print('\n', 'Ingrese las coordenadas del punto de entrada:')
                    filaentrada=input('Ingrese fila:'+'\n')
                    columnaentrada=input('Ingrese columna:'+'\n')
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_de_Extracción')
                    print('.......................................')
                    print('Tipo de misión: Extracción','\n','Recurso extraido:','x',',','y','\n','Robot utlizado:', listaRobotsFighter.ultimo.nombrerobot, '(ChapinFighter- Capacidad de combate inicial:','cap_inicial',',','Capacidad de combate final'+'cap_final',')')
                    print('Resultado----->Mision realizada')
                    print('.......................................')
                elif conteorecursos>1:
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Seleccionar_Recurso_a_Extraer')
                    print('\n', 'Ingrese las coordenadas del recurso a extraer:')
                    filarecurso=input('Ingrese fila:'+'\n')
                    columnarecurso=input('Ingrese columna:'+'\n')
                    print('\n', 'Ingrese las coordenadas del punto de entrada:')
                    filaentrada=input('Ingrese fila:'+'\n')
                    columnaentrada=input('Ingrese columna:'+'\n')  
                    crearlistaciudades.retornar_nodo(int(ciudadseleccionada)).MatrizDispersa.graficarNeato('Misión_de_Extracción')
                    print('.......................................')
                    print('Tipo de misión: Extracción','\n','Recurso Extraido:',filarecurso,',',columnarecurso,'\n','Robot utlizado:', listaRobotsFighter.retornar_NombreRobotRescate(int(retornarrobot)).nombrerobot, '(ChapinFighter- Capacidad de combate inicial:','cap_inicial',',','Capacidad de combate final'+'cap_final',')')
                    print('Resultado----->Mision realizada')
                    print('.......................................') 

        print('\n')
        salir=input('¿Desea salir de la aplicación?' +'\n'+'Responda: si o no'+'\n')
        if salir=='si':
            exit()
        else:
            contadorprocesos+=1

    
