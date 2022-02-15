import glob, os, shutil

src = r"C:\Users\Admin\Downloads"
docx_dir = os.path.join(src, "Docs")
img_dir = os.path.join(src, "Images")
aud_dir = os.path.join(src, "Audios")
vid_dir = os.path.join(src, "Videos")
other_dir = os.path.join(src, "Others")

docs = glob.glob("*.docx")
image = glob.glob("*.jpg")
audio = glob.glob("*.mp3")
video = glob.glob("*.mp4")
pdfs = glob.glob("*.pdf")
general = glob.glob("*.*")

files = os.listdir(src)

for file in files:
  if os.path.isfile(file):
    if docs:
      full_dest = os.path.join(docx_dir, file)
      shutil.move(file, full_dest)
    if image:
      full_dest = os.path.join(img_dir, file)
      shutil.move(file, full_dest)
    if audio:
      full_dest = os.path.join(aud_dir, file)
      shutil.move(file, full_dest)
    if video:
      full_dest = os.path.join(vid_dir, file)
      shutil.move(file, full_dest)
    if pdfs:
      full_dest = os.path.join(docx_dir, file)
      shutil.move(file, full_dest)
    if general:
      full_dest = os.path.join(other_dir, file)
      shutil.move(file, full_dest)


