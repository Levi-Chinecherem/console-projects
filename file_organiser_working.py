import os, shutil, time

src = r"C:\Users\Admin\Downloads"
docx_dir = os.path.join(src, "Docs")
img_dir = os.path.join(src, "Images")
aud_dir = os.path.join(src, "Audios")
vid_dir = os.path.join(src, "Videos")
zip_dir = os.path.join(src, "Zip_Files")
other_dir = os.path.join(src, "Others")

images = ["jpg", "png", "jpeg", "gif", "tiff", "webp", "svg"]
audio = ["mp3", "wav"]
video = ["mp4", "webm", "avi"]
docs = ["ai", "ait", "txt", "rtf", "docx", "doc", "pdf"]
zip_files = ["zip"]

while True:
  os.chdir(src)
  time.sleep(3)
  for file in os.listdir():
    if os.path.isfile(file):
      name = file.split(".")
      ext = (name[-1]).lower()
      
      if ext in docs:
        shutil.move(file, docx_dir)
      elif ext in images:
        shutil.move(file, img_dir)
      elif ext in audio:
        shutil.move(file, aud_dir)
      elif ext in video:
        shutil.move(file, vid_dir)
      elif ext in zip_files:
        shutil.move(file, zip_dir)
      else:
          shutil.move(file, other_dir)
