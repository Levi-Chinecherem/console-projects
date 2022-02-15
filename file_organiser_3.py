import glob, os, shutil

src = r"C:\Users\Admin\Downloads"
docx_dir = os.path.join(src, "Docs")
img_dir = os.path.join(src, "Images")
aud_dir = os.path.join(src, "Audios")
vid_dir = os.path.join(src, "Videos")
other_dir = os.path.join(src, "Others")
folder_dir = os.path.join(src, "Folders")


os.chdir(src)

for file in os.listdir():
  if os.path.isfile(file):
    if file.endswith(".docx") or file.endswith(".ai") or file.endswith(".ait") or file.endswith(".txt") or file.endswith(".pdf") or file.endswith(".rtf") or file.endswith(".doc"):
      full_dest = os.path.join(docx_dir, file)
      shutil.move(file, full_dest)
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".gif") or file.endswith(".tiff") or file.endswith(".webp"):
      full_dest = os.path.join(img_dir, file)
      shutil.move(file, full_dest)
    if file.endswith(".mp3") or file.endswith(".wav"):
      full_dest = os.path.join(aud_dir, file)
      shutil.move(file, full_dest)
    if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".webm"):
      full_dest = os.path.join(vid_dir, file)
      shutil.move(file, full_dest)
    #if file.endswith(".pdf"):
    #  full_dest = os.path.join(docx_dir, file)
    #  shutil.move(file, full_dest)
    else:
      if os.path.isfile(file):
        full_dest = os.path.join(other_dir, file)
        shutil.move(file, other_dir)
      else:
        shutil.move(file, folder_dir)