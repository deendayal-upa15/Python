# -*- coding: utf-8 -*-
"""
Created on Mon May 20 ‏‎19:10:23 2022 

@author: Deendayal

We are going to make youtube downloader to download videos, playlist and audio from given link, using PyTube library and Exception handling
"""

#importing the libraries
from pytube import YouTube
from pytube import Playlist #for downloading playlist
import os

# Function for downloading a video from link.
# It takes links and path as arguments and downloads video at given path.
def ytdownload(link, path):
    yt = YouTube(link)
    print("Title: ",yt.title)
    """
    # if you want to print you can have these insights
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    print("Rating of video: ",yt.rating)
    """
    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    #Starting download
    print("Downloading...")
    ys.download(path)
    print("Download completed!!")
    
    
# Downloading Playlist:
# It takes link and path as arguments and downloads whole playlist at given path.
def PlaylistDownload(link, path):
    playlist = Playlist(link)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video in playlist.videos:
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download(path)
        print(yt.title + " has been successfully downloaded.")
        
        
# you can also change the name of your preference. here I am using it to give numbering to names of videos
def downloadPlaylist(link, path):
    playlist = Playlist(link)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    i=0
    for video_url in playlist.video_urls:
        yt = YouTube(video_url)
        name = str(i+1)+". "+ yt.title
        print(name)
        i+=1
        yt.streams.get_highest_resolution().download(path, filename=(name))
        print(yt.title + " has been successfully downloaded.")


# Download Audio:
# It takes link and path as arguments and downloads only audio file at given path.        
def DownloadAudio(link, path):
    video = YouTube(link).streams.filter(only_audio=True).first()
    out_file = video.download(path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(YouTube(link).title + " has been successfully downloaded.")
    
    
    
# Main Function for user interaction:
# This function plays in a loop. Takes user input as link and path and interact with user to download requested file. also, it handles exceptions raised in this function.
while True:
    #asking user preferences
    start = str(input("Want to start YouTube Downloader (y/n): "))
    if start == 'n' or start == 'N':
        print('Thank you! See you soon.')
        break
    if start == 'y' or start == 'Y':
        link = str(input("Enter youtube link (video/playlist): "))
        path = str(input("Enter the destination location of download: "))
        while True:
            choice = str(input("Want to download a video(v), Audio(a), or Playlist(p)? (enter 'm' to main menu or v/a/p): \n"))
            if choice == 'v' or choice == 'V':
                try:
                    ytdownload(link,path)
                    print("Thank you!")
                except BaseException:
                    print("Enter valid input (url/path).")
                except OSError:
                    print("Video Title is not valid to save.")
                break
            if choice == 'a' or choice == 'A':
                try:
                    DownloadAudio(link, path)
                    print("Thank you!")
                except BaseException:
                    print("Enter valid input (video/path).")
                except OSError:
                    print("Video Title is not valid to save.")
                break
            if choice == 'p' or choice == 'P':
                try:
                    downloadPlaylist(link, path)
                    print("Thank you!")
                except KeyError:
                    print("Enter valid Playlist url.")
                except OSError:
                    print("Video Title is not valid to save.")
                break
                
            if choice == 'm' or choice == 'M':
                break
            else:
                print("Invalid input please Try again.")
    else:
        print("Invalid input please Try again.")
        

# Exceptions
# KeyError:
# Playlist extracts URLs of videos and other information from the given link if we input only the video URL then it will raise a KeyError. By this, we can understand there is a problem in input and we can fix this without termination of the program.

# OSError:
# Sometimes youtube video titles have some extra symbols, and OS doesn't accept some special characters as naming a file name. This will raise an OSError. In this case, we specify file name is not appropriate for the nomenclature of the file in the system.

# BaseException:
# All exceptions inherit from BaseException, and so it can be used to serve as a wildcard. When we pass the URL of a playlist in the youtube video link the module raises RagexMatchError, Because the passed URL is not a link for the video. Adding BaseException is a better way to handle exceptions raise in the library's specific functions.