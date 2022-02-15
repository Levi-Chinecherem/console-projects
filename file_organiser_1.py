import os
import shutil

images = ["jpg", "png", "jpeg", "gif", "tiff", "webp", "svg"]
audio = ["mp3", "wav"]
video = ["mp4", "webm", "avi"]
docs = ["ai", "ait", "txt", "rtf", "docx", "doc", "pdf"]

while True:
  files = os.listdir("C:\\Users\\Admin\\Downloads")

  for file in files:
    if os.path.isfile(file):
      ext = (file.split(".")[-1]).lower()

      if ext in images:
        shutil.move(file, "Images/"+file)
      if ext in audio:
        shutil.move(file, "Audios/"+file)
      if ext in video:
        shutil.move(file, "Videos/"+file)
      if ext in docs:
        shutil.move(file, "Docs/"+file)
      else:
        shutil.move(file, "Others/"+file)

