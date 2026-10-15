class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def tamaño(self):
        return len(self.items)

# Ejemplo de uso: Revertir una cadena

def revertir_cadena(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()
    return cadena_invertida

# Ejemplo de aplicación: Validar paréntesis balanceados

def parentesis_balanceados(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter == '(':
            pila.apilar(caracter)
        elif caracter == ')':
            if pila.esta_vacia():
                return False
            pila.desapilar()
    return pila.esta_vacia()

# Pruebas
cadena = "Hola Amigos"
print(f"Cadena original: {cadena}")
print(f"Cadena invertida: {revertir_cadena(cadena)}")

expresion1 = "(a+b) * (c-d)"
expresion2 = "(a+b * (c-d)"
print(f"Expresión '{expresion1}' balanceada: {parentesis_balanceados(expresion1)}")
print(f"Expresión '{expresion2}' balanceada: {parentesis_balanceados(expresion2)}")