# Definimos un string
texto = "   Bienvenido al mundo de Python!   "

# 1. Eliminar espacios al principio y al final usando strip()
texto_limpio = texto.strip()
print(f"Texto limpio: '{texto_limpio}'")

# 2. Convertir todo el texto a mayúsculas
texto_mayusculas = texto_limpio.upper()
print(f"Texto en mayúsculas: '{texto_mayusculas}'")

# 3. Convertir todo el texto a minúsculas
texto_minusculas = texto_limpio.lower()
print(f"Texto en minúsculas: '{texto_minusculas}'")

# 4. Contar la longitud del texto
longitud = len(texto_limpio)
print(f"La longitud del texto es: {longitud}")

# 5. Reemplazar una palabra en el texto
texto_reemplazado = texto_limpio.replace("Python", "programación")
print(f"Texto después de reemplazar: '{texto_reemplazado}'")

# 6. Dividir el texto en una lista de palabras
lista_palabras = texto_limpio.split()
print(f"Lista de palabras: {lista_palabras}")

# 7. Acceso a caracteres individuales
primer_caracter = texto_limpio[0]
ultimo_caracter = texto_limpio[-1]
print(f"Primer caracter: '{primer_caracter}', Último caracter: '{ultimo_caracter}'")

# 8. Comprobar si una palabra está en el texto
palabra_buscada = "mundo"
if palabra_buscada in texto_limpio.lower():
    print(f"La palabra '{palabra_buscada}' está en el texto.")
else:
    print(f"La palabra '{palabra_buscada}' NO está en el texto.")
