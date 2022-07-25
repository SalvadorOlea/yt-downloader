import pafy
import os
from moviepy.editor import VideoFileClip

print("")
print("Youtube Downloader by SalvadorOlea")
print("")

path = os.getcwd() + "/export/"
if not os.path.isdir(path):
    os.mkdir(path)

url =  input("[YT] Link de youtube: " )
video = pafy.new(url)

def human_size(num: int) -> str:
    base = 1
    for unit in ['B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']:
        n = num / base
        if n < 9.95 and unit != 'B':
            # Less than 10 then keep 1 decimal place
            value = "{:.1f}{}".format(n, unit)
            return value
        if round(n) < 1000:
            # Less than 4 digits so use this
            value = "{}{}".format(round(n), unit)
            return value
        base *= 1024
    value = "{}{}".format(round(n), unit)
    return value

audio = video.getbest()
print("")
print("==================================")
print("Video: ", video.title)
print("Duración: ", video.duration)
print("Tamaño: ", human_size(audio.get_filesize()))
print("==================================")
print("")
audio.download(path + video.title + "." + audio.extension)
vid_path = path + video.title + "." + audio.extension

print("Iniciando la conversión a .mp3...")
def mp3convert(path, output_ext="mp3"):
    filename, ext = os.path.splitext(path)
    audio_path = filename + "." + output_ext
    clip = VideoFileClip(path)
    clip.audio.write_audiofile(audio_path)

mp3convert(vid_path, "mp3")
print("Proceso terminadoo...")