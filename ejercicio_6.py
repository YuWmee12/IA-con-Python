import PyPDF2
import json

def extraer_texto_de_pdf(ruta_pdf):
    """
    Extrae el texto de cada página de un archivo PDF usando PyPDF2.

    Args:
        ruta_pdf (str): Ruta del archivo PDF.

    Returns:
        list: Lista de strings, cada uno con el contenido de una página.
    """
    with open(ruta_pdf, 'rb') as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        contenido_texto = []
        for pagina in lector_pdf.pages:
            texto = pagina.extract_text()
            contenido_texto.append(texto)
    return contenido_texto

def guardar_texto_archivo(contenido_texto, ruta_salida):
    """
    Guarda el texto extraído en un archivo de texto plano (.txt).

    Args:
        contenido_texto (list): Lista de textos extraídos por página.
        ruta_salida (str): Ruta del archivo de salida.
    """
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        for indice, texto in enumerate(contenido_texto, start=1):
            f.write(f"--- Página {indice} ---\n")
            f.write(texto)
            f.write("\n\n")

def guardar_json_archivo(contenido_texto, ruta_salida):
    """
    Guarda el texto extraído en un archivo JSON, organizándolo por páginas.

    Args:
        contenido_texto (list): Lista de textos extraídos por página.
        ruta_salida (str): Ruta del archivo JSON de salida.
    """
    data = {f"pagina_{indice}": texto for indice, texto in enumerate(contenido_texto, start=1)}
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    # Ruta fija del PDF
    ruta_pdf = r"C:\Users\52993\OneDrive\Desktop\python_ia\1 Carta compromiso SEMESTRE.pdf"

    # Rutas para guardar los archivos de salida
    salida_txt = r"C:\Users\52993\OneDrive\Desktop\python_ia\1 Carta compromis.txt"
    salida_json = r"C:\Users\52993\OneDrive\Desktop\python_ia\1 Carta compromiso.json"

    # Extraer el texto del PDF
    contenido_texto = extraer_texto_de_pdf(ruta_pdf)

    # Guardar el texto extraído en un archivo de texto
    guardar_texto_archivo(contenido_texto, salida_txt)
    print(f"Texto extraído guardado en: {salida_txt}")

    # Guardar el texto extraído en un archivo JSON
    guardar_json_archivo(contenido_texto, salida_json)
    print(f"Datos extraídos guardados en formato JSON en: {salida_json}")

if __name__ == "__main__":
    main()