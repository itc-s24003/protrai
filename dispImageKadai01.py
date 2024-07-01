#s24003
#dispImageKadai01.py
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        apuri.config(text=fpath)

root = tk.Tk()
root.geometry("500x500")
hensu = tk.Label(text="画像表示アプリバージョン2.0", font=("Helvetica", 20))
apuri = tk.Label(text="開いてません", font=("Helvetica", 20))


btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()

hensu.pack()
btn.pack()
imageLabel.pack()
apuri.pack()

tk.mainloop()
