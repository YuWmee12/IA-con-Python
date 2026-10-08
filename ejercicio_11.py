# 1. Crear y escribir en un archivo
with open("mi_archivo.txt", "w") as archivo:
    archivo.write("Mi primer Archivo de texto creado con Python.\n")
    archivo.write("Lizeth Mayumi Hernandez Luciano.\n")
    archivo.write("Version 1 del Archivo\n")


# 2. Leer el contenido del archivo
with open("mi_archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo despues de crearlo:")
    print(contenido)


# 3. Agregar mas texto al archivo
with open("mi_archivo.txt", "a") as archivo:
    archivo.write("Version 2 de mi archivo txt.\n")
    archivo.write("Python facilita la manipulacion de archivos de texto.\n")


# 4. Leer el contenido actualizado del archivo
with open("mi_archivo.txt", "r") as archivo:
    contenido_actualizado = archivo.read()
    print("\nContenido del archivo despues de agregar mas texto:")
    print(contenido_actualizado)
    
    