# YouTube Video Downloader with Queue Support

Este proyecto es un descargador de videos y listas de reproducción de YouTube, con soporte para agregar nuevas descargas mientras otras están en curso. Los videos se descargan en carpetas organizadas de acuerdo a si son videos individuales o listas de reproducción, y se puede agregar contenido a la cola de descargas en tiempo real.

## Requisitos

Asegúrate de tener instalado Python 3.6+ y los siguientes paquetes antes de comenzar:


bash

    pip install yt-dlp

Uso

    Ejecuta el script youtube-dw.py en tu terminal:

    bash

    python youtube-dw.py

    Se te pedirá ingresar la URL de un video individual o una lista de reproducción de YouTube. Puedes seguir agregando más URLs mientras se descargan otros videos o listas.
        Si deseas detener el proceso de entrada de URLs, escribe salir.
        El programa continuará descargando todo lo que esté en la cola hasta finalizar.

    Los videos se descargarán en la carpeta YouTube ubicada en tu directorio de usuario. Los videos individuales se guardarán en YouTube/Videos Individuales, mientras que las listas de reproducción se guardarán en YouTube/Listas.

Ejemplo de uso:

bash

Ingresa la URL del video o lista de reproducción de YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Se añadió el enlace https://www.youtube.com/watch?v=dQw4w9WgXcQ a la cola. Total en cola: 1

Ingresa la URL del video o lista de reproducción de YouTube: https://www.youtube.com/playlist?list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj
Se añadió el enlace https://www.youtube.com/playlist?list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj a la cola. Total en cola: 2

Ingresa la URL del video o lista de reproducción de YouTube: salir
Saliendo del programa...
