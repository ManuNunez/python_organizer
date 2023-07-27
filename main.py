import os
import shutil

def organizar_archivos(carpeta):
    # Verificar si la carpeta de destino existe, si no, crearla
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Lista todos los archivos en la carpeta
    archivos = os.listdir(carpeta)

    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)

        if os.path.isfile(ruta_archivo):
            # Obtener la extensión del archivo
            _, extension = os.path.splitext(archivo)

            # Definir las categorías y sus extensiones correspondientes
            categorias = {
                'Imágenes': ['.jpg', '.jpeg', '.png', '.gif'],
                'Documentos': ['.doc', '.docx', '.pdf', '.txt'],
                'Música': ['.mp3', '.wav', '.ogg'],
                'Videos': ['.mp4'], 
                'Código': ['.py', '.c', '.cpp', '.html', '.css', '.js'],

            }

            # Encontrar la categoría del archivo
            categoria_encontrada = None
            for categoria, extensiones in categorias.items():
                if extension.lower() in extensiones:
                    categoria_encontrada = categoria
                    break

            # Si no se encuentra una categoría, el archivo se clasifica como 'Otros'
            if not categoria_encontrada:
                categoria_encontrada = 'Otros'

            # Crear la carpeta para la categoría, si no existe
            carpeta_categoria = os.path.join(carpeta, categoria_encontrada)
            if not os.path.exists(carpeta_categoria):
                os.makedirs(carpeta_categoria)

            # Mover el archivo a la carpeta de la categoría
            nueva_ruta_archivo = os.path.join(carpeta_categoria, archivo)
            shutil.move(ruta_archivo, nueva_ruta_archivo)

if __name__ == "__main__":
    # Ruta de la carpeta que deseas organizar
    print ("inserte la ruta de la carpeta")
    path = input()
    organizar_archivos(path)
