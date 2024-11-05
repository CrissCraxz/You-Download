import os
import yt_dlp
import queue
import threading
import time

# Cola global para manejar los videos/listas de reproducción hysito
download_queue = queue.Queue()

# Función para descargar videos individuales


def download_video(url, download_path):
    ydl_opts = {
        # Limitar calidad
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        # Guardar el video con su título
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',  # Fusionar video y audio en MP4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Función para descargar listas de reproducción


def download_playlist(url):
    download_path = os.path.join(os.path.expanduser('~'), 'YouTube', 'Listas')
    os.makedirs(download_path, exist_ok=True)  # Crear la carpeta si no existe
    print(f"Usando directorio para listas: {download_path}")

    ydl_opts = {
        # Limitar calidad
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        # Guardar en carpetas según la lista
        'outtmpl': os.path.join(download_path, '%(playlist)s/%(title)s.%(ext)s'),
        'noplaylist': False,  # Descargar la lista de reproducción completa
        'merge_output_format': 'mp4',  # Fusionar video y audio en MP4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Función para procesar la cola de descargas


def process_queue():
    while True:
        if not download_queue.empty():
            url = download_queue.get()
            # Verificar si es una lista de reproducción o un video individual
            if 'playlist' in url:
                download_playlist(url)
            else:
                download_path = os.path.join(os.path.expanduser(
                    '~'), 'YouTube', 'Videos Individuales')
                os.makedirs(download_path, exist_ok=True)
                print(f"Usando directorio para videos individuales: {
                      download_path}")
                download_video(url, download_path)

            download_queue.task_done()  # Marcar como completado en la cola

# Función principal para agregar videos a la cola


def main():
    # Crear la carpeta principal 'YouTube' donde se guardarán las descargas
    base_download_path = os.path.join(os.path.expanduser('~'), 'YouTube')
    # Crear carpeta si no existe
    os.makedirs(base_download_path, exist_ok=True)

    # Iniciar el hilo que procesará la cola de descargas
    download_thread = threading.Thread(target=process_queue, daemon=True)
    download_thread.start()

    while True:
        url = input(
            "Ingresa la URL del video o lista de reproducción de YouTube (o 'salir' para terminar): ")
        if url.lower() == 'salir':
            print("Saliendo del programa...")
            break
        download_queue.put(url)  # Añadir el enlace a la cola
        print(f"Se añadió el enlace {url} a la cola. Total en cola: {
              download_queue.qsize()}")

    # Esperar a que la cola de descargas termine de procesarse
    download_queue.join()
    print("Todas las descargas han sido completadas.")


if __name__ == '__main__':
    main()

