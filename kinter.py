from tkinter import *
from tkinter import filedialog
import shutil
import os
from pytube import YouTube
from mutagen.easyid3 import EasyID3


fPath = os.getcwd() + os.sep

def file_path(file_name):
    # return os.path.dirname(os.path.realpath(__file__)) + os.sep + file_name
    return os.getcwd() + os.sep + file_name

def download():
    import moviepy.editor as mp
    current = os.getcwd() + os.sep
    link = linkEntry.get()

    title = titleEntry.get()
    artist = artistEntry.get()
    album = albumEntry.get()

    yt = YouTube(link)
    file_name = title
    yt.streams.filter(file_extension='mp4').first().download(filename=file_name)

    fileTitle4 = file_name + '.mp4'
    fileTitle3 = file_name + '.mp3'

    clip = mp.VideoFileClip(fileTitle4)

    clip.audio.write_audiofile(fileTitle3)
    audio = EasyID3(fileTitle3)
    audio["title"] = title
    audio["album"] = album
    audio["artist"] = artist
    audio.save()


    shutil.move(current+fileTitle3, fPathh + os.sep + fileTitle3)

def filePath():
    global fPathh
    fPathh=filedialog.askdirectory()
    pathLabel.config(text=fPathh)

root = Tk()
root.title("YT-DL-GUI")
root.geometry("815x200+30+30")

tFrame = Frame(root)
bFrame = Frame(root)
# tFrame.grid(side=TOP)

tFrame.grid(row=0, sticky=W)
bFrame.grid(row=1)

linkLabel = Label(tFrame, text="Link: ")
titleLabel = Label(tFrame, text="Title: ")
artistLabel = Label(tFrame, text="Artist: ")
albumLabel = Label(tFrame, text="Album: ")
outputLabel = Label(tFrame, text="Output: ")
pathLabel = Label(tFrame, text=fPath)

linkLabel.grid(row=0, sticky=W)
titleLabel.grid(row=1, sticky=W)
artistLabel.grid(row=2, sticky=W)
albumLabel.grid(row=3, sticky=W)
outputLabel.grid(row=4, sticky=W)
pathLabel.grid(row=2,column=3,sticky=W)

fontSize = 15
font = " "
# linkLabel.config(font=(font, fontSize))
# titleLabel.config(font=(font, fontSize))
# artistLabel.config(font=(font, fontSize))
# albumLabel.config(font=(font, fontSize))
# outputLabel.config(font=(font, fontSize))

linkEntry = Entry(tFrame)
titleEntry = Entry(tFrame)
artistEntry = Entry(tFrame)
albumEntry = Entry(tFrame)

linkEntry.grid(row=0, column=1, sticky=W)
titleEntry.grid(row=1, column=1, sticky=W)
artistEntry.grid(row=2, column=1, sticky=W)
albumEntry.grid(row=3, column=1, sticky=W)

ew = 60
linkEntry.config(width=ew)
titleEntry.config(width=ew)
artistEntry.config(width=ew)
albumEntry.config(width=ew)

dlBtn = Button(tFrame, text="download", command=download)
dlBtn.grid(row=4, column=1, sticky=E)

fPath = Button(tFrame, text="File Path: ", command=filePath)
fPath.grid(row=2,column=2,sticky=E)

# text = Text(bFrame, height=20, width=100)
# text.grid(row=0, padx=5)
# text.insert(END, "")

root.mainloop()
