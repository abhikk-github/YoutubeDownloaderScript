from pytube import YouTube
import os

cureent_user = os.getlogin()
print(cureent_user)

#SAVE_PATH = "C:/Users/{cureent_user}/Downloads/YouTube"
SAVE_PATH = 'C:/Users/'+cureent_user+'/Downloads'

link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Rating of video: ",yt.rating)

ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download(SAVE_PATH)
print("Download completed!!")
