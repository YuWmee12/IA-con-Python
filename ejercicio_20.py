# Variable global
player_score = 0

def add_points(points):
    """Función que suma puntos al marcador global"""
    global player_score  # Indicamos que usaremos la variable global
    player_score += points
    print(f"Puntos añadidos: {points}")
    print_current_score()

def reset_score():
    """Función que reinicia el marcador"""
    global player_score
    player_score = 0
    print("El marcador se ha reiniciado.")

def print_current_score():
    """Función que imprime el marcador actual"""
    # Aquí usamos la variable global directamente
    print(f"Marcador actual: {player_score}")

def simulate_game():
    """Simulación de un juego usando variables locales y globales"""
    # Variable local: solo existe dentro de esta función
    bonus = 10
    print("¡Inicio del juego!")
    add_points(5)      # Usando la variable global
    add_points(bonus)  # Pasando una variable local como argumento
    reset_score()
    add_points(7)

# Ejecutar la simulación
simulate_game()