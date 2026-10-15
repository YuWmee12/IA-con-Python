#Crear un Diccionario
nombre_diccionario = {"key": "element",
                      "Nombre": "Miguel",
                      "Edad": 22
                      }
print(nombre_diccionario)
print(nombre_diccionario["Nombre"])
print(nombre_diccionario["Edad"])

print(nombre_diccionario.get("altura", "No hay altura"))

#Agregar Nuevos Valores
nombre_diccionario["altura"] = 1.70
print(nombre_diccionario)
print(nombre_diccionario.get("altura", "No hay altura"))


#Un diccionario puede tener otro diccionario dentro (anidado):



estudiante = {
    "nombre": "Luis",
    "materias": {
        "matematicas": 9,
        "historia": 8
    }
}
print(estudiante["materias"]["historia"])  # 8