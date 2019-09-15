import subprocess
from tkinter import *
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import shutil
import os
from pydub import AudioSegment
from pytube import YouTube
import time

def file_path(file_name):
    return os.path.dirname(os.path.realpath(__file__)) + os.sep + file_name


def runCommand(command):
    out = subprocess.Popen(command.split(), shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    stdout, stderr = out.communicate()
    out = stdout.decode('utf-8')
    text.insert(END, out)
    print(out)


def download():
    current = os.getcwd()
    # current = current + r"\"
    value = linkEntry.get()
    # download = r"youtube-dl.exe -x " + value + " --audio-format mp3 -o C:/Users/rsuri/Desktop/SpotifyLocalFilesbackup/%(title)s.%(ext)s"
    # download = r"youtube-dl.exe -x https://www.youtube.com/watch?v=a1Y73sPHKxw --audio-format mp3 -o %(title)s.%(ext)s"

    # download = r"youtube-dl.exe -x " + value + " --audio-format mp3 -o %(title)s.%(ext)s"
    # runCommand(download)
    # download = r"youtube-dl.exe -x " + value + " --audio-format mp3"
    # out = subprocess.Popen(download.split(), shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    # stdout, stderr = out.communicate()
    # out = stdout.decode('utf-8')
    # text.insert(END, out)
    # print(out + "stdout")

    yt = YouTube('https://www.youtube.com/watch?v=rUWxSEwctFU')
    file_name = str(int(time.time()))
    yt.streams.filter(file_extension='mp4').first().download(filename=file_name)

    title = titleEntry.get()
    artist = artistEntry.get()
    album = albumEntry.get()

    fileTitle4 = file_name + '.mp4'
    fileTitle3 = title + '.mp3'

    AudioSegment.from_file(file_path(fileTitle4), 'mp4').export(file_path(fileTitle3), format="mp3")
    # AudioSegment.from_file('All over in 10 seconds.mp4').export('All over in 10 seconds.mp3', format="mp3")

    print(fileTitle3 + "=filetitle")
    print(MP3File.url)
    mp3 = MP3File(file_path(fileTitle3))
    # mp3 = MP3File(current+fileTitle3)

    mp3.album = album
    mp3.artist = artist
    mp3.song = title
    mp3.save()

    os.remove(file_path(fileTitle4))

    # shutil.move('C:/Users/rsuri/PycharmProjects/Test/' + fileTitle, 'C:/Users/rsuri/Desktop/Spotify Local Files backup/'+fileTitle)
    # shutil.move(current + fileTitle, 'C:/Users/rsuri/Desktop/Spotify Local Files backup/' + fileTitle)

    # m = 'id3.exe -t "' + title1 + '" -a "' + artist + '" -l "' + album + '" "' +getName(value)
    # m = m[:-1] + '.mp3"'
    # print(m)
    # out1 = subprocess.Popen(m.split(),shell=True,stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    # stdout,stderr=out1.communicate()
    # out1 = stdout.decode('utf-8')
    # print(out1)
    # text.insert(END,out1)


def getName(link):
    cmd = "youtube-dl.exe --skip-download --get-title " + link
    # subprocess.run(cmd.split())
    out = subprocess.Popen(cmd.split(), shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

    stderr, stdout = out.communicate()
    out = stderr.decode('utf-8')

    text.insert(END, out)

    return out


root = Tk()
root.title("this is tkinter")
root.geometry("815x600+30+30")

tFrame = Frame(root)
bFrame = Frame(root)
# tFrame.grid(side=TOP)

tFrame.grid(row=0, sticky=W)
bFrame.grid(row=1)

linkLabel = Label(tFrame, text="Link:")
titleLabel = Label(tFrame, text="Title: ")
artistLabel = Label(tFrame, text="Artist: ")
albumLabel = Label(tFrame, text="Album: ")
outputLabel = Label(tFrame, text="Output:")

linkLabel.grid(row=0, sticky=W)
titleLabel.grid(row=1, sticky=W)
artistLabel.grid(row=2, sticky=W)
albumLabel.grid(row=3, sticky=W)
outputLabel.grid(row=4, sticky=W)

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

# w3=Label(root, text="ywdywdydwydwyydwydwywdywdywydywdydwyydwydwydwydwydwydwydwydwydwydwydwydwyydwydwydwydwyd")
#
# w3.grid(column=5,row=0)

dlBtn = Button(tFrame, text="download", command=download)
dlBtn.grid(row=4, column=1, sticky=E)

text = Text(bFrame, height=20, width=100)
text.grid(row=0, padx=5)
text.insert(END, "")

root.mainloop()
