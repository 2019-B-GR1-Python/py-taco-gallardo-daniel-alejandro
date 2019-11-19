# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:45:25 2019

@author: danie
"""
from consolemenu import *
from consolemenu.items import *

lista_tipos= []
lista_juegos = []

def mainMenu():
    # Create the menu
    menu = ConsoleMenu("Tienda de Videojuegos", "Menu")
    imprimir = FunctionItem("Inventario", imprimirInventario)
    editar = FunctionItem("Editar Inventario", editMenu)
    menu.append_item(imprimir) 
    menu.append_item(editar)
    menu.show()
    menu.exit()
    
    
def editMenu():
        # Create the menu
    menu = ConsoleMenu("Tienda de Videojuegos", "Menu de Edición")
    crear = FunctionItem("Crear Registro", menuCrearRegistro)
    modificar = FunctionItem("Modificar Registro", menuEditarRegistro)
    eliminar = FunctionItem("Eliminar Registro", menuEliminarRegistro)
    menu.append_item(crear) 
    menu.append_item(modificar)
    menu.append_item(eliminar)
    menu.show()

def menuEditarRegistro():
    exist = False
    text = input('Ingrese el IDV del Videojuego a Eliminar: ')
    for juego in lista_juegos:
        if juego.getIDV() == text:
                print("\nCampos posibles de modificar:\n1:Nombre\n2:Clasificacion\n3:Desarrollador\n")
                tipo = input('Ingrese el tipo de campo por modificar: ')
                dato = input('Ingrese el nuevo valor del campo: ')
                juego.modificarRegistro(tipo,dato)
                lista_juegos[lista_juegos.index(juego)]=juego
                print("\nRegistro Modificado")
                exist = True
    if not exist:
        print("El identificador ingresado no existe en los registros")
            
def menuCrearRegistro():
        print("\nLista de Generos:\n")
        for tipo in lista_tipos:
            print(tipo[0]+":"+tipo[1]+"\n")
        text = input('Seleccione el tipo de genero del videojuego que desea ingresar: ')
        name = input('Ingrese el nombre del videojuego: ')
        clasificacion = input('Ingrese la clasificacion del videojuego: ')
        desarrollador = input('Ingrese el desarrollador del videojuego: ')
        juego = Videojuego(text,lista_tipos[int(text)-1][1],len(lista_juegos)+1,name,clasificacion,desarrollador)
        escribirArchivo()
        lista_juegos.append((juego))
        print("\nRegistro Ingresado")
        
def menuEliminarRegistro():
        exist = False
        text = input('Ingrese el IDV del Videojuego a Eliminar: ')
        for juego in lista_juegos:
            if juego.getIDV() == text:
                lista_juegos.remove(juego)
                juego.eleminarRegistro()
                print("\nRegistro Eliminado")
                exist = True
        if not exist:
            print("El identificador ingresado no existe en los registros")
                 

def escribirArchivo():
        path = './juegos.txt'
        text = ""
        archivo_escritura_abierto = open(path, mode="w")
            #text = str(self.__IDT+","+self.__nombre+","+self.__clasificacion+","+self.__desarrollador)
        for juego in lista_juegos:
            archivo_escritura_abierto.write(str(juego.lineaAImprimir()))
        archivo_escritura_abierto.close()

def imprimirInventario():
    print("\nLista de VideoJuegos:\n")
    for juego in lista_juegos:
        print(juego)

def cargarDatos():
    try:
        path = "./tipos.txt"
        archivo_abierto = open(path)
        contenido = archivo_abierto.readlines()
        for linea in contenido:
            linea = linea.split(",")
            lista_tipos.append([linea[0],linea[1]])
        archivo_abierto.close()
    except Exception as error:
        print("Error")
    
    try:
        path = "./juegos.txt"
        archivo_abierto = open(path)
        contenido = archivo_abierto.readlines()
        for linea in contenido:
            linea = linea.split(",")
            IDT = linea[1]
            if any(IDT in lista_tipos for lista_tipos  in lista_tipos):
                juego = Videojuego(IDT,lista_tipos[int(linea[1])][1],linea[0],linea[2],linea[3],linea[4])
                lista_juegos.append((juego))
        archivo_abierto.close()
    except Exception as error:
        print("Error")
        
        
class TipoDeJuego:
    __IDT: None
    __genero: None
    
    def __init__(self,IDT,genero):
        self.__IDT = IDT
        self.__genero = genero
    def __str__(self):
        return  f"IDT: {self.__IDT}\n" + f"Genero: {self.__genero}\n"
    def getIDT(self):
        return self.__IDT

        
class Videojuego(TipoDeJuego):
    __IDV = None
    __nombre = None
    __clasificacion = None
    __desarrollador = None
    
    def __init__(self,IDT,genero,IDV,nombre,clasificacion,desarrollador):
        super().__init__(IDT,genero)
        self.__IDV = IDV
        self.__nombre = nombre
        self.__clasificacion = clasificacion
        self.__desarrollador = desarrollador
        
    def getIDV(self):
        return self.__IDV
    
    def eleminarRegistro(self):
        escribirArchivo()
        
    def modificarRegistro(self,tipo,dato):
        if tipo == "1":
            self.__nombre = dato
        else:
            if tipo == "2":
                self.__clasificacion = dato
            else:
                if tipo == "3":
                    self.__desarrollador = dato
        escribirArchivo()
                    
        
    def lineaAImprimir(self):
        return f"{self.__IDV},"+self.getIDT()+f",{self.__nombre},{self.__clasificacion},{self.__desarrollador}"
    
            
    def __str__(self):
        return super().__str__() + f"IDV: {self.__IDV}\n" + f"Nombre: {self.__nombre}\n" + f"Clasificacion: {self.__clasificacion}\n" + f"Desarrollador: {self.__desarrollador}\n"
        
cargarDatos()
mainMenu()