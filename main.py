from pytube import YouTube
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Youtube Video Downloader")
root.iconbitmap('icon.ico')
root.geometry("500x200")

input_link = Text(
    root,
    height=1,
    width=45
)

input_link.pack()

def getVideo():
    link = input_link.get("1.0",END)
    yt = YouTube(link)

    varTitle = StringVar()
    varTitle.set("Title: {}".format(yt.title))
    varViews = StringVar()
    varViews.set("Number of views: {}".format(yt.views))
    varLength = StringVar()
    varLength.set("Length of video: {}".format(yt.length))
    varRating = StringVar()
    varRating.set("Rating of video: {}".format(yt.rating))

    #Showing details
    labelTitle = Label( root, textvariable=varTitle)
    labelNumbers = Label( root, textvariable=varViews)
    labelLength = Label( root, textvariable=varLength)
    labelRating = Label( root, textvariable=varRating)

    labelTitle.pack()
    labelNumbers.pack()
    labelLength.pack()
    labelRating.pack()

    downloadButton = Button(root, text ="Download", command = download)

    downloadButton.pack()

def download():
    varDownload = StringVar()
    varDownload.set("Downloading...")
    labelDownload = Label( root, textvariable=varDownload)
    link = input_link.get("1.0",END)
    yt = YouTube(link)
    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    ys.download()
    messagebox.showinfo("Youtube Video Downloader", "Download completed!")
    root.destroy()

videoButton = Button(root, text ="Get video", command = getVideo)

videoButton.pack()

root.mainloop()