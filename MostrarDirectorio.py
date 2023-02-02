'''
Este programa permite recuperar el contenido de la ruta donde 
se esta ejecutando el programa de python.
Muestra todo el contenido del directorio, diferenciando si se trata 
de un archivo o de otro directorio
'''

#Importa librería para poder trabajar con el sistema operativo 
import os 

#Recupera el directorio actual 
Directorio = os.getcwd()

#Recupera la lista del directorio
Contenido = os.listdir(path = Directorio)

#Muestra en el terminal el contenido recuperado
#print(Contenido)

#Recupera información del directorio
Informacion = os.scandir(Directorio)

#Recorre todos los archivos encontrados en el directorio
# muestra en pantalla si se trata de un archivo o de otro directorio
for Archivo in Informacion:
    if Archivo.is_dir():
        #Muestra el nombre del directorio 
        print("Dir: ", Archivo.name)
    elif Archivo.is_file():
        #Muestra el nombre del archivo
        print(f"File: {Archivo.name}")