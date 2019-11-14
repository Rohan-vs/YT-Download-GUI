import subprocess
from tkinter import *
from tkinter import filedialog
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import shutil
import os
from pydub import AudioSegment
from pytube import YouTube
import time


fPath = os.getcwd() + os.sep

def file_path(file_name):
    # return os.path.dirname(os.path.realpath(__file__)) + os.sep + file_name
    return os.getcwd() + os.sep + file_name


# def runCommand(command):
#     out = subprocess.Popen(command.split(), shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
#     stdout, stderr = out.communicate()
#     out = stdout.decode('utf-8')
#     text.insert(END, out)
#     print(out)


def download():
    import moviepy.editor as mp
    current = os.getcwd() + os.sep
    value = linkEntry.get()

    yt = YouTube(value)
    file_name = str(int(time.time()))
    yt.streams.filter(file_extension='mp4').first().download(filename=file_name)

    title = titleEntry.get()
    artist = artistEntry.get()
    album = albumEntry.get()

    fileTitle4 = file_name + '.mp4'
    fileTitle3 = title + '.mp3'

    clip = mp.VideoFileClip(fileTitle4)

    clip.audio.write_audiofile(fileTitle3)

    # print(fileTitle3 + "=filetitle")
    print(MP3File.url)
    mp3 = MP3File(file_path(fileTitle3))
    # mp3 = MP3File(current+fileTitle3)

    mp3.album = album
    mp3.artist = artist
    mp3.song = title
    mp3.save()

    os.remove(file_path(fileTitle4))


    shutil.move(current+fileTitle3, fPath + os.sep + fileTitle3)


def filePath():
    global fPath
    fPath=filedialog.askdirectory() + os.sep
    pathLabel.config(text=fPath)



root = Tk()
root.title("this is tkinter")
root.geometry("815x600+30+30")

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

ew = 30
linkEntry.config(width=ew)
titleEntry.config(width=ew)
artistEntry.config(width=ew)
albumEntry.config(width=ew)


dlBtn = Button(tFrame, text="download", command=download)
dlBtn.grid(row=4, column=1, sticky=E)

fPath = Button(tFrame, text="File Path: ", command=filePath)
fPath.grid(row=2,column=2,sticky=E)

text = Text(bFrame, height=20, width=100)
text.grid(row=0, padx=5)
text.insert(END, "")




root.mainloop()

