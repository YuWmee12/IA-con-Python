from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, Canvas, Scrollbar, Frame
from collections import Counter

# Configuración: Umbral mínimo de píxeles para mostrar un color
UMBRAL_MINIMO = 500  # Ajusta este valor según la imagen

def get_colors(image_path):
    """Analiza los colores dominantes en una imagen y filtra por cantidad mínima."""
    try:
        image = Image.open(image_path)
        image = image.convert("RGB")  # Convertir a RGB
        pixels = np.array(image)
        pixels = pixels.reshape(-1, 3)  # Convertir a lista de colores

        # Obtener dimensiones
        ancho, alto = image.size

        # Contar colores
        color_counts = Counter(map(tuple, pixels))

        # Filtrar solo los colores que superen el umbral mínimo
        filtered_colors = {color: count for color, count in color_counts.items() if count > UMBRAL_MINIMO}

        # Ordenar de mayor a menor cantidad
        top_colors = sorted(filtered_colors.items(), key=lambda x: x[1], reverse=True)

        return top_colors, ancho, alto
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return [], 0, 0

def show_colors_window(top_colors, ancho, alto):
    """Muestra los colores y el tamaño de la imagen en una ventana gráfica con Scroll."""
    if not top_colors:
        print("No hay colores con suficiente cantidad para mostrar.")
        return

    # Crear ventana principal
    root = tk.Tk()
    root.title("Análisis de Imagen")

    # Crear contenedor con Scroll
    main_frame = Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    canvas = Canvas(main_frame)
    scrollbar = Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = Frame(canvas)

    # Configurar el frame scrollable
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Mostrar tamaño de la imagen
    size_label = tk.Label(scrollable_frame, text=f"Tamaño de la imagen: {ancho} x {alto} píxeles", font=("Arial", 12, "bold"))
    size_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Crear etiquetas y cuadros de color
    for i, (color, count) in enumerate(top_colors, start=1):
        rgb_text = f"RGB: {color} - Cantidad: {count}"

        # Convertir valores np.uint8 a enteros normales
        color_int = tuple(map(int, color))

        # Etiqueta con el código RGB
        label = tk.Label(scrollable_frame, text=rgb_text, font=("Arial", 12))
        label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

        # Cuadro con el color
        color_hex = f"#{color_int[0]:02x}{color_int[1]:02x}{color_int[2]:02x}"
        color_box = tk.Canvas(scrollable_frame, width=50, height=20, bg=color_hex)
        color_box.grid(row=i, column=1, padx=10, pady=5)

    # Empaquetar elementos con scroll
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Ejecutar la ventana
    root.mainloop()

# Pedir imagen al usuario
image_path = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Archivos de imagen", ".jpg;.png;*.jpeg")])

if image_path:
    # Obtener colores y tamaño de la imagen
    top_colors, ancho, alto = get_colors(image_path)

    # Mostrar los colores y el tamaño en la ventana
    show_colors_window(top_colors, ancho, alto)
else:
    print("No se seleccionó ninguna imagen.")