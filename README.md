# Youtube Downloader
### Script Python para descargar videos de youtube

Para hacer funcionar el programa se deben descargar las siguientes librerías:
```sh
pip install pafy moviepy ffmpeg
```
| Librería | Enlace |
| ------ | ------ |
|Pafy|[https://github.com/mps-youtube/pafy]|
|MoviePy|[https://github.com/Zulko/moviepy]|
|FFMPEG|[https://github.com/FFmpeg/FFmpeg]|

## Funcionamiento
Al iniciar el script se creará una subcarpeta con el nombre "export", el cual está declarado en la linea número 11 cómo:
```sh 
path = os.getcwd() + "/export/"
if not os.path.isdir(path):
    os.mkdir(path)
```
En dicha carpeta se almancenarán los archivos de videos como de audio (mp3).

_Cualquier duda, comentario o sugerencia por favor contactárme a travez de mensaje._
